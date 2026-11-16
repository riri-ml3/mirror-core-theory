# Synthetic Experiment A — Outlier vs Change-Point
## Temporal Structure Bridge / v0.2 Draft

---

## 0. Status

### English
This is a **synthetic model-identifiability experiment**. It tests whether the current temporal-structure formalization can computationally distinguish an isolated surprising event from a persistent structural regime change when the initial observation is identical.

It is **not** human validation of `Theta_O`, and it is **not** evidence that physical time emerges from information.

### 日本語
本実験は、**合成データによるモデル識別可能性の確認**である。初期観測を完全に一致させたうえで、単発外れ値と持続的構造変化を、現行の時間構造モデルが計算上分離できるかを検査する。

本実験は人間における `Theta_O` の実証ではなく、物理時間が情報から創発することの証拠でもない。

---

## 1. Research question / 研究問い

Can two sequences with identical initial surprise and identical immediate Bayesian information gain later diverge in structural evidence?

`same initial surprise + same G`

but

`outlier -> no persistent structural change`

`change-point -> persistent structural change / jump evidence`

If this separation fails even in a minimal synthetic setting, TP2 of the Temporal Structure Bridge is not computationally viable.

---

## 2. Minimal generative setup / 最小生成モデル

Observation variance:

`sigma^2 = 1`

Initial event for both conditions:

`y_1 = 3.5`

Outlier condition:

`y_t ~ Normal(0,1), t >= 2`

Change-point condition:

`y_t ~ Normal(2,1), t >= 2`

The same Gaussian noise realization is paired across the two conditions after adding the change mean in the change-point condition.

Candidate models:

- `M0`: stationary mean fixed at 0
- `M1`: persistent post-event mean `mu`, with prior `mu ~ Normal(0,4)`

Prior probability of `M1`:

`P(M1) = 0.05`

Jump threshold:

`P(M1 | D_t) >= 0.95`

Confirmation rule:

the threshold must be exceeded for two consecutive steps.

---

## 3. Matched initial quantities / 初期量の一致

Because both conditions use exactly the same first observation:

`surprise_1(outlier) = surprise_1(change) = 7.0439385 nat`

and:

`G_1(outlier) = G_1(change) = 1.3847190 nat`

The posterior after the first event is also identical:

`mu_post = 2.8`

`var_post = 0.8`

Thus any later divergence cannot be attributed to different first-event surprise or first-event Bayesian update magnitude.

---

## 4. Baseline simulation / 基準シミュレーション

Parameters:

- replications per condition: 5000
- horizon: 20 observations
- seed: 42
- event value: 3.5
- change mean: 2.0
- jump threshold: 0.95
- confirmation: 2 consecutive threshold crossings

### Results

| Metric | Outlier | Change-point |
|---|---:|---:|
| Jump detection rate | 0.0094 | 1.0000 |
| Median detected step | 3 | 3 |
| Mean predictive structural distance `C_pred` over all trials | 0.0244 | 3.0788 |
| Median final structural evidence | 0.0088 | 1.0000 |
| Median held-out predictive gain among detected trials | -1.2800 | +1.9042 |
| Mean `P(change)` after first event | 0.7597 | 0.7597 |
| Mean final `P(change)` | 0.0265 | ~1.0000 |

### 日本語解釈
最初の一発だけを見た時点では、両条件は完全に同じである。ところが後続観測を取り込むと、

- 単発外れ値では構造変化の事後確率が消退する
- 真のchange-pointでは構造変化の事後確率がほぼ1へ収束する

という分岐が生じた。

したがって、この最小モデルでは、

`G != structural persistence`

を計算上分離できる。

---

## 5. Confirmation-rule test / 閾値確認規則

One-step threshold crossing:

- outlier false-jump rate: 0.0318
- change-point detection rate: 1.0000

Two-consecutive-step confirmation:

- outlier false-jump rate: 0.0094
- change-point detection rate: 1.0000

Thus, in this configuration, requiring persistence across two observations reduced false jumps by roughly 70% without reducing detection of the strong change-point condition.

This supports the usefulness of a persistence/hysteresis-like rule in the current minimal model.

It does **not** establish that two steps or the threshold 0.95 are universal values.

---

## 6. Robustness sweep / 感度監査

The following parameters were varied:

- event value: 3.0, 3.5, 4.0
- persistent change mean: 1.0, 1.5, 2.0
- prior change probability: 0.01, 0.05, 0.10
- jump threshold: 0.90, 0.95, 0.99

Total cells:

`3 x 3 x 3 x 3 = 81`

Replications per cell:

`800`

Across the 81 cells:

