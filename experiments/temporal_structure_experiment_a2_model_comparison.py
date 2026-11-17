#!/usr/bin/env python3
"""Experiment A2: predictive comparison of soft vs hard structural change models.

This script asks whether a discrete hard-threshold jump improves predictive log
score relative to (a) Bayesian model averaging over the same candidate models
and (b) a continuous delta-rule learner.

Negative results are informative: if the hard jump does not improve prediction,
a discrete jump should not be justified merely by predictive fit in this task.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from dataclasses import dataclass
from typing import Dict, List, Sequence

from temporal_structure_experiment_a import (
    Config,
    LOG_2PI,
    log_marginal_changed_mean,
    log_marginal_stationary,
    posterior_mean_parameters,
)


@dataclass
class Prepared:
    condition: str
    y: List[float]
    logbf_after: List[float]
    alt_mean_before: List[float]
    alt_var_before: List[float]


def log_normal(y: float, mean: float, variance: float) -> float:
    return -0.5 * (LOG_2PI + math.log(variance) + ((y - mean) ** 2) / variance)


def logsumexp2(a: float, b: float) -> float:
    m = max(a, b)
    return m + math.log(math.exp(a - m) + math.exp(b - m))


def logistic(log_odds: float) -> float:
    if log_odds >= 0:
        e = math.exp(-log_odds)
        return 1.0 / (1.0 + e)
    e = math.exp(log_odds)
    return e / (1.0 + e)


def prepare(condition: str, y: Sequence[float], cfg: Config) -> Prepared:
    logbf_after = []
    alt_mean_before = []
    alt_var_before = []
    for t in range(len(y)):
        if t == 0:
            alt_mean_before.append(0.0)
            alt_var_before.append(
                cfg.observation_variance + cfg.alternative_mean_prior_variance
            )
        else:
            m, v = posterior_mean_parameters(
                y[:t], cfg.observation_variance, cfg.alternative_mean_prior_variance
            )
            alt_mean_before.append(m)
            alt_var_before.append(cfg.observation_variance + v)
        prefix = y[: t + 1]
        logbf_after.append(
            log_marginal_changed_mean(
                prefix,
                cfg.observation_variance,
                cfg.alternative_mean_prior_variance,
            )
            - log_marginal_stationary(prefix, cfg.observation_variance)
        )
    return Prepared(
        condition, list(y), logbf_after, alt_mean_before, alt_var_before
    )


def generate_pairs(n_pairs: int, cfg: Config, seed: int) -> List[Prepared]:
    rng = random.Random(seed)
    out = []
    sd = math.sqrt(cfg.observation_variance)
    for _ in range(n_pairs):
        eps = [rng.gauss(0.0, sd) for _ in range(cfg.horizon - 1)]
        y_out = [cfg.event_value] + eps
        y_change = [cfg.event_value] + [cfg.change_mean + e for e in eps]
        out.append(prepare("outlier", y_out, cfg))
        out.append(prepare("change", y_change, cfg))
    return out


def score_soft(seq: Prepared, cfg: Config, prior_change: float) -> float:
    prior_lo = math.log(prior_change / (1.0 - prior_change))
    scores = []
    for t in range(1, len(seq.y)):
        p = logistic(prior_lo + seq.logbf_after[t - 1])
        p = min(max(p, 1e-15), 1.0 - 1e-15)
        log0 = log_normal(seq.y[t], 0.0, cfg.observation_variance)
        log1 = log_normal(
            seq.y[t], seq.alt_mean_before[t], seq.alt_var_before[t]
        )
        scores.append(
            logsumexp2(math.log1p(-p) + log0, math.log(p) + log1)
        )
    return sum(scores) / len(scores)


def score_hard(
    seq: Prepared,
    cfg: Config,
    prior_change: float,
    threshold: float,
    confirm_steps: int,
) -> float:
    prior_lo = math.log(prior_change / (1.0 - prior_change))
    jumped = False
    run = 0
    scores = []

    p_after_first = logistic(prior_lo + seq.logbf_after[0])
    if p_after_first >= threshold:
        run = 1
        if run >= confirm_steps:
            jumped = True

    for t in range(1, len(seq.y)):
        if jumped:
            ll = log_normal(
                seq.y[t], seq.alt_mean_before[t], seq.alt_var_before[t]
            )
        else:
            ll = log_normal(seq.y[t], 0.0, cfg.observation_variance)
        scores.append(ll)

        if not jumped:
            p = logistic(prior_lo + seq.logbf_after[t])
            if p >= threshold:
                run += 1
                if run >= confirm_steps:
                    jumped = True
            else:
                run = 0
    return sum(scores) / len(scores)


def score_delta(seq: Prepared, cfg: Config, alpha: float) -> float:
    mu = alpha * seq.y[0]
    scores = []
    for t in range(1, len(seq.y)):
        scores.append(log_normal(seq.y[t], mu, cfg.observation_variance))
        mu = mu + alpha * (seq.y[t] - mu)
    return sum(scores) / len(scores)


def mean_score(values: Sequence[float]) -> float:
    return sum(values) / len(values)


def tune(train: Sequence[Prepared], cfg: Config) -> Dict[str, object]:
    soft = []
    for prior in [0.01, 0.03, 0.05, 0.10, 0.20, 0.30, 0.50]:
        score = mean_score([score_soft(x, cfg, prior) for x in train])
        soft.append((score, prior))
    soft.sort(reverse=True)

    hard = []
    for prior in [0.01, 0.03, 0.05, 0.10, 0.20]:
        for threshold in [0.80, 0.90, 0.95, 0.975, 0.99]:
            for confirm in [1, 2, 3]:
                score = mean_score(
                    [
                        score_hard(x, cfg, prior, threshold, confirm)
                        for x in train
                    ]
                )
                hard.append((score, prior, threshold, confirm))
    hard.sort(reverse=True)

    delta = []
    for i in range(1, 96):
        alpha = i / 100.0
        score = mean_score([score_delta(x, cfg, alpha) for x in train])
        delta.append((score, alpha))
    delta.sort(reverse=True)

    return {
        "soft": {
            "train_score": soft[0][0],
            "prior_change": soft[0][1],
        },
        "hard": {
            "train_score": hard[0][0],
            "prior_change": hard[0][1],
            "threshold": hard[0][2],
            "confirm_steps": hard[0][3],
        },
        "delta": {
            "train_score": delta[0][0],
            "alpha": delta[0][1],
        },
    }


def summarize_test(
    test: Sequence[Prepared], cfg: Config, tuned: Dict[str, object]
) -> Dict[str, object]:
    rows = []
    for seq in test:
        soft = score_soft(seq, cfg, tuned["soft"]["prior_change"])
        hard = score_hard(
            seq,
            cfg,
            tuned["hard"]["prior_change"],
            tuned["hard"]["threshold"],
            tuned["hard"]["confirm_steps"],
        )
        delta = score_delta(seq, cfg, tuned["delta"]["alpha"])
        rows.append((seq.condition, soft, hard, delta))

    by_condition = {}
    for condition in ("outlier", "change"):
        subset = [r for r in rows if r[0] == condition]
        by_condition[condition] = {
            "n": len(subset),
            "mean_log_predictive_density_soft": mean_score(
                [r[1] for r in subset]
            ),
            "mean_log_predictive_density_hard": mean_score(
                [r[2] for r in subset]
            ),
            "mean_log_predictive_density_delta": mean_score(
                [r[3] for r in subset]
            ),
            "mean_soft_minus_hard": mean_score(
                [r[1] - r[2] for r in subset]
            ),
            "mean_soft_minus_delta": mean_score(
                [r[1] - r[3] for r in subset]
            ),
            "mean_hard_minus_delta": mean_score(
                [r[2] - r[3] for r in subset]
            ),
        }

    soft = [r[1] for r in rows]
    hard = [r[2] for r in rows]
    delta = [r[3] for r in rows]

    def diff_summary(a: Sequence[float], b: Sequence[float]) -> Dict[str, float]:
        d = [x - y for x, y in zip(a, b)]
        mean = statistics.mean(d)
        se = statistics.stdev(d) / math.sqrt(len(d))
        return {
            "mean": mean,
            "se": se,
            "normal_approx_95_low": mean - 1.96 * se,
            "normal_approx_95_high": mean + 1.96 * se,
        }

    return {
        "overall": {
            "n_sequences": len(rows),
            "mean_log_predictive_density_soft": mean_score(soft),
            "mean_log_predictive_density_hard": mean_score(hard),
            "mean_log_predictive_density_delta": mean_score(delta),
            "soft_minus_hard": diff_summary(soft, hard),
            "soft_minus_delta": diff_summary(soft, delta),
            "hard_minus_delta": diff_summary(hard, delta),
        },
        "by_condition": by_condition,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=None)
    parser.add_argument("--train-pairs", type=int, default=2000)
    parser.add_argument("--test-pairs", type=int, default=5000)
    args = parser.parse_args()

    cfg = Config()
    train = generate_pairs(args.train_pairs, cfg, seed=100)
    test = generate_pairs(args.test_pairs, cfg, seed=200)
    tuned = tune(train, cfg)
    test_summary = summarize_test(test, cfg, tuned)

    payload = {
        "status": "synthetic predictive model comparison; not human validation",
        "config": {
            "train_pairs": args.train_pairs,
            "test_pairs": args.test_pairs,
            "event_value": cfg.event_value,
            "change_mean": cfg.change_mean,
            "horizon": cfg.horizon,
        },
        "tuned_on_training_set": tuned,
        "heldout_test": test_summary,
        "decision": {
            "hard_jump_predictive_advantage_over_soft": (
                test_summary["overall"]["mean_log_predictive_density_hard"]
                > test_summary["overall"]["mean_log_predictive_density_soft"]
            ),
            "interpretation": (
                "A discrete hard jump is not justified by predictive log score "
                "in this minimal task if Bayesian model averaging performs better. "
                "Jump structure may still be relevant for segmentation, "
                "representation, or other observables, but that requires separate evidence."
            ),
        },
    }

    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
