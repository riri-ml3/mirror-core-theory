# Bridge: Mirror Core × Recognition Cycle Capacity
## U-Structure Type Audit, Information Load, and Simulation Design
## v0.2 Draft

---

## 0. Status / 位置づけ

### English

This document is a Bridge-level research draft for Mirror Core Theory.

It does **not** redefine the Core primitives `O`, `W`, `M`, `S`, or `J`, and it does not modify the definitions fixed in `bridge_mirror_x_u_foundation.md`.

Its purpose is to:
1. audit the variable types used in the provisional recognition-capacity simulation,
2. separate U-structure states from processing/connectivity modifiers,
3. define a safer operational meaning for recognition-cycle capacity,
4. preserve a clear boundary between the observable/operational model and Absolute-0 / 0↔100 hypotheses,
5. specify the next simulation and falsification requirements.

### 日本語

本書は、Mirror Core Theory の Bridge レベル研究ドラフトである。

Core の原始概念 `O`, `W`, `M`, `S`, `J` を再定義せず、`bridge_mirror_x_u_foundation.md` で固定された定義も変更しない。

本書の目的は以下である。

1. 暫定的な認識容量シミュレーションで用いた変数型を監査する。
2. U構造の状態・機能的位置と、処理能力／接続性を表す修飾変数を分離する。
3. 認識循環容量の操作的意味を安全に定義する。
4. 観測可能・操作可能なモデルと Absolute-0 / 0↔100 仮説の境界を維持する。
5. 次段階のシミュレーションと反証条件を明示する。

---

## 1. Boundary Contract / 境界契約

### English

This bridge is restricted to the manifest-relative operational domain.

The normalized numerical interval `[0,1]` used in simulations is only a computational scale.

Therefore:

- numerical `0` is not Absolute-0,
- numerical `1` is not Absolute-1,
- `F_rec → 0` does not mean approach to Absolute-0,
- `F_rec → 1` does not mean arrival at `100`,
- the regularization constant `eps_num` has no ontological meaning.

The working hypothesis that `0` and `100` are non-manifest foundational representations is not tested by this simulation.

### 日本語

本Bridgeは、顕現・相対的な操作領域のみに限定する。

シミュレーションで用いる正規化区間 `[0,1]` は、計算上の尺度にすぎない。

したがって、

- 数値上の `0` は Absolute-0 ではない。
- 数値上の `1` は Absolute-1 ではない。
- `F_rec → 0` は Absolute-0 への接近を意味しない。
- `F_rec → 1` は `100` への到達を意味しない。
- 正則化定数 `eps_num` に存在論的意味を与えない。

`0` と `100` を非顕現基盤の表現として扱う作業仮説は、本シミュレーションの検証対象ではない。

---

## 2. Compatibility with the Existing U-Foundation Bridge
## 既存U-Foundation Bridgeとの整合性

### English

The existing U-foundation bridge formally distinguishes:

- `U_1^W`: world-side foundational conditions,
- `U_{1,O}^{(n)}`: observer-internalized foundation,
- `U_2^{(n)}`: higher-order psychological, symbolic, social, learning, meaning, and self-establishment structures,
- `B_O`: rebaselining operator,
- `U_{1,O}^{(n+1)}`: next-cycle foundation,
- `U_∞`: higher-order integrative direction in the spiral.

This document preserves that structure.

In particular, it does **not** impose the mandatory per-cycle sequence:

`U1 → U2 → U∞ → U1'`

Instead, the minimal rebaselining contract remains:

`U_{1,O}^{(n)} → U_2^{(n)} → B_O → U_{1,O}^{(n+1)}`

with `U_∞` retained as a higher-order integrative layer/direction whose exact activation conditions remain unresolved.

### 日本語

既存のU-Foundation Bridgeでは、以下が正式に区別されている。

- `U_1^W`：世界側基盤条件
- `U_{1,O}^{(n)}`：観測者内在化基盤
- `U_2^{(n)}`：心理・記号・社会・学習・意味・自己確立を含む高次構造
- `B_O`：再基盤化作用
- `U_{1,O}^{(n+1)}`：次周期基盤
- `U_∞`：スパイラル上の高次統合方向

本書はこの構造を維持する。

特に、各周期に

`U1 → U2 → U∞ → U1'`

