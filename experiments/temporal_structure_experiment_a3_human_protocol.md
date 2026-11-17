# Temporal Structure Experiment A3 — Human-Level Protocol Draft
## Continuous inference vs independent representational reorganization

> Status: preregistration-oriented human-study design draft
> Scope: empirical test of independent temporal-Bridge J; not a test of physical-time emergence.

---

## 0. Core question / 中心問い

After continuous posterior belief, prediction error, prediction uncertainty, event-boundary variables, boredom, engagement, attention-to-time, and memory strength are modeled, does an additional representational transition variable `J` retain reproducible held-out explanatory value?

Required distinction:

`continuous inference != independent representational jump`

Only data can determine whether the right-hand term is needed.

---

## 1. Main hypotheses / 主仮説

### H1 — Independent representation hypothesis

At least one representational or memory-organization observable shows a reproducible discrete/hysteretic component not reducible to continuous posterior belief or known boundary variables.

### H2 — Persistence hypothesis

Putative structural transitions that persist into later memory/model organization should explain delayed temporal-order organization better than immediate surprise alone.

### H3 — Psychological-time hypothesis

`Theta_O` is not identified with subjective time. Structural-history variables may add explanatory value primarily for retrospective reconstruction `Psi_retro`, not necessarily for online/prospective time `Psi_pro`.

### H0 / reduction hypothesis

Continuous posterior belief plus known psychological/event variables explains the data adequately; independent temporal-Bridge `J` is unnecessary.

---

## 2. Task architecture / 課題構造

Use a controlled probabilistic environment with latent regimes so that continuous model evidence can be computed or fitted.

Four trial/block types:

- `C0 stable`: latent regime remains stable.
- `C1 outlier`: one large unexpected observation occurs, then the original regime resumes.
- `C2 persistent change`: the latent regime genuinely changes and persists.
- `C3 uncertainty change`: predictive uncertainty increases without one uniquely large prediction error.

Immediate surprise between `C1` and `C2` should be matched or statistically controlled as closely as possible.

An abstract visual/probabilistic environment is preferred for the first human test because the generative structure is known and continuous evidence can be estimated directly. Naturalistic narratives may follow after identifiability is established.

---

## 3. Trial-level participant measures / 試行単位測定

At selected non-time probes, collect:

1. next-event/category prediction
2. prediction confidence
3. current-rule / current-context judgment
4. optional same-context vs new-context judgment

These measures support participant-specific continuous inference estimates rather than relying only on a normative ideal observer.

---

## 4. Continuous predictor set / 連続説明変数

Estimate at minimum:

- posterior probability of regime change
- Bayesian information gain `G_T`
- prediction error
- prediction uncertainty
- raw surprisal
- confidence change
- event-boundary probability/report

Psychological covariates:

- boredom `B_bor`
- engagement `E_eng`
- exploratory/task involvement `X_expl`
- perceived effort `F_eff`
- attention to time `A_time`

These variables form the strongest continuous/known baseline against which `J` must compete.

---

## 5. Candidate independent-J observables / 独立Jの候補観測量

`J` is not defined by posterior threshold crossing.

Candidate evidence must come from another level:

- abrupt categorical interpretation/strategy switch
- persistent context/schema reassignment
- memory separation vs integration
- temporal-order reorganization
- delayed schema persistence
- reproducible hysteresis between forward and reverse transitions
- optional neural representational state transition

Event-boundary reports alone are insufficient because surprise and event segmentation are already known to be related.

---

## 6. Memory and temporal measures / 記憶・時間測定

After each main block:

- temporal-order reconstruction
- event/subevent recall
- context/schema recall
- retrospective duration estimate `Psi_retro`
- passage-of-time judgment recorded separately from numeric duration estimation

Delayed follow-up, if feasible:

- delayed context/schema recall
- delayed temporal-order reconstruction
- persistence of separated vs integrated memory organization

---

## 7. Prospective time must be separated / prospective time の分離

Repeatedly asking about time during the main task would itself increase `A_time` and alter the phenomenon being measured.

Therefore the primary A3 block should not continuously probe subjective time.

Prospective/online time `Psi_pro` should be measured in:

- a separate block, or
- a separate counterbalanced condition with sparse preregistered probes.

This prevents a circular design in which measuring time-monitoring creates time-monitoring.

---

## 8. Competing models / 競合モデル

### M_cont

Continuous inference + psychological covariates.

### M_cont+B

`M_cont` + event-boundary variables.

### M_J

`M_cont+B` + independent latent/observed representational-transition term.

### M_J+R

`M_J` + delayed persistence variables.

