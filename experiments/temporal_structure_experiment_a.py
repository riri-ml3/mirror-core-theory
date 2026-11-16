#!/usr/bin/env python3
"""Synthetic Experiment A for the Temporal Structure Bridge.

Goal
----
Test whether an identical initial surprising observation can later be
classified differently as:
  (1) a one-off outlier, or
  (2) evidence for a persistent regime change.

This is a model-identifiability / falsification-preparation experiment.
It is NOT evidence that human structural time Theta_O has been validated.

Dependencies: Python standard library only.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


LOG_2PI = math.log(2.0 * math.pi)


@dataclass(frozen=True)
class Config:
    n_replications: int = 5000
    horizon: int = 20
    event_value: float = 3.5
    change_mean: float = 2.0
    observation_variance: float = 1.0
    alternative_mean_prior_variance: float = 4.0
    prior_change_probability: float = 0.05
    jump_threshold: float = 0.95
    confirm_steps: int = 2
    seed: int = 42


@dataclass
class TrialResult:
    condition: str
    detected: bool
    detect_step: Optional[int]
    c_pred: float
    r_struct_final: float
    p_heldout: Optional[float]
    p_change_step1: float
    p_change_final: float


def normal_surprise(y: float, mean: float = 0.0, variance: float = 1.0) -> float:
    return 0.5 * (LOG_2PI + math.log(variance) + ((y - mean) ** 2) / variance)


def posterior_mean_parameters(
    observations: Sequence[float],
    observation_variance: float,
    prior_variance: float,
    prior_mean: float = 0.0,
) -> Tuple[float, float]:
    n = len(observations)
    prior_precision = 1.0 / prior_variance
    precision = prior_precision + n / observation_variance
    variance = 1.0 / precision
    mean = variance * (
        prior_mean / prior_variance
        + sum(observations) / observation_variance
    )
    return mean, variance


def kl_normal_q_to_p(
    q_mean: float,
    q_variance: float,
    p_mean: float,
    p_variance: float,
) -> float:
    return 0.5 * (
        q_variance / p_variance
        + ((p_mean - q_mean) ** 2) / p_variance
        - 1.0
        + math.log(p_variance / q_variance)
    )


def log_marginal_stationary(
    observations: Sequence[float], observation_variance: float
) -> float:
    n = len(observations)
    sum_sq = sum(y * y for y in observations)
    return -0.5 * (
        n * (LOG_2PI + math.log(observation_variance))
        + sum_sq / observation_variance
    )


def log_marginal_changed_mean(
    observations: Sequence[float],
    observation_variance: float,
    prior_variance: float,
) -> float:
    """Marginal likelihood for y_i ~ N(mu, sigma^2), mu ~ N(0, tau^2)."""
    n = len(observations)
    s = sum(observations)
    sum_sq = sum(y * y for y in observations)
    sigma2 = observation_variance
    tau2 = prior_variance

    logdet = (n - 1) * math.log(sigma2) + math.log(sigma2 + n * tau2)
    quad = (
        sum_sq / sigma2
        - tau2 * s * s / (sigma2 * (sigma2 + n * tau2))
    )
    return -0.5 * (n * LOG_2PI + logdet + quad)


def logistic_from_log_odds(log_odds: float) -> float:
    if log_odds >= 0.0:
        e = math.exp(-log_odds)
        return 1.0 / (1.0 + e)
    e = math.exp(log_odds)
    return e / (1.0 + e)


def posterior_change_path(observations: Sequence[float], cfg: Config) -> List[float]:
    prior_log_odds = math.log(
        cfg.prior_change_probability / (1.0 - cfg.prior_change_probability)
    )
    output: List[float] = []
    for n in range(1, len(observations) + 1):
        prefix = observations[:n]
        log_bf = (
            log_marginal_changed_mean(
                prefix,
                cfg.observation_variance,
                cfg.alternative_mean_prior_variance,
            )
            - log_marginal_stationary(prefix, cfg.observation_variance)
        )
        output.append(logistic_from_log_odds(prior_log_odds + log_bf))
    return output


def first_confirmed_crossing(
    probabilities: Sequence[float], threshold: float, confirm_steps: int
) -> Optional[int]:
    """Return one-based first step of a confirmed threshold run."""
    run = 0
    for zero_idx, value in enumerate(probabilities):
        if value >= threshold:
            run += 1
            if run >= confirm_steps:
                first_zero_idx = zero_idx - confirm_steps + 1
                return first_zero_idx + 1
        else:
            run = 0
    return None


def predictive_kl_from_baseline(mean: float, posterior_variance: float) -> float:
    """KL[N(mean, 1+v) || N(0,1)] in the shared observation space."""
    pred_variance = 1.0 + posterior_variance
    return 0.5 * (
        pred_variance + mean * mean - 1.0 - math.log(pred_variance)
    )


def predictive_log_density(y: float, mean: float, variance: float) -> float:
    return -0.5 * (
        LOG_2PI + math.log(variance) + ((y - mean) ** 2) / variance
    )


def evaluate_sequence(condition: str, observations: Sequence[float], cfg: Config) -> TrialResult:
    p_path = posterior_change_path(observations, cfg)
    detect_step = first_confirmed_crossing(
        p_path, cfg.jump_threshold, cfg.confirm_steps
    )

    if detect_step is None:
        return TrialResult(
            condition=condition,
            detected=False,
            detect_step=None,
            c_pred=0.0,
            r_struct_final=p_path[-1],
            p_heldout=None,
            p_change_step1=p_path[0],
            p_change_final=p_path[-1],
        )

    fitted = observations[:detect_step]
    mean, variance = posterior_mean_parameters(
        fitted,
        cfg.observation_variance,
        cfg.alternative_mean_prior_variance,
    )
    c_pred = predictive_kl_from_baseline(mean, variance)

    start = detect_step
    end = min(len(observations), detect_step + 5)
    p_heldout: Optional[float]
    if end > start:
        pred_variance = cfg.observation_variance + variance
        gains = []
        for y in observations[start:end]:
            ll0 = predictive_log_density(y, 0.0, cfg.observation_variance)
            ll1 = predictive_log_density(y, mean, pred_variance)
            gains.append(ll1 - ll0)
        p_heldout = sum(gains) / len(gains)
    else:
        p_heldout = None

    return TrialResult(
        condition=condition,
        detected=True,
        detect_step=detect_step,
        c_pred=c_pred,
        r_struct_final=p_path[-1],
        p_heldout=p_heldout,
        p_change_step1=p_path[0],
        p_change_final=p_path[-1],
    )


def median_or_none(values: Iterable[Optional[float]]) -> Optional[float]:
    kept = [x for x in values if x is not None]
    if not kept:
        return None
    return statistics.median(kept)


def summarize(results: Sequence[TrialResult]) -> Dict[str, Dict[str, Optional[float]]]:
    out: Dict[str, Dict[str, Optional[float]]] = {}
    for condition in ("outlier", "change"):
        subset = [r for r in results if r.condition == condition]
        out[condition] = {
            "n": len(subset),
            "detection_rate": sum(r.detected for r in subset) / len(subset),
            "median_detect_step_detected_only": median_or_none(
                float(r.detect_step) if r.detect_step is not None else None
                for r in subset
            ),
            "mean_c_pred_all_trials": sum(r.c_pred for r in subset) / len(subset),
            "median_r_struct_final": statistics.median(
                r.r_struct_final for r in subset
            ),
            "median_p_heldout_detected_only": median_or_none(
                r.p_heldout for r in subset
            ),
            "mean_p_change_step1": sum(r.p_change_step1 for r in subset) / len(subset),
            "mean_p_change_final": sum(r.p_change_final for r in subset) / len(subset),
        }
    return out


def simulate(cfg: Config) -> Tuple[List[TrialResult], Dict[str, float]]:
    rng = random.Random(cfg.seed)
    results: List[TrialResult] = []

    first_mean, first_variance = posterior_mean_parameters(
        [cfg.event_value],
        cfg.observation_variance,
        cfg.alternative_mean_prior_variance,
    )
    first_g = kl_normal_q_to_p(
        first_mean,
        first_variance,
        0.0,
        cfg.alternative_mean_prior_variance,
    )
    first_surprise = normal_surprise(
        cfg.event_value, 0.0, cfg.observation_variance
    )

    for _ in range(cfg.n_replications):
        epsilon = [
            rng.gauss(0.0, math.sqrt(cfg.observation_variance))
            for _ in range(cfg.horizon - 1)
        ]
        outlier = [cfg.event_value] + epsilon
        changed = [cfg.event_value] + [cfg.change_mean + e for e in epsilon]
        results.append(evaluate_sequence("outlier", outlier, cfg))
        results.append(evaluate_sequence("change", changed, cfg))

    matched = {
        "initial_surprise_nats_both_conditions": first_surprise,
        "initial_bayesian_information_gain_G_nats_both_conditions": first_g,
        "posterior_mean_after_first_event": first_mean,
        "posterior_variance_after_first_event": first_variance,
    }
    return results, matched


def run_sweep(base: Config, replications_per_cell: int = 800) -> Dict[str, object]:
    cells = []
    for event_value in (3.0, 3.5, 4.0):
        for change_mean in (1.0, 1.5, 2.0):
            for prior_change_probability in (0.01, 0.05, 0.10):
                for jump_threshold in (0.90, 0.95, 0.99):
                    cfg = Config(
                        n_replications=replications_per_cell,
                        horizon=base.horizon,
                        event_value=event_value,
                        change_mean=change_mean,
                        observation_variance=base.observation_variance,
                        alternative_mean_prior_variance=base.alternative_mean_prior_variance,
                        prior_change_probability=prior_change_probability,
                        jump_threshold=jump_threshold,
                        confirm_steps=base.confirm_steps,
                        seed=123,
                    )
                    results, _ = simulate(cfg)
                    summary = summarize(results)
                    cells.append({
                        "event_value": event_value,
                        "change_mean": change_mean,
                        "prior_change_probability": prior_change_probability,
                        "jump_threshold": jump_threshold,
                        "false_positive_rate": summary["outlier"]["detection_rate"],
                        "true_positive_rate": summary["change"]["detection_rate"],
                    })

    fprs = [c["false_positive_rate"] for c in cells]
    tprs = [c["true_positive_rate"] for c in cells]
    return {
        "replications_per_cell": replications_per_cell,
        "n_cells": len(cells),
        "median_false_positive_rate": statistics.median(fprs),
        "median_true_positive_rate": statistics.median(tprs),
        "min_true_positive_rate": min(tprs),
        "max_false_positive_rate": max(fprs),
        "cells": cells,
    }


def compare_confirmation_rule(base: Config) -> Dict[str, object]:
    comparisons = {}
    for confirm_steps in (1, 2):
        cfg = Config(**{**asdict(base), "confirm_steps": confirm_steps})
        results, _ = simulate(cfg)
        comparisons[str(confirm_steps)] = summarize(results)
    return comparisons


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=None, help="Write JSON results to this path")
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    cfg = Config(n_replications=args.n, seed=args.seed)
    results, matched = simulate(cfg)
    payload = {
        "status": "synthetic model-identifiability experiment; not human validation",
        "config": asdict(cfg),
        "matched_initial_quantities": matched,
        "baseline_summary": summarize(results),
        "confirmation_rule_comparison": compare_confirmation_rule(cfg),
        "robustness_sweep": run_sweep(cfg),
        "interpretation_boundary": {
            "supported_by_simulation": [
                "identical initial surprise and G can later yield different persistent model evidence",
                "a two-step confirmation rule can reduce outlier false positives in this minimal model",
                "G and jump/model-structure evidence are computationally separable in this setup"
            ],
            "not_supported_by_simulation": [
                "human Theta_O exists as a biological variable",
                "the chosen thresholds are universal",
                "physical time emerges from information",
                "the model is empirically superior to existing human event-segmentation models"
            ]
        }
    }

    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