という必須系列を新たに課さない。

最小の再基盤化契約は、

`U_{1,O}^{(n)} → U_2^{(n)} → B_O → U_{1,O}^{(n+1)}`

のままとし、`U_∞` は高次統合層／方向として保持する。U∞の正確な発動条件は未確定である。

---

## 3. Type Audit / 変数型監査

### English

The provisional Simulation 1 treated the following five quantities as peers:

`G(U1, U2, U∞, L, K)`

This is computationally convenient but theoretically unsafe.

The audit separates them as follows.

| Variable | Provisional type | Role |
|---|---|---|
| `u1_state` | state/foundation proxy | operational proxy for current observer foundation |
| `u2_state` | higher-order activity proxy | operational proxy for higher-order exploratory/meaning activity |
| `uinf_state` | integration proxy | provisional proxy only; activation conditions unresolved |
| `L_log` | processing modifier | structural/logical organization capacity |
| `K_conn` | connectivity modifier | semantic/self-relevant information connectivity |
| `P_info` | exogenous pressure | normalized information pressure |
| `Q` | input/salience candidate | unresolved-difference or problem-salience candidate |
| `F_rec` | emergent operational capacity | capacity of the observer-side cycle to process and re-stabilize information |
| `E_load` | derived load index | effective load under information pressure |
| `D_del` | downstream indicator | model-internal delegation/transition tendency |

`L_log` and `K_conn` are therefore not treated as additional U-states.

### 日本語

暫定 Simulation 1 では、以下の5量を同列に扱っていた。

`G(U1, U2, U∞, L, K)`

これは計算上は便利であるが、理論的には型混同を含む。

監査後は以下のように分離する。

| 変数 | 暫定型 | 役割 |
|---|---|---|
| `u1_state` | 状態／基盤proxy | 現在の観測者基盤の操作的代理 |
| `u2_state` | 高次活動proxy | 探索・意味形成等の高次活動の操作的代理 |
| `uinf_state` | 統合proxy | 暫定代理。発動条件は未確定 |
| `L_log` | 処理修飾変数 | 情報の論理的・構造的配置能力 |
| `K_conn` | 接続修飾変数 | 情報を意味的・自己関連的に接続する能力 |
| `P_info` | 外生圧力 | 正規化された情報圧 |
| `Q` | 入力／顕著性候補 | 未解決差分・問題顕著性の候補 |
| `F_rec` | 創発的操作容量 | 情報を処理し再安定化する観測者側循環の容量 |
| `E_load` | 派生負荷指標 | 情報圧下の実効負荷 |
| `D_del` | 下流指標 | モデル内部の委譲／遷移傾向 |

したがって、`L_log` と `K_conn` を追加のU状態として扱わない。

---

## 4. Rejection of the Flat Five-Variable Model
## 5変数平坦モデルの棄却

### English

The following equation is rejected as a theoretical model:

`F_rec = G(U1, U2, U∞, L_log, K_conn)`

Reason: it averages functional U-positions/states together with processing and connectivity modifiers.

The equation may be retained only as a historical sensitivity-test baseline.

### 日本語

以下の式は、理論モデルとしては棄却する。

`F_rec = G(U1, U2, U∞, L_log, K_conn)`

理由は、U構造上の機能的位置／状態と、処理・接続を修飾する変数を同一型として平均しているためである。

この式は、過去の感度分析ベースラインとしてのみ保存可能である。

---

## 5. Revised Operational Definition of `F_rec`
## `F_rec` の改訂操作定義

### English

`F_rec` is not defined as an arithmetic or generalized average of psychological capacities.

Working definition:

> `F_rec` is the operational capacity of the observer-side system to preserve a usable foundation, process higher-order information, and re-stabilize a preservation schema under information pressure.

This definition is intentionally functional rather than ontological.

A provisional decomposition is:

`U_base = G_p(u1_state, u2_state[, uinf_state])`

`F_rec = H(U_base; L_log, K_conn, T)`

where:

- `G_p` is a generalized-mean family used only for sensitivity analysis,
- inclusion of `uinf_state` is optional until U∞ activation is operationally defined,
- `H` is not yet fixed,
- `T` denotes transition-efficiency terms to be defined only after a transition-map audit.

### 日本語

