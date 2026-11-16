# Bridge: Mirror Core × Temporal Structure
## Observer-relative Structural Time, Irreversible Records, and Falsification Program
## v0.2 Draft — B-0 to B-6 Mathematical Foundation Audit

---

## 0. Status / 位置づけ

### English
This document is a Bridge extension of Mirror Core Theory. It does not redefine the fixed v0.1 core primitives `O`, `W`, `M`, `S`, or `J`.

Its purpose is to formalize an observer-relative temporal-structure layer while preserving compatibility with standard physical time. It separates physical proper time, observer structural time, and subjective duration, then defines information-update variables, thermodynamic constraints, hybrid jump dynamics, multi-observer synchronization, and falsification tests.

This document does **not** claim that physical time itself has been derived from information. That stronger hypothesis is reserved as an open research layer.

### 日本語
本書は Mirror Core Theory の Bridge 拡張である。固定された v0.1 Core の原始概念 `O`, `W`, `M`, `S`, `J` を上書きしない。

目的は、既存物理学の時間構造を保持したまま、観測者に固有の「構造的時間」を数理化することである。物理的固有時間、観測者の構造的時間、主観的持続時間を分離し、情報更新、熱力学的制約、ジャンプ、複数観測者同期、反証条件を一つの研究枠組みに整理する。

本書は「物理的時間そのものが情報から導出された」とは主張しない。その強い仮説は未解決の上位研究層として保留する。

---

## 1. Core boundary / Coreとの境界

Core symbols remain unchanged:

- `O`: observer / agent
- `W`: world / externalized object space
- `M`: meaning operator
- `S`: preservation schema
- `J`: jump event

To avoid symbol collision, this bridge denotes the observer's internal predictive model of the world by:

`W_hat_O` = observer `O`'s internal predictive world-model

Thus, `M` is never redefined as an internal predictive model in this bridge.

### 日本語
Core の `M` は意味作用素、`S` は保存スキーマとして固定する。本Bridgeでは、観測者内部の予測的世界モデルを `W_hat_O` と記し、Core記号を再定義しない。

---

## 2. Time-layer separation / 時間層の分離

We distinguish:

- `t`: coordinate time
- `tau_O`: physical proper time along observer O's worldline
- `Theta_O`: dimensionless structural temporal coordinate
- `Psi_O`: subjective duration / experienced time
- `T_G`: stronger open hypothesis that physical time itself emerges from deeper informational relations

The required separation is:

`Theta_O != tau_O != Psi_O`

### 日本語
本Bridgeでは、以下を明確に分離する。

- `t`：座標時間
- `tau_O`：観測者Oの世界線に沿う物理的固有時間
- `Theta_O`：無次元の構造的時間座標
- `Psi_O`：主観的持続時間
- `T_G`：物理時間自体の情報的創発を扱う未証明の上位仮説

したがって、

`Theta_O != tau_O != Psi_O`

である。

`Theta_O` は物理時計の代替ではなく、観測者が通過した構造更新履歴を表す。

---

## 3. Observer state and information update / 観測者状態と情報更新

Observer O is represented by a physical trajectory and an internal information state.

`O_i = (x_i^mu(tau_i), X_i)`

The predictive world-model is:

`W_hat_O = (m_O, theta_O)`

where `m_O` is model structure/class and `theta_O` is a continuous parameter state.

Belief update:

`q_n^- -> q_n^+`

### 3.1 Immediate update variables / 即時更新量

Bayesian update magnitude:

`G_T,n = D_KL(q_n^+ || q_n^-)`

Structural reconfiguration:

`C_T,n = d_W(W_hat_n^-, W_hat_n^+)`

When two model classes cannot be directly compared, a predictive-distribution distance such as Jensen-Shannon divergence is a candidate proxy.

### 3.2 Delayed validation variables / 事後検証量

Predictive consequence:

`P_T,n(Delta) = L_n^- - L_n^+`

Memory persistence:

`R_T,n^mem(Delta)`

Structural persistence:

`R_T,n^struct(Delta)`

These delayed variables must not be used as if they were already known at the instant of update.

### 日本語
即時量と事後量を分離する。特に `P_T` と `R_T` は未来情報を含むため、リアルタイム状態方程式へそのまま代入しない。

---

## 4. White-noise constraint / ホワイトノイズ制約

