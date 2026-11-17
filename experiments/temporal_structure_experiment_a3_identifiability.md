# Temporal Structure Experiment A3 — Synthetic Identifiability Result
## Null continuous world vs imposed independent hysteretic-state world

> Status: synthetic model-identifiability sanity check
> This result does not validate human `J`, `Theta_O`, or physical-time emergence.

---

## 1. Question / 問い

Experiment A2 showed that a hard predictive jump was not required for held-out environmental prediction.

A3 therefore asks a narrower question:

> If an observable contains an independent hysteretic structural state beyond a smooth continuous posterior-like variable, can a held-out model-comparison procedure detect that extra state without falsely preferring it in a continuous-only world?

---

## 2. Generative worlds / 生成世界

### Null world

The binary observable is generated only from a smooth continuous posterior-like variable `p_t`.

No independent discrete state contributes to the observation.

### True-J synthetic world

The same smooth `p_t` is present, but an additional hysteretic state `Z_J(t)` contributes independently.

The imposed synthetic state switches on/off using separate thresholds.

This is intentionally a known-ground-truth world for identifiability testing.

---

## 3. Competing models / 比較モデル

### Continuous model

Uses smooth functions of `logit(p_t)` only.

### Continuous + candidate-J model

Uses the same continuous features plus an inferred hysteretic state.

The candidate-J thresholds are tuned on training data only.

Held-out test data are then evaluated without retuning.

---

## 4. Decision rule / 判定規則

Independent `J` is supported for a replication only when:

`held-out log-loss improvement = loss_continuous - loss_J`

has a sequence-level normal-approximation 95% lower bound above zero.

This is a diagnostic simulation rule, not a universal scientific threshold.

---

## 5. Baseline configuration / 基準条件

- 12 independent train/test replications per world
- training: 100 sequences per replication
- test: 220 sequences per replication
- horizon: 80 steps
- observation-noise parameter: `0.18`
- imposed true-J effect: `1.4` in the True-J world
- true synthetic hysteresis thresholds: on `0.72`, off `0.38`
- candidate threshold grid tuned on training data only

---

## 6. Baseline results / 基準結果

### Null continuous world

- mean held-out log-loss improvement from adding candidate J: `-0.000207`
- observed range across 12 replications: `[-0.000537, -0.000059]`
- replications with 95% lower bound above zero: `0 / 12`
- empirical false-support rate under this baseline: `0.00`

Interpretation:

The candidate-J model did not gain held-out explanatory value when the data-generating world contained no independent jump state. In this baseline it slightly worsened held-out log loss.

### True-J synthetic world

- mean held-out log-loss improvement: `+0.008088`
- observed range across 12 replications: `[+0.005887, +0.009411]`
- replications with 95% lower bound above zero: `12 / 12`
- empirical support rate under this baseline: `1.00`
- mean Brier-score improvement: `+0.003387`
- median selected candidate thresholds: on `0.76`, off `0.34`

Interpretation:

Under the imposed synthetic independent-state world, the model-comparison procedure recovered additional held-out explanatory value beyond the continuous posterior-like predictor.

---

## 7. Sensitivity sweep / 感度走査

Five train/test replications were run in each cell.

| Noise | Imposed J effect | Mean held-out log-loss improvement | 95%-support rate |
|---:|---:|---:|---:|
| 0.12 | 0.4 | 0.000208 | 0.0 |
| 0.12 | 0.8 | 0.002651 | 0.8 |
| 0.12 | 1.2 | 0.005325 | 1.0 |
| 0.12 | 1.6 | 0.009636 | 1.0 |
| 0.30 | 0.4 | 0.000285 | 0.2 |
| 0.30 | 0.8 | 0.002200 | 0.8 |
| 0.30 | 1.2 | 0.005304 | 1.0 |
| 0.30 | 1.6 | 0.008677 | 1.0 |

### Sensitivity interpretation

The detection procedure is not parameter-free.

When the independent structural contribution is weak (`effect = 0.4`), support is poor even though the discrete state is truly present in the generator.

At moderate-to-large imposed effects (`>= 0.8` in this particular synthetic design), recovery becomes substantially more reliable.

Therefore:

`failure to detect J != proof that no J exists`

unless the expected effect size and measurement sensitivity are adequately constrained.

---

## 8. What this result establishes / 何が確認できたか

The simulation supports only the following methodological statement:

> In this specified synthetic architecture, a held-out model-comparison procedure can distinguish a continuous-only generator from a generator containing an additional hysteretic state when the independent effect is sufficiently strong.

It does not establish:

- that human representation changes are discrete
- that Mirror Core `J` exists in temporal cognition
- that the true psychological mechanism is hysteresis
- that the fitted threshold values are universal
- that `Theta_O` is empirically validated
- that physical time emerges from information

---

## 9. Consequence for T-F4r / 反証条件への含意

The A3 procedure is now suitable for a stronger falsification test because it has at least passed a minimal synthetic identifiability check.

The theoretical rule remains:

**T-F4r** — If appropriately designed empirical tasks show that continuous posterior-belief trajectories and known event-boundary variables explain all apparent transition phenomena, with no independent held-out contribution from representational, memory, behavioral, temporal-order, or persistence discontinuities, remove independent `J` from the Temporal Structure Bridge.

---

## 10. Next step / 次工程

The next stage is not further threshold tuning.

The next stage is to define an empirical/human-level A3 design in which:

1. continuous posterior belief is explicitly estimated;
2. event-boundary and prediction-error variables are controlled;
3. candidate representational observables are measured independently;
4. prospective and retrospective psychological time are separated;
5. `J` is retained only if it adds held-out explanatory value beyond continuous and known psychological mechanisms.

---

## 11. Reproducibility

Implementation:

`experiments/temporal_structure_experiment_a3_identifiability.py`

Run:

`python experiments/temporal_structure_experiment_a3_identifiability.py`

Optional JSON output:

`python experiments/temporal_structure_experiment_a3_identifiability.py --output a3_identifiability_results.json`