`F_rec` を心理的能力の算術平均または一般化平均そのものとして定義しない。

作業定義は次の通りである。

> `F_rec` は、情報圧下において、観測者側システムが利用可能な基盤を保存し、高次情報を処理し、保存スキーマを再安定化するための操作的機能容量である。

これは存在論的定義ではなく、意図的に機能的・操作的定義とする。

暫定分解は次の通りである。

`U_base = G_p(u1_state, u2_state[, uinf_state])`

`F_rec = H(U_base; L_log, K_conn, T)`

ここで、

- `G_p` は感度分析に限定した一般化平均族である。
- `uinf_state` は、U∞発動が操作的に定義されるまで任意項とする。
- `H` は未固定である。
- `T` は遷移効率項であり、transition-map監査後にのみ定義する。

---

## 6. Generalized-Mean Sensitivity Result
## 一般化平均の感度分析結果

### English

For positive normalized components `x_i`, the provisional family is:

`G_p(x) = (Σ w_i x_i^p)^(1/p)`

with the geometric-mean limit at `p = 0`.

The first robustness sweep showed:

- `p = 1` permits strong compensation of a severely degraded component,
- `p = 0` still permits substantial compensation,
- negative `p` increasingly penalizes local severe weakness,
- `p = -1` is a useful reference candidate, not an established truth.

Example sensitivity states:

- all-high: `[0.8,0.8,0.8,0.8,0.8]`
- one-low: `[0.2,0.8,0.8,0.8,0.8]`
- one-extreme: `[0.05,0.95,0.95,0.95,0.95]`
- all-mid: `[0.5,0.5,0.5,0.5,0.5]`

Selected results:

| `p` | all-high | one-low | one-extreme | all-mid |
|---:|---:|---:|---:|---:|
| 1 | 0.800 | 0.680 | 0.770 | 0.500 |
| 0 | 0.800 | 0.606 | 0.527 | 0.500 |
| -0.5 | 0.800 | 0.556 | 0.340 | 0.500 |
| -1 | 0.800 | 0.500 | 0.207 | 0.500 |
| -2 | 0.800 | 0.400 | 0.111 | 0.500 |

These values do not validate a psychological law. They only expose the compensability assumptions encoded by `p`.

### 日本語

正の正規化成分 `x_i` に対する暫定一般化平均族を、

`G_p(x) = (Σ w_i x_i^p)^(1/p)`

とする。なお `p = 0` は幾何平均の極限として扱う。

第一回頑健性走査では以下が確認された。

- `p = 1` は、単一要素の深刻な低下を他要素が強く補償する。
- `p = 0` でも相当程度の補償が残る。
- 負の `p` は、局所的な重度低下をより強く反映する。
- `p = -1` は有力な参照候補であるが、真理値として固定しない。

例として用いた状態は以下である。

- all-high: `[0.8,0.8,0.8,0.8,0.8]`
- one-low: `[0.2,0.8,0.8,0.8,0.8]`
- one-extreme: `[0.05,0.95,0.95,0.95,0.95]`
- all-mid: `[0.5,0.5,0.5,0.5,0.5]`

主要結果は以下である。

| `p` | all-high | one-low | one-extreme | all-mid |
|---:|---:|---:|---:|---:|
| 1 | 0.800 | 0.680 | 0.770 | 0.500 |
| 0 | 0.800 | 0.606 | 0.527 | 0.500 |
| -0.5 | 0.800 | 0.556 | 0.340 | 0.500 |
| -1 | 0.800 | 0.500 | 0.207 | 0.500 |
| -2 | 0.800 | 0.400 | 0.111 | 0.500 |

これらの値は心理法則を実証するものではない。パラメータ `p` が暗黙に置く「要素間の補償可能性」を可視化した結果である。

---

## 7. Information Pressure and Effective Load
## 情報圧と実効負荷

### English

The provisional effective-load equation is retained:

`E_load = P_info / (F_rec + eps_num)`

where:

- `P_info` is normalized information pressure,
- `F_rec` is operational recognition-cycle capacity,
- `eps_num > 0` is a numerical regularizer only.

A downstream transition indicator may be written:

`D_del = sigmoid(alpha * (E_load - theta_del))`

For `alpha > 0`, the 50% transition point satisfies:

`P_info,50 = theta_del * (F_rec + eps_num)`

Therefore:

- `theta_del` controls the transition location,
- `alpha` controls transition steepness,
- state ranking under fixed `P_info`, `alpha`, and `theta_del` is inherited monotonically from `F_rec`.

`D_del` must not be interpreted as an empirically calibrated probability unless calibration data are introduced.

### 日本語

暫定的な実効負荷式は維持する。

`E_load = P_info / (F_rec + eps_num)`

ここで、

- `P_info` は正規化された情報圧、
- `F_rec` は操作的な認識循環容量、
- `eps_num > 0` は数値計算上の正則化項にすぎない。

下流の遷移指標候補として、

`D_del = sigmoid(alpha * (E_load - theta_del))`

を置くことができる。

`alpha > 0` のとき、50%転移点は、

`P_info,50 = theta_del * (F_rec + eps_num)`

を満たす。

したがって、

- `theta_del` は転移位置を制御する。
- `alpha` は転移の急峻さを制御する。
- `P_info`, `alpha`, `theta_del` を固定した状態間順位は、`F_rec` の順位を単調に継承する。

実測データによる校正を行わない限り、`D_del` を実際の委譲確率として解釈してはならない。

---

## 8. Candidate Roles of Logical Structure and Semantic Connectivity
## 論理構造化と意味接続性の候補役割

### English

The present bridge distinguishes two candidate modifiers.

### `L_log`: logical/structural organization

Working interpretation:
the capacity to organize relations, contradictions, causal structure, and consistency among information.

It may modify processing or rebaselining efficiency, but the exact causal edge is not fixed.

### `K_conn`: semantic/self-relevant connectivity

Working interpretation:
the degree or capacity by which incoming information can be meaningfully connected to an existing self-related information network.

It is **not** defined as preference strength or hedonic liking.

This distinction preserves the research hypothesis "liking ≈ understanding/connectivity" without equating it with simple positive affect.

### 日本語

本Bridgeでは、二つの修飾変数候補を区別する。

### `L_log`：論理的・構造的配置能力

作業解釈：
情報間の関係、矛盾、因果、整合性を構造的に配置する能力である。

処理効率または再基盤化効率を修飾する可能性があるが、正確な因果矢印はまだ固定しない。

### `K_conn`：意味的・自己関連的接続性

作業解釈：
新規情報を既存の自己関連情報ネットワークへ意味的に接続できる度合いまたは能力である。

これは単なる嗜好強度や快楽的な「好き」の強さではない。

この区別により、「好き ≈ わかる／接続できる」という研究仮説を、単純な正感情と同一視せず保持する。

---

## 9. Irreversible Difference Interface
## 不可逆差分インターフェース

### English

A separate candidate bridge concerns irreversible difference.

Provisional chain:

`fixed history → unresolved difference → Q → higher-order response`

where `Q` is a problem-salience candidate.

This document does not assert:

`irreversibility → U2`

as a universal causal law.

The response may depend on foundation stability, threat intensity, context, and other variables. Under severe threat, preservation-dominant responses may occur instead of higher-order exploration.

Therefore, irreversible difference remains an input-side Bridge hypothesis, not a Core axiom.

### 日本語

別の候補Bridgeとして、不可逆差分を扱う。

暫定系列は、

`固定された履歴 → 未解決差分 → Q → 高次反応`

である。

ここで `Q` は問題顕著性の候補変数である。

本書では、

`不可逆性 → U2`

を普遍的因果法則としては主張しない。

反応は、基盤安定性、脅威強度、文脈、その他の変数に依存しうる。強い脅威下では、高次探索より保存優位反応が生じる可能性がある。

したがって不可逆差分は、Core公理ではなく入力側Bridge仮説として保持する。

---

## 10. Next Audit: U-Transition Map
## 次監査：U-Transition Map

### English

Before introducing additional simulation parameters, the following causal edges must be audited separately:

1. whether `Q` predicts higher-order exploratory activity,
2. whether `L_log` modifies information integration, rebaselining, or both,
3. whether `K_conn` modifies information selection, semantic integration, persistence, or multiple stages,
4. whether `U_∞` can be operationalized without forcing it into every U-cycle,
5. whether `F_rec` is better represented by a bottleneck, flow/capacity, or dynamical-state model.