High Shannon entropy does not imply large structural temporal update.

Required condition:

`H(Y) large !=> Delta Theta_O large`

After the observer has learned that the process is noise, repeated random samples may remain high in raw entropy while:

`G_T -> 0`

`C_T -> 0`

`P_T approx 0`

Therefore the model must distinguish raw data unpredictability from durable model restructuring.

Kolmogorov complexity alone is not sufficient because incompressible random strings can have high algorithmic complexity.

### 日本語
「データ量が大きい」「予測不能である」「観測者の世界モデルが更新された」は同一ではない。ホワイトノイズを大量に記憶するだけで `Theta_O` が大きく進むモデルは棄却する。

---

## 5. Thermodynamic separation / 情報熱力学的分離

The bridge distinguishes:

- `H_bel`: uncertainty of the observer's belief distribution
- `S_th`: thermodynamic/statistical entropy of physical states
- `I(O;W)`: observer-world mutual information
- `Sigma_tot`: total thermodynamic entropy production

A reduction in belief uncertainty:

`Delta H_bel < 0`

does not imply a violation of the second law.

For appropriate classical weak-coupling settings:

`<Sigma_tot> >= 0`

is the relevant average thermodynamic constraint.

Landauer's principle is not interpreted as “every acquired bit necessarily dissipates k_B T ln 2.” It is used only under the physical conditions where logically irreversible operations such as erasure are actually modeled.

Thermodynamic entropy production is a feasibility constraint, not the definition of structural time:

`Delta Theta_O is not proportional to Sigma_tot`

### 日本語
意味ある情報更新量と熱力学的散逸量を同一視しない。発熱量が大きい系が、それだけで大きな構造的時間を生成するとはしない。

---

## 6. Hybrid jump dynamics / ジャンプを含むハイブリッド力学系

The minimal observer state excludes `Theta_O` as a causal physical state variable:

`X_O = (m, theta, q, R)`

Structural time is treated as a path functional:

`Theta_O = F_T[Gamma_O(0:tau)]`

Normal flow:

`X in C : dX/dtau = F(X,Y)`

Candidate jump evidence:

`Lambda_(m->m')(tau) = log[p(m'|D_tau) / p(m|D_tau)]`

Jump set:

`D = { X : max_(m' != m) Lambda_(m->m') >= Lambda_on }`

Jump map:

`X^+ = J_map(X^-, D_tau)`

Hysteresis may be introduced with:

`Lambda_on > Lambda_off`

to prevent one-off noise from generating unstable repeated switching.

The default model preserves continuity of structural time at the jump:

`Theta_O(tau_k^+) = Theta_O(tau_k^-)`

while allowing the post-jump structural accumulation rule to change.

A direct discontinuity in `Theta_O` is retained only as a separate optional hypothesis.

### 日本語
ジャンプとは「情報量が一瞬で巨大化した点」ではなく、蓄積証拠が現在モデルより代替構造を優位にし、内部世界モデル `W_hat_O` が再編される点として扱う。

---

## 7. Multi-observer temporal structure / 複数観測者

Each observer has local quantities:

`(tau_i, Theta_i)`

No condition requires:

`Theta_A = Theta_B`

The shared foundation is the event and causal structure:

`(E, <_causal)`

For a shared event `e`:

`Theta_A <- e -> Theta_B`

is more fundamental than a direct one-valued map `Theta_A -> Theta_B`.

The synchronization relation is:

`R_AB = { (e, Theta_A(e), Theta_B(e)) : e in E_AB }`

A direct synchronization map is only a special case where such a map is well-defined.

### 日本語
共有時間を一つの絶対スカラーとして仮定しない。共有可能なのはまず同一イベントと因果順序であり、各観測者は同じイベントに異なる `Theta` 値を割り当てうる。

---

## 8. Existing-physics consistency audit / 既存物理との整合性監査

Current status:

- Relativity: compatible if `Theta_O` is not used as the cause of proper-time dilation.
- Thermodynamics: compatible if only the appropriate ensemble/average second-law statement is imposed and information entropy is not equated with thermal entropy.
- Quantum theory: classical observer layer is compatible; a genuine quantum extension remains incomplete.
- Subjective time: `Psi_O` must remain distinct from `Theta_O`.
- Physical origin of time: not established.

Zero-extension limit:

When observer-information variables and jumps are removed,