Primary requirement:

`M_J` or `M_J+R` must improve held-out prediction of independent representational/memory/temporal observables after complexity control.

Hard environmental prediction is not the target; Experiment A2 already showed that hard switching need not outperform soft Bayesian prediction.

---

## 9. Primary outcomes / 主要アウトカム

Primary outcomes should be preregistered before confirmatory data collection.

Recommended hierarchy:

1. held-out prediction of categorical context/schema organization
2. held-out prediction of temporal-order reconstruction
3. held-out prediction of delayed schema persistence
4. incremental prediction of `Psi_retro` beyond physical duration, event boundaries, and memory strength

`Psi_pro` is secondary because it is strongly affected by time attention and measurement procedure.

---

## 10. Statistical decision structure / 統計判定

Use train/tuning and held-out evaluation or nested cross-validation.

Report:

- held-out log predictive density / log loss
- calibration
- Brier score where applicable
- complexity-aware comparison
- participant-level and sequence-level uncertainty
- jump-timing recovery when a latent transition estimate is used

Do not retain `J` solely because an in-sample fit improves.

---

## 11. Falsification / 反証

### T-F4r

Remove independent temporal-Bridge `J` if:

1. continuous posterior trajectories explain the transition pattern;
2. event-boundary variables explain remaining segmentation;
3. no independent discontinuity/hysteresis remains in representation, memory organization, behavior, temporal order, or persistence;
4. `M_J`/`M_J+R` fail to improve held-out prediction after complexity control.

### Psychological-time reduction

If structural-history variables add no held-out explanatory value for `Psi_retro` beyond physical duration, remembered event boundaries, memory, boredom, engagement, and attention, remove the claimed `Theta -> Psi_retro` contribution.

---

## 12. Sensitivity boundary from synthetic A3 / 合成監査からの制約

Synthetic A3 showed that weak independent-state effects can remain undetected.

Therefore empirical non-detection should be interpreted as evidence against `J` only when:

- measurement reliability is adequate;
- the task has demonstrated sensitivity to a plausible independent effect;
- model recovery succeeds under simulated data matched to the empirical design.

Before confirmatory human inference, perform design-specific parameter recovery using the planned sample size, noise, missingness, and response reliability.

---

## 13. Sample-size policy / サンプルサイズ方針

No universal participant count is fixed at this stage.

Sample size should be chosen only after:

1. a feasibility/pilot estimate of measurement reliability;
2. design-specific synthetic recovery analysis;
3. a preregistered smallest effect of theoretical interest or model-selection target.

Do not choose sample size from the effect magnitude that makes `J` easiest to detect.

---

## 14. Method-development vs confirmatory study / 開発と確認の分離

A single-observer or small feasibility pilot may be used only to test task usability, timing, and data pipeline.

It cannot establish population-level claims.

Confirmatory inference requires an independently powered sample and preregistered analysis.

---

## 15. Literature boundary / 既存研究との境界

Comparison anchors:

- Kumar M, Goldstein A, Michelmann S, et al. Bayesian Surprise Predicts Human Event Segmentation in Story Listening. Cognitive Science. 2023;47(10):e13343. DOI: 10.1111/cogs.13343.
- Nguyen TT, et al. Modeling human activity comprehension at human scale: prediction, segmentation, and categorization. PNAS Nexus. 2024;3(10):pgae459. DOI: 10.1093/pnasnexus/pgae459.
- Boeltzig M, Siestrup S, Bramão I, Schubotz RI. To update or to separate: Neural signatures and consequences of latent cause inference in episodic memory. NeuroImage. 2026;332:121898. DOI: 10.1016/j.neuroimage.2026.121898.
- Liu Z, Johansson M, Bramão I. Episodic events are flexibly encoded in both integrated and separated neural representations. Nature Communications. 2026;17:752. DOI: 10.1038/s41467-026-68473-6.
- Yue WWY, Liu J, Yao Z, et al. Retrospective duration judgments of naturalistic events depend on memories of event boundaries. Psychonomic Bulletin & Review. 2026;33:33. DOI: 10.3758/s13423-025-02833-z.

These findings motivate strong competing explanations. They do not validate temporal-Bridge `J` or `Theta_O`.

---

## 16. Current decision / 現在の判断

The human-level A3 design is justified because:

- A2 rejected hard-jump predictive necessity;
- synthetic A3 showed minimal identifiability of an independent hysteretic residual state;
- psychological-time reintegration now specifies confounds that must be controlled.

The next implementation task is a design-specific simulation/power-and-recovery package for the exact human task before confirmatory participant collection.