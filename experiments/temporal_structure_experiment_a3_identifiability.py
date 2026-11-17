#!/usr/bin/env python3
"""Experiment A3: synthetic identifiability of an independent hysteretic structural state.

This experiment does NOT validate human J or Theta_O.
It asks whether a model-comparison procedure can distinguish:

1. a null world in which an observable is generated entirely from a smooth
   continuous posterior-like variable p_t; and
2. a true-J synthetic world in which the same smooth variable is present but
   an additional hysteretic latent state contributes independently.

The independent-J model is supported only when its held-out sequence-level
log-loss improvement has a normal-approximation 95% interval above zero.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np
from scipy.special import expit, logit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss


GRID = [
    (on, off)
    for on in [0.60, 0.68, 0.76, 0.84]
    for off in [0.24, 0.34, 0.44, 0.54]
    if off < on - 0.08
]


def make_dataset(
    seed: int,
    n_sequences: int,
    horizon: int = 80,
    noise: float = 0.18,
    jump_effect: float = 1.4,
    true_jump: bool = False,
    true_on: float = 0.72,
    true_off: float = 0.38,
):
    rng = np.random.default_rng(seed)
    p_all = np.zeros((n_sequences, horizon))
    y_all = np.zeros((n_sequences, horizon), dtype=int)
    z_all = np.zeros((n_sequences, horizon), dtype=int)

    for s in range(n_sequences):
        t = np.arange(horizon)
        up_center = rng.uniform(18, 30)
        down_center = rng.uniform(50, 65)
        slope_up = rng.uniform(0.13, 0.22)
        slope_down = rng.uniform(0.12, 0.20)

        x = (
            -2.2
            + 5.2 * expit((t - up_center) * slope_up)
            - 5.0 * expit((t - down_center) * slope_down)
            + rng.normal(0, noise, horizon)
        )
        p = expit(x)
        p_all[s] = p

        state = 0
        for i, value in enumerate(p):
            if state == 0 and value >= true_on:
                state = 1
            elif state == 1 and value <= true_off:
                state = 0
            z_all[s, i] = state

        eta = -0.3 + 1.15 * logit(np.clip(p, 1e-6, 1 - 1e-6))
        if true_jump:
            eta = eta + jump_effect * z_all[s]

        y_all[s] = rng.binomial(1, expit(eta))

    return p_all, y_all, z_all


def hysteresis_feature(p_all, threshold_on, threshold_off):
    n_sequences, horizon = p_all.shape
    z = np.zeros((n_sequences, horizon), dtype=int)

    for s in range(n_sequences):
        state = 0
        for t in range(horizon):
            value = p_all[s, t]
            if state == 0 and value >= threshold_on:
                state = 1
            elif state == 1 and value <= threshold_off:
                state = 0
            z[s, t] = state
    return z


def continuous_features(p_all):
    lp = logit(np.clip(p_all.ravel(), 1e-6, 1 - 1e-6))
    return np.column_stack([lp, lp ** 2])


def fit_and_evaluate(p_train, y_train, p_test, y_test):
    x_train = continuous_features(p_train)
    y_train_flat = y_train.ravel()
    x_test = continuous_features(p_test)
    y_test_flat = y_test.ravel()

    continuous_model = LogisticRegression(C=1e5, max_iter=300)
    continuous_model.fit(x_train, y_train_flat)

    best = None
    for threshold_on, threshold_off in GRID:
        z_train = hysteresis_feature(
            p_train, threshold_on, threshold_off
        ).ravel()
        x_jump = np.column_stack([x_train, z_train])

        model = LogisticRegression(C=1e5, max_iter=300)
        model.fit(x_jump, y_train_flat)

        train_loss = log_loss(
            y_train_flat,
            model.predict_proba(x_jump)[:, 1],
        )

        if best is None or train_loss < best[0]:
            best = (
                train_loss,
                threshold_on,
                threshold_off,
                model,
            )

    _, threshold_on, threshold_off, jump_model = best

    prob_cont = continuous_model.predict_proba(x_test)[:, 1]
    z_test = hysteresis_feature(
        p_test, threshold_on, threshold_off
    ).ravel()
    prob_jump = jump_model.predict_proba(
        np.column_stack([x_test, z_test])
    )[:, 1]

    eps = 1e-15
    y = y_test_flat

    loss_cont = -(
        y * np.log(np.clip(prob_cont, eps, 1 - eps))
        + (1 - y) * np.log(np.clip(1 - prob_cont, eps, 1 - eps))
    )
    loss_jump = -(
        y * np.log(np.clip(prob_jump, eps, 1 - eps))
        + (1 - y) * np.log(np.clip(1 - prob_jump, eps, 1 - eps))
    )

    sequence_difference = (
        (loss_cont - loss_jump)
        .reshape(p_test.shape)
        .mean(axis=1)
    )

    mean_difference = float(sequence_difference.mean())
    se = float(
        sequence_difference.std(ddof=1)
        / math.sqrt(len(sequence_difference))
    )

    return {
        "threshold_on": threshold_on,
        "threshold_off": threshold_off,
        "heldout_logloss_improvement": mean_difference,
        "normal_95_low": mean_difference - 1.96 * se,
        "normal_95_high": mean_difference + 1.96 * se,
        "continuous_brier": brier_score_loss(y, prob_cont),
        "jump_brier": brier_score_loss(y, prob_jump),
        "jump_supported_95": (mean_difference - 1.96 * se) > 0,
    }


def replicate(
    true_jump,
    n_replications=12,
    train_sequences=100,
    test_sequences=220,
    noise=0.18,
    jump_effect=1.4,
):
    rows = []
    for r in range(n_replications):
        p_train, y_train, _ = make_dataset(
            2000 + 2 * r,
            train_sequences,
            noise=noise,
            jump_effect=jump_effect,
            true_jump=true_jump,
        )
        p_test, y_test, _ = make_dataset(
            2001 + 2 * r,
            test_sequences,
            noise=noise,
            jump_effect=jump_effect,
            true_jump=true_jump,
        )
        rows.append(fit_and_evaluate(
            p_train, y_train, p_test, y_test
        ))
    return rows


def summarize(rows):
    improvements = np.array(
        [r["heldout_logloss_improvement"] for r in rows]
    )
    return {
        "mean_heldout_logloss_improvement": float(improvements.mean()),
        "min_improvement": float(improvements.min()),
        "max_improvement": float(improvements.max()),
        "support_rate_95": float(np.mean([
            r["jump_supported_95"] for r in rows
        ])),
        "mean_brier_improvement": float(np.mean([
            r["continuous_brier"] - r["jump_brier"]
            for r in rows
        ])),
    }


def run_sweep():
    output = []
    for noise in [0.12, 0.30]:
        for jump_effect in [0.4, 0.8, 1.2, 1.6]:
            rows = []
            for r in range(5):
                seed_offset = int(jump_effect * 10) + int(noise * 100)
                p_train, y_train, _ = make_dataset(
                    5000 + 100 * r + seed_offset,
                    70,
                    noise=noise,
                    jump_effect=jump_effect,
                    true_jump=True,
                )
                p_test, y_test, _ = make_dataset(
                    5001 + 100 * r + seed_offset,
                    140,
                    noise=noise,
                    jump_effect=jump_effect,
                    true_jump=True,
                )
                rows.append(fit_and_evaluate(
                    p_train, y_train, p_test, y_test
                ))
            s = summarize(rows)
            output.append({
                "noise": noise,
                "jump_effect": jump_effect,
                **s,
            })
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    null_rows = replicate(False)
    true_rows = replicate(True)

    payload = {
        "status": (
            "synthetic identifiability sanity check; "
            "not validation of human J or Theta_O"
        ),
        "baseline": {
            "null_world": summarize(null_rows),
            "true_J_world": summarize(true_rows),
        },
        "sensitivity_sweep_true_J": run_sweep(),
        "decision_rule": (
            "support independent J only when the held-out "
            "sequence-level log-loss improvement has a "
            "normal-approximation 95% lower bound above zero"
        ),
    }

    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