`G_T = C_T = 0`

`J = none`

`Delta Theta_O = 0`

standard physical spacetime, proper time, and causal order remain.

Therefore the current bridge is an **observer-relative temporal-structure theory**, not yet an emergent-physical-time theory.

---

## 9. B-6: Testable quantities / 検証可能量

The central empirical rule is that `Theta_O` is latent and must not be identified directly with subjective duration.

Candidate observables:

1. physical duration `tau`
2. raw input entropy `H(Y)`
3. Bayesian update magnitude `G_T`
4. structural reconfiguration `C_T`
5. inferred jump indicator `J_k`
6. delayed memory persistence `R_T^mem`
7. delayed structural persistence `R_T^struct`
8. predictive consequence `P_T`
9. prospective subjective duration `Psi_pro`
10. retrospective subjective duration `Psi_retro`
11. temporal-order memory
12. event-boundary reports

### Candidate empirical structural-time score

No fixed universal scalar is asserted yet. For model comparison only, an empirical latent score may be fitted:

`Theta_hat_O^(Delta) = sum_n Q_n^(Delta)`

where `Q_n` is estimated from standardized `G_T, C_T, J, R_T` variables.

Weights must be estimated or preregistered; they are not assumed from theory.

---

## 10. Competing models / 競合モデル

The theory must outperform simpler explanations.

- `M0`: physical duration only
- `M1`: raw entropy / information quantity
- `M2`: surprise only
- `M3`: event-boundary count only
- `M4`: structural reconfiguration / jump model
- `M5`: structural reconfiguration + delayed persistence

Support requires out-of-sample improvement of `M4/M5` over the simpler models on preregistered dependent measures.

---

## 11. Distinct predictions / 独自予測候補

### TP1 — White-noise dissociation
High raw entropy without durable model restructuring should not produce the same structural-time effects as structured change.

### TP2 — Surprise vs structural change
Two events matched for immediate surprise should diverge when one is a one-off outlier and the other is a genuine regime change. The regime change should produce larger `C_T`, higher jump probability, and stronger delayed structural effects.

### TP3 — Persistence requirement
Immediate surprise or a boundary report alone should be insufficient. Updates with higher delayed `R_T^struct` should better predict durable temporal organization and retrospective duration effects.

### TP4 — Hybrid threshold / hysteresis
If jumps are real components of the model, a hybrid threshold model should outperform a purely continuous-learning model in appropriate regime-switching tasks. Forward and reverse transitions may exhibit different effective thresholds.

### TP5 — Structural magnitude vs epistemic correctness
A large structural update may occur even when `P_T < 0`. Structural temporal update and predictive correctness are therefore separable.

### TP6 — Prospective/retrospective asymmetry
Because `Theta_O` is defined from structural history, its strongest behavioral relation should be with retrospective temporal reconstruction and temporal-order memory, not necessarily prospective timing.

### TP7 — Multi-observer divergence
Observers exposed to the same physical event sequence but holding different priors may develop different `G_T/C_T/J` histories and therefore different structural-time organization. Communication may reduce model distance without forcing equality of `Theta_A` and `Theta_B`.

---

## 12. Minimal experiments / 最小検証実験

### Experiment A — Outlier vs change-point
Construct sequences containing:
- stable baseline,
- one-off outlier,
- genuine latent regime change.

Match immediate prediction error/surprise as closely as possible between outlier and regime-change trials.

Measure:
- trial-wise predictions and confidence,
- inferred Bayesian surprise,
- event-boundary judgments,
- model-switch evidence,
- immediate retrospective duration,
- temporal-order memory,
- delayed recall after a preregistered interval.

Primary test:
Does structural-change evidence `C_T/J` explain delayed temporal organization beyond surprise alone?

### Experiment B — White noise vs learnable structure
Compare high-entropy noise with a high-entropy sequence containing learnable higher-order structure.

Primary test:
Raw entropy can be high in both, but durable structural effects should track learnable model change rather than entropy alone.

### Experiment C — Hysteresis
Gradually shift evidence from model A to B, then reverse from B to A.

Primary test:
Compare continuous-learning models with hybrid threshold/hysteresis models.

### Experiment D — Multi-observer priors
Manipulate prior knowledge before presenting the same event sequence.

Primary test:
Same physical duration and event sequence should not guarantee identical `G_T/C_T/J` histories or identical retrospective temporal organization.

