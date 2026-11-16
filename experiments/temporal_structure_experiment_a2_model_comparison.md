# Synthetic Experiment A2 — Continuous vs Hard-Jump Predictive Comparison
## Temporal Structure Bridge / v0.2 Draft

---

## 0. Status

### English
This experiment directly tests whether a discrete hard-threshold jump is justified by **predictive performance** in the same synthetic outlier/change-point environment used in Experiment A.

Three models are compared:

1. Bayesian model averaging (soft structural evidence)
2. hard-threshold jump model
3. continuous delta-rule learner

The result is intentionally treated as a falsification-oriented test. A negative result is retained rather than optimized away.

### 日本語
本実験は、Experiment A と同一種の合成環境において、離散的な hard jump が**予測性能上必要か**を直接検査するものである。

比較対象は以下である。

1. Bayesian model averaging による soft model
2. 閾値を超えると離散的に切り替わる hard-jump model
3. 連続的な delta-rule learner

否定的結果もそのまま保持し、ジャンプ仮説に有利になるよう事後的に条件を変更しない。

---

## 1. Why this test is necessary / なぜ必要か

Experiment A showed that identical initial surprise and identical immediate Bayesian information gain can later diverge into:

- transient outlier evidence, or
- persistent structural-change evidence.

However, that result alone does not show that a **discrete jump mechanism** is needed.

A continuous probabilistic model may retain uncertainty over candidate models and predict better without committing to a hard switch.

Therefore the stronger question is:

`Does hard J improve held-out prediction relative to soft model uncertainty?`

---

## 2. Models

### M_soft — Bayesian model averaging

Before each future observation, predictions from the stationary model and changed-mean model are weighted by posterior model probability.

This model allows structural evidence to change continuously.

### M_hard — discrete jump

The system remains in the stationary model until:

`P(change | D_t) >= threshold`

for the required number of confirmation steps.

After crossing the threshold, prediction is made from the changed-mean model.

### M_delta — continuous delta rule

`mu_(t+1) = mu_t + alpha (y_t - mu_t)`

This model contains no explicit latent structural switch.

---

## 3. Train/test separation

Training data:

- 2000 paired outlier/change sequences
- seed = 100

Held-out test data:

- 5000 paired outlier/change sequences
- 10000 sequences total
- seed = 200

All tuning was performed on the training set only.

### Tuned parameters

Soft model:

- prior change probability = 0.01

Hard model:

- prior change probability = 0.20
- threshold = 0.95
- confirmation steps = 1

Delta model:

- learning rate `alpha = 0.24`

The hard model was therefore allowed to select its own best predictive threshold from the predefined grid; it was not forced to use the Experiment A value.

---

## 4. Held-out predictive results

Higher mean log predictive density is better.

| Model | Overall held-out mean log predictive density |
|---|---:|
| Soft Bayesian model averaging | **-1.49444** |
| Hard jump | -1.54468 |
| Continuous delta rule | -1.54610 |

Paired difference:

`soft - hard = +0.05024`

normal-approximation 95% interval:

`[+0.04809, +0.05239]`

Thus the soft model had a clear held-out predictive advantage over the tuned hard-jump model in this task.

The difference between hard jump and delta rule was small:

`hard - delta = +0.00142`

95% interval:

`[-0.00120, +0.00405]`

Therefore the hard-jump model did not show a reliable overall predictive advantage over the simple continuous delta learner either.

---

## 5. Condition-specific results

### Outlier condition

| Model | Mean log predictive density |
|---|---:|
| Soft | **-1.44692** |
| Hard | -1.45806 |
| Delta | -1.52563 |

Differences:

- soft - hard = +0.01114
- hard - delta = +0.06757

The hard model handled outliers better than the simple delta rule, but still underperformed Bayesian model averaging.

### Change-point condition

| Model | Mean log predictive density |
|---|---:|
| Soft | **-1.54196** |
| Delta | -1.56658 |
| Hard | -1.63130 |

Differences:

- soft - hard = +0.08934
- soft - delta = +0.02462
- hard - delta = -0.06473

The largest failure of the hard model occurred under persistent change: thresholded commitment delayed or distorted adaptation relative to the soft Bayesian mixture.