- median false-positive rate: 0.00375
- median true-positive rate: 0.99875
- minimum true-positive rate: 0.565
- maximum false-positive rate: 0.18

### Important failure regions / 重要な失敗領域

The model is **not universally robust**.

Low-amplitude changes (`change mean = 1.0`) combined with a very skeptical prior and a high threshold can produce low sensitivity. For example:

`event=3.0, change=1.0, prior=0.01, threshold=0.99 -> TPR=0.565, FPR=0`

Conversely, a very large isolated event combined with a permissive prior and low threshold can produce false jumps. For example:

`event=4.0, prior=0.10, threshold=0.90 -> FPR=0.18`

Therefore the jump rule is not a parameter-free law. Thresholds, priors, and expected effect size materially control performance.

---

## 7. What was demonstrated / 示されたこと

This synthetic experiment supports only the following limited claims:

1. Identical initial surprise and identical `G` can later lead to different persistent structural evidence.
2. A one-off outlier and a persistent change-point are computationally separable in the current minimal Bayesian model.
3. Requiring persistence across more than one observation can reduce false structural jumps.
4. `G`, jump evidence, structural predictive distance, and delayed predictive consequence need not collapse to one scalar.

These are **model-architecture results**, not empirical claims about human cognition.

---

## 8. What was not demonstrated / 示されていないこと

The simulation does not establish:

- that human cognition literally performs this Bayesian model comparison;
- that `Theta_O` is a biological state variable;
- that the chosen `C_pred` is the unique or correct measure of structural reconfiguration;
- that the threshold 0.95 or two-step confirmation is universal;
- that subjective duration `Psi_O` follows the simulated variable;
- that the hybrid model outperforms existing event-segmentation or latent-cause models on human data;
- that physical proper time emerges from information.

---

## 9. Relation to existing research / 既存研究との境界

The experiment deliberately builds on an already established distinction: surprising outcomes should be learned from differently depending on whether they indicate a true environmental change or an uninformative outlier. Nassar, Bruckner, and Frank (2019) experimentally dissociated surprise from learning demand in changepoint versus oddball contexts.

Bayesian surprise has also been shown to predict human event segmentation in naturalistic story listening, while simple surprisal did not show the same relation (Kumar et al., 2023).

Recent work further distinguishes updating an existing memory representation from inferring a new latent cause, with different representational consequences (Boeltzig et al., 2026).

Retrospective duration judgments of complex naturalistic events have been shown to depend strongly on remembered event structure and boundaries (Yue et al., 2026).

Therefore the candidate contribution of the Temporal Structure Bridge is **not** the claim that surprise, change-points, latent causes, or event boundaries are novel. The testable extension is whether structural reconfiguration and delayed persistence add explanatory value for temporal organization beyond those existing variables.

---

## 10. Reproducibility / 再現性

Implementation:

`experiments/temporal_structure_experiment_a.py`

Default run:

`python experiments/temporal_structure_experiment_a.py`

Optional JSON output:

`python experiments/temporal_structure_experiment_a.py --output experiment_a_results.json`

The script uses only the Python standard library.

---

## 11. Decision / 現時点の判定

### Pass condition for this stage
The immediate-surprise variable and persistent structural-change variables must be computationally separable.

### Result
`PASS — under the specified minimal generative model`

### Qualification
The result is parameter-sensitive and does not yet validate the psychological or temporal interpretation.

The next required test is stronger:

**compare a continuous-learning model against the hybrid jump model using the same synthetic datasets and then move to preregisterable human-observable predictions only if the hybrid model has an identifiable predictive advantage.**

---

## References / 参考文献

- Nassar MR, Bruckner R, Frank MJ. Statistical context dictates the relationship between feedback-related EEG signals and learning. eLife. 2019;8:e46975. PMID: 31433294. DOI: 10.7554/eLife.46975.
- Kumar M, Goldstein A, Michelmann S, Zacks JM, Hasson U, Norman KA. Bayesian Surprise Predicts Human Event Segmentation in Story Listening. Cognitive Science. 2023;47(10):e13343. PMID: 37867379. DOI: 10.1111/cogs.13343.
- Yue WWY, Liu J, Yao Z, et al. Retrospective duration judgments of naturalistic events depend on memories of event boundaries. Psychonomic Bulletin & Review. 2026;33:33. PMID: 41491329. DOI: 10.3758/s13423-025-02833-z.
- Boeltzig M, Siestrup S, Bramão I, Schubotz RI. To update or to separate: Neural signatures and consequences of latent cause inference in episodic memory. NeuroImage. 2026;332:121898. PMID: 41933851. DOI: 10.1016/j.neuroimage.2026.121898.