---

## 13. Falsification hooks / 反証フック

This bridge requires major revision if:

- **T-F1**: high-entropy white noise produces the same durable structural-time effects as structured learnable change after attention and surprise are controlled.
- **T-F2**: `C_T`, jump indicators, and persistence variables provide no reproducible out-of-sample explanatory gain over surprise or event-boundary count.
- **T-F3**: delayed persistence is unrelated to retrospective temporal organization across preregistered tasks.
- **T-F4**: a hybrid jump model consistently fails to outperform continuous models in tasks explicitly designed to contain latent regime changes.
- **T-F5**: prior-model differences do not alter structural-update histories under otherwise identical physical event sequences.
- **T-F6**: the theory requires violations of standard proper-time, causal-order, or thermodynamic constraints to fit data.
- **T-F7**: `Theta_O` cannot be operationalized independently of `Psi_O`, making the proposed separation empirically empty.

A failure of TP1–TP7 may reduce this framework to an integrative description rather than an independent predictive theory.

---

## 14. Novelty boundary / 新規性の境界

The following are not claimed as novel by themselves:

- surprise can trigger event segmentation,
- prediction error can drive memory updating,
- event boundaries can influence retrospective duration judgments,
- change-points and outliers can produce different learning responses.

The candidate contribution of this bridge is narrower:

1. explicit separation of `tau_O`, `Theta_O`, and `Psi_O`;
2. separation of immediate information gain, structural model change, delayed persistence, and epistemic correctness;
3. integration of these variables into a hybrid jump framework;
4. relational multi-observer synchronization through shared events rather than a forced global structural clock;
5. preregisterable tests asking whether structural reconfiguration and persistence explain temporal organization beyond surprise and event-boundary models.

If these additional variables add no predictive value, the framework should be described as an integrative conceptual architecture, not a new empirical time theory.

---

## 15. Interface with Mirror Core / Mirror Coreとの接続

Mirror Core's jump primitive `J` remains unchanged.

This bridge proposes one operational route for a temporal/learning instance of `J`:

`O <-> W -> prediction -> mismatch -> structural evidence accumulation -> J -> new preservation schema S'`

The bridge therefore refines a candidate measurement pathway for jump events without changing the Core definition of `J`.

It also preserves the Core constraint that a valid jump must generate a changed preservation schema rather than merely a new narrative.

---

## 16. Current research status / 現在の研究状態

### Established within this draft
- symbol-layer separation,
- observer-relative structural-time definition,
- information/thermodynamic separation,
- hybrid jump architecture,
- event-based multi-observer relation,
- explicit falsification program.

### Not established
- a universal scalar formula for `Theta_O`,
- a quantum implementation,
- thermodynamic derivation of `Theta_O`,
- emergence of physical proper time from information,
- empirical confirmation of TP1–TP7.

### 日本語
現段階では「時間の本質を解明した完成理論」ではない。B-0〜B-6によって、何を時間として扱い、何を既存物理に委ね、どの変数を測定し、どの条件で理論を棄却するかが明確になった段階である。

---

## 17. Empirical anchors / 既存研究との照合点

Relevant comparison literature includes:

- Bayesian Surprise Predicts Human Event Segmentation in Story Listening — PMID 37867379
- Prediction error and event segmentation in episodic memory — PMID 38184184
- Statistical context dictates the relationship between feedback-related EEG signals and learning — PMID 31433294
- Retrospective duration judgments of naturalistic events depend on memories of event boundaries — PMID 41491329
- Unfolding event structure distorts subjective time — Cognition 267 (2026), 106354, DOI 10.1016/j.cognition.2025.106354
- To update or to separate: Neural signatures and consequences of latent cause inference in episodic memory — PMID 41933851

These studies are comparison anchors, not evidence that the full bridge theory has already been validated.

---

## 18. Summary / 要約

This bridge defines a conservative temporal-structure theory:

`physical proper time tau_O`
→ `observation and belief update`
→ `structural world-model reconfiguration`
→ `persistent records / jump events`
→ `observer-relative structural temporal history Theta_O`

while keeping subjective time `Psi_O` and physical time `tau_O` distinct.

The decisive next step is empirical: determine whether structural reconfiguration and persistence predict temporal organization beyond raw entropy, surprise, and event-boundary count.