No new edge should be treated as established merely because it improves simulation behavior.

### 日本語

新たなシミュレーション変数を追加する前に、以下の因果矢印を個別に監査する必要がある。

1. `Q` が高次探索活動を予測するか。
2. `L_log` が情報統合、再基盤化、またはその両方を修飾するか。
3. `K_conn` が情報選択、意味統合、持続性、または複数段階を修飾するか。
4. `U_∞` を各U周期の必須通過点にせず操作化できるか。
5. `F_rec` は bottleneck、flow/capacity、dynamical-state のいずれで表現するのが妥当か。

シミュレーション挙動が改善するという理由だけで、新しい因果矢印を確立事項として扱ってはならない。

---

## 11. Falsification and Revision Hooks
## 反証・改訂フック

### English

This bridge requires revision if:

- **RC1**: treating `L_log` and `K_conn` as modifiers is empirically inferior to treating them as U-states under a well-defined measurement model.
- **RC2**: `F_rec` cannot be operationalized independently of Absolute-0/100 assumptions.
- **RC3**: generalized-mean sensitivity conclusions disappear under reasonable rescaling or measurement definitions.
- **RC4**: no stable relation exists between operational cycle capacity and effective information load.
- **RC5**: `K_conn` cannot be distinguished from simple preference/positive affect.
- **RC6**: `L_log` has no measurable relation to structural integration or rebaselining.
- **RC7**: the proposed transition-map decomposition adds no predictive or explanatory value over the flat model.

### 日本語

以下が成立する場合、本Bridgeは改訂を要する。

- **RC1**：明確な測定モデルの下で、`L_log` と `K_conn` を修飾変数として扱うよりU状態として扱う方が経験的に優れる場合。
- **RC2**：`F_rec` を Absolute-0/100 仮説から独立して操作化できない場合。
- **RC3**：一般化平均の感度分析結果が、妥当な再尺度化や測定定義によって消失する場合。
- **RC4**：操作的循環容量と実効情報負荷の間に安定した関係が存在しない場合。
- **RC5**：`K_conn` を単純な嗜好・正感情から区別できない場合。
- **RC6**：`L_log` が構造統合または再基盤化と測定可能な関係を持たない場合。
- **RC7**：transition-map分解が平坦モデルに対して予測力・説明力を追加しない場合。

---

## 12. Current Status / 現在の判定

### English

Current research status:

- the flat five-variable model is rejected as a theoretical model,
- the generalized-mean family is retained as a sensitivity-analysis tool,
- `p = -1` is a reference candidate only,
- `F_rec` is redefined as emergent operational cycle capacity,
- `L_log` and `K_conn` are separated from U-state variables,
- `U_∞` is not imposed as a mandatory stage in every rebaselining cycle,
- Absolute-0 / 0↔100 claims remain outside the numerical simulation,
- the next required step is a U-transition map audit before further model expansion.

### 日本語

現段階の研究判定は以下である。

- 5変数平坦モデルは理論モデルとして棄却する。
- 一般化平均族は感度分析ツールとして保持する。
- `p = -1` は参照候補に留める。
- `F_rec` は創発的な操作的循環容量として再定義する。
- `L_log` と `K_conn` をU状態変数から分離する。
- `U_∞` を各再基盤化周期の必須段階として課さない。
- Absolute-0 / 0↔100 に関する主張を数値シミュレーションの外部に保持する。
- 次工程はモデル拡張ではなく U-transition map audit とする。

---

## 13. Relation to Core / Coreとの最終境界

### English

This document is a Bridge and simulation-design draft.

It does not alter:

- Mirror Effect `O ↔ W`,
- Meaning Operator `M`,
- Preservation Schema `S`,
- Jump `J`,
- the Core falsification hooks,
- the existing U-foundation definitions.

Any future promotion of these propositions into Core requires independent theoretical and empirical justification.

### 日本語

本書はBridgeおよびシミュレーション設計ドラフトである。

以下を変更しない。

- ミラー効果 `O ↔ W`
- 意味作用素 `M`
- 保存スキーマ `S`
- ジャンプ `J`
- Coreの反証フック
- 既存U-Foundation Bridgeの定義

本書の命題を将来Coreへ昇格させる場合には、独立した理論的・経験的根拠を必要とする。