---

## 6. Interpretation / 解釈

### Result

`hard jump predictive advantage = NOT SUPPORTED`

in this minimal synthetic task.

This matters because the original Temporal Structure Bridge included:

`TP4 — hybrid threshold / hysteresis`

as a candidate prediction.

The present result does not fully falsify TP4, because TP4 refers to a broader class of tasks and observables. However, it directly shows that:

`discrete jump != automatically better prediction`

and therefore jump structure cannot be justified merely by predictive accuracy in this setup.

### Why the soft model can win

Bayesian model averaging preserves uncertainty over candidate models instead of prematurely selecting one model and discarding the other. Under log-score prediction this can be advantageous because the predictive distribution integrates model uncertainty rather than treating a threshold crossing as certainty.

This is consistent with the established statistical motivation for Bayesian model averaging.

---

## 7. Consequence for the theory / 理論への修正

The role of `J` should now be narrowed.

### Do not claim

`J is required because discrete switching predicts the environment better.`

This claim is not supported by Experiment A2.

### Keep open

`J may represent a discrete change in representation, segmentation, preservation schema, accessibility, or behavioral state even when the optimal predictive distribution changes continuously.`

This distinction is critical.

A system can have:

- continuous probabilistic belief updating at the predictive level,
- while still showing discrete representational or behavioral reorganization at another level.

Therefore:

`predictive continuity != representational continuity`

and:

`predictive jump != required condition for structural jump`

---

## 8. Revised interpretation of TP4

Original strong reading:

> A hybrid jump model should outperform continuous learning in regime-switching tasks.

This is too strong.

Revised testable reading:

> If `J` is an independent structural event, jump-linked observables should show discrete or hysteretic organization that cannot be explained solely by continuous posterior belief or continuous prediction error.

Candidate observables include:

- event-boundary reports,
- categorical strategy switches,
- representational separation,
- delayed schema persistence,
- abrupt changes in temporal-order organization,
- neural state-space transitions.

Predictive log score alone is no longer treated as the primary validation target for `J`.

---

## 9. Falsification update

The current evidence moves the project closer to T-F4 for the narrow predictive interpretation.

A stronger falsification condition is now:

**T-F4r** — If across appropriately designed tasks, all apparent jumps are fully explained by continuous posterior belief trajectories and no independent discontinuity appears in representation, memory organization, behavior, or temporal reconstruction, the independent jump variable `J` should be removed from the temporal-structure model.

This is stricter and more informative than demanding predictive superiority of hard thresholding.

---

## 10. Literature boundary

Bayesian model averaging was developed precisely to retain uncertainty across candidate models rather than choosing one model and proceeding as if model selection were certain. Hoeting et al. (1999) review improved out-of-sample predictive performance from such averaging in multiple examples.

Relevant comparison:

- Hoeting JA, Madigan D, Raftery AE, Volinsky CT. Bayesian Model Averaging: A Tutorial. Statistical Science. 1999;14(4):382-417. DOI: 10.1214/ss/1009212519.

This literature is not evidence for the Temporal Structure Bridge itself. It explains why a soft model can legitimately outperform hard threshold selection on predictive log score.

---

## 11. Reproducibility

Implementation:

`experiments/temporal_structure_experiment_a2_model_comparison.py`

Run from the experiments directory or repository environment where Experiment A is importable.

Default:

`python experiments/temporal_structure_experiment_a2_model_comparison.py`

Optional JSON output:

`python experiments/temporal_structure_experiment_a2_model_comparison.py --output a2_results.json`

---

## 12. Decision

### Experiment A
PASS for computational separation of immediate surprise and persistent structural evidence.

### Experiment A2
FAIL for the stronger claim that hard discrete jumping improves held-out prediction.

### Current theoretical implication

The jump concept remains viable only if it refers to a structural/representational transition that has evidence beyond predictive thresholding.

The next appropriate experiment is therefore **not** another attempt to tune the hard threshold until it wins.

The next experiment should test whether a latent discrete representational state is identifiable from observables such as event segmentation, memory separation, temporal-order reconstruction, or delayed schema persistence after controlling for continuous posterior belief.
