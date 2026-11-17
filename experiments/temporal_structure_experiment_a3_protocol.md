# Temporal Structure Experiment A3 — Protocol
## Independent Structural Jump Test Beyond Continuous Belief Updating

> Status: preregistration-oriented protocol draft
> Purpose: test whether temporal-structure jump J has independent representational evidence beyond continuous posterior belief, surprise, and event-boundary reports.

## 1. Why A3 is needed / なぜA3が必要か

Experiment A showed that immediate surprise and persistent structural evidence can be computationally separated.

Experiment A2 then produced a negative result for the stronger predictive claim:

hard jump predictive superiority = NOT SUPPORTED

Soft Bayesian model averaging outperformed the tuned hard-jump model on held-out predictive log score.

Therefore A3 must not attempt to tune a hard threshold until it wins.

The next question is narrower:

Does a discrete or hysteretic representational transition remain observable after continuous posterior belief, prediction error, prediction uncertainty, and event-boundary variables are modeled?

If not, the independent jump variable J should be removed from this temporal-structure Bridge.

## 2. Primary hypothesis / 主仮説

H_A3:

After controlling for continuous posterior belief and continuous prediction-quality signals, at least one independent observable shows a reproducible transition associated with structural reorganization.

Candidate observables:

- event-boundary report
- categorical strategy/model report
- representational separation
- temporal-order reorganization
- delayed schema persistence
- retrospective duration reconstruction
- optional neural state-space transition

Null / competing hypothesis:

All apparent jumps are adequately explained by continuous trajectories of posterior model probability, Bayesian surprise, prediction error, prediction uncertainty, and event-boundary probability, with no additional discrete latent state.

## 3. Literature boundary / 既存研究との境界

Existing literature already supports several weaker effects:

1. Bayesian surprise can predict human event segmentation better than simple surprisal.
2. Prediction error and prediction uncertainty can support partially distinct event-boundary mechanisms.
3. Latent-cause inference can reorganize episodic representations by updating an existing trace or separating a new trace.
4. Retrospective duration judgments depend on remembered event structure and subevent boundaries.
5. Event-internal structure can bias subjective duration.

Therefore event boundaries, surprise, representational change, or duration distortion alone are not sufficient evidence for the present theory.

The required contribution is:

independent structural discontinuity beyond continuous/known mechanisms

## 4. Minimal task architecture / 最小課題

Use sequences generated from latent regimes.

C0 — stable: no structural change.

C1 — one-off outlier: a large transient deviation occurs, then the original regime resumes.

C2 — persistent latent change: a genuine regime transition occurs and persists.

C3 — uncertainty transition: prediction uncertainty increases without a large single prediction error.

Immediate surprise between C1 and C2 should be matched or statistically controlled where possible.

## 5. Continuous predictors / 連続モデル側

For each time step estimate:

- posterior probability of regime change
- Bayesian information gain G_T(t)
- prediction error
- prediction uncertainty
- raw surprisal
- event-boundary probability

These define the strongest continuous baseline.

## 6. Candidate independent-J model / 独立Jモデル

Add a latent structural state Z_J(t).

State transitions may be discrete or hysteretic, but the J model is not allowed to replace the continuous posterior predictors. It must explain residual structure beyond them.

Candidate form:

P(Z_J(t) != Z_J(t-1)) = h(evidence_t, history_t)

with explicit regularization against unnecessary switching.

## 7. Primary model comparison / 主要比較

M_cont: continuous predictors only.

M_cont+B: continuous predictors plus event-boundary variables.

M_J: continuous predictors plus independent latent jump state.

M_J+R: M_J plus delayed persistence variables.

Central criterion:

Does M_J or M_J+R improve held-out prediction of independent representational or temporal observables beyond M_cont and M_cont+B?

Predictive superiority of hard thresholding over soft Bayesian prediction is no longer the validation target.

## 8. Primary dependent measures / 従属変数

Behavioral minimum:

1. event-boundary judgment
2. categorical interpretation / strategy choice
3. temporal-order memory
4. retrospective duration estimate
5. delayed schema/model recall

Optional stronger measures:

6. representational similarity change
7. neural state-space transition
8. eye-movement or action-policy switch

## 9. Critical dissociations / 決定的分離

Dissociation A — Outlier vs regime change

Match immediate surprise. C1 may produce high surprise without persistent structural separation; C2 should produce stronger delayed representational separation if J has independent value.

Dissociation B — Prediction vs representation

Continuous posterior belief may change smoothly. A valid independent J requires another observable to show discontinuity or hysteresis not reducible to the smooth posterior trajectory.

Dissociation C — Structure vs epistemic correctness

A large structural transition may occur even when later predictive consequence is negative.

jump magnitude != predictive correctness

## 10. Falsification rule / 反証条件

T-F4r:

Remove the independent jump variable J from the temporal-structure model if, across appropriately designed tasks:

1. continuous posterior-belief trajectories explain apparent transitions;
2. event-boundary variables explain the remaining segmentation effects;
3. no reproducible independent discontinuity appears in representation, memory organization, behavior, temporal-order reconstruction, or delayed persistence;
4. adding J does not improve held-out prediction after complexity penalty or cross-validation.

This is a theory-reduction rule, not a parameter-tuning target.

## 11. Theta criterion / Theta_O の扱い

A3 does not directly validate Theta_O.

Theta_O remains latent. A3 tests only whether the proposed ingredients for structural temporal history have independent explanatory value.

A future empirical structural-time score should be estimated only if structural variables and delayed persistence replicate, held-out explanatory gain exists, and Theta_O remains operationally distinct from subjective time Psi_O.

## 12. Analysis principles / 解析原則

- preregister dependent measures and exclusion criteria
- separate tuning and held-out test data
- retain negative results
- compare against continuous baselines
- use complexity-aware model comparison
- report calibration and predictive performance
- do not infer physical-time emergence from behavioral results
- do not infer consciousness-specific quantum collapse

## 13. Current decision / 現時点の判断

A3 is warranted because A2 eliminated one overly strong justification for J.

The theory should now survive only if J corresponds to an independent representational or organizational transition.

If A3 fails under adequate power and well-identified tasks, the parsimonious action is to remove independent J from this temporal Bridge and retain continuous structural updating only.

## 14. Literature anchors

- Kumar M, Goldstein A, Michelmann S, et al. Bayesian Surprise Predicts Human Event Segmentation in Story Listening. Cognitive Science. 2023;47(10):e13343. DOI: 10.1111/cogs.13343.
- Nolden S, Turan G, Güler B, Günseli E. Prediction error and event segmentation in episodic memory. Neuroscience & Biobehavioral Reviews. 2024;157:105533. DOI: 10.1016/j.neubiorev.2024.105533.
- Nguyen TT, et al. Modeling human activity comprehension at human scale: prediction, segmentation, and categorization. PNAS Nexus. 2024;3(10):pgae459. DOI: 10.1093/pnasnexus/pgae459.
- Boeltzig M, Siestrup S, Bramão I, Schubotz RI. To update or to separate: Neural signatures and consequences of latent cause inference in episodic memory. NeuroImage. 2026;332:121898. DOI: 10.1016/j.neuroimage.2026.121898.
- Yue WWY, Liu J, Yao Z, et al. Retrospective duration judgments of naturalistic events depend on memories of event boundaries. Psychonomic Bulletin & Review. 2026;33(1):33. DOI: 10.3758/s13423-025-02833-z.
- Wen C, Yousif SR, Sherman BE. Unfolding event structure distorts subjective time. Cognition. 2026;267:106354. DOI: 10.1016/j.cognition.2025.106354.

---

## 15. Synthetic identifiability status / 合成識別監査

The protocol has now passed a minimal synthetic sanity check documented in:

- `experiments/temporal_structure_experiment_a3_identifiability.py`
- `experiments/temporal_structure_experiment_a3_identifiability.md`

Under the baseline synthetic configuration, the candidate-J model was not supported in 12/12 Null-world replications and was supported in 12/12 imposed True-J replications.

Weak imposed J effects remained difficult to recover. Therefore empirical non-detection can count against J only when measurement sensitivity is independently adequate.

This result authorizes progression to human-level A3 design; it does not validate human J.