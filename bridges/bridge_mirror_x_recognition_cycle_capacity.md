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
- the U-transition map audit has been completed at Bridge level,
- the next required step is a minimal dynamic model that respects the Transition Contract v0.1.

### 日本語

現段階の研究判定は以下である。

- 5変数平坦モデルは理論モデルとして棄却する。
- 一般化平均族は感度分析ツールとして保持する。
- `p = -1` は参照候補に留める。
- `F_rec` は創発的な操作的循環容量として再定義する。
- `L_log` と `K_conn` をU状態変数から分離する。
- `U_∞` を各再基盤化周期の必須段階として課さない。
- Absolute-0 / 0↔100 に関する主張を数値シミュレーションの外部に保持する。
- U-transition map audit はBridgeレベルで完了した。
- 次工程は Transition Contract v0.1 を守る最小動的モデルの設計とする。

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


---

## 14. U-Transition Map Audit / U遷移マップ監査

### English

The transition-map audit distinguishes fixed relations from working hypotheses.

| Relation | Status | Contract |
|---|---|---|
| `U_1^W → R_O → U_{1,O}^{(n)}` | retained existing definition | world-side conditions require observer-specific internalization |
| foundation stability → higher-order U2 probability | retained existing prediction | stability may increase probability; it does not guarantee U2 |
| `U_2^{(n)} → B_O → U_{1,O}^{(n+1)}` | retained existing definition | matured U2 may be rebaselined |
| `B_O → K_O` | retained existing definition | rebaselining may jointly produce stability and rigidity |
| irreversible/unresolved difference → `Q` | Bridge hypothesis | candidate input relation only |
| `Q → U2` | conditional hypothesis | requires a gate; no universal direct causation |
| `L_log →` transition efficiency | working modifier hypothesis | exact edge unresolved |
| `K_conn →` semantic integration/persistence | working modifier hypothesis | exact edge unresolved |
| `U2 → U∞` | not mandatory | must not be imposed in every cycle |
| `U∞ → next U1` | unresolved | not part of the minimal cycle |
| `F_rec` as an independent state node | rejected | treat as derived cycle-capacity measure |

The minimal causal skeleton is therefore:

`foundation + unresolved difference → gated higher-order response → rebaselining → next foundation`

This is a Bridge-level causal candidate, not an established empirical law.

### 日本語

U-transition Map Audit では、既存定義で固定できる関係と、作業仮説を分離する。

| 関係 | 状態 | 契約 |
|---|---|---|
| `U_1^W → R_O → U_{1,O}^{(n)}` | 既存定義を維持 | 世界側条件は観測者固有の内在化を必要とする |
| 基盤安定性 → 高次U2活動確率 | 既存予測を維持 | 安定は確率を高めうるがU2を保証しない |
| `U_2^{(n)} → B_O → U_{1,O}^{(n+1)}` | 既存定義を維持 | 成熟したU2は再基盤化されうる |
| `B_O → K_O` | 既存定義を維持 | 再基盤化は安定と硬直を同時に生みうる |
| 不可逆／未解決差分 → `Q` | Bridge仮説 | 入力関係候補に留める |
| `Q → U2` | 条件付き仮説 | ゲートを必要とし、普遍的直接因果としない |
| `L_log →` 遷移効率 | 作業修飾仮説 | 正確な作用点は未確定 |
| `K_conn →` 意味統合／保持 | 作業修飾仮説 | 正確な作用点は未確定 |
| `U2 → U∞` | 必須ではない | 各周期の必須遷移として課さない |
| `U∞ → next U1` | 未確定 | 最小循環には含めない |
| `F_rec` を独立状態ノードとする | 棄却 | 循環容量から導出される派生量として扱う |

したがって最小因果骨格は、

`基盤 + 未解決差分 → ゲート付き高次反応 → 再基盤化 → 次周期基盤`

である。

これはBridgeレベルの因果候補であり、確立された経験法則ではない。

---

## 15. Transition Contract v0.1 / 遷移契約 v0.1

### 15.1 Contract classes / 契約クラス

### English

Each variable must belong to one of four operational classes:

1. **Input**: introduces external or unresolved difference into the cycle.
2. **Gate**: determines whether higher-order processing can become active.
3. **Modifier**: changes transition quality or efficiency without being the transition target itself.
4. **Output / retained structure**: becomes a candidate for rebaselining or downstream measurement.

No variable may change class merely to improve simulation fit.

### 日本語

各変数は、以下の4つの操作クラスのいずれかに属さなければならない。

1. **Input**：外部情報または未解決差分を循環へ入力する。
2. **Gate**：高次処理が前景化できるかを条件付ける。
3. **Modifier**：遷移対象そのものではなく、遷移の質または効率を修飾する。
4. **Output / retained structure**：再基盤化または下流測定の候補となる。

シミュレーション適合性を改善する目的だけで、変数のクラスを変更してはならない。

### 15.2 Input contract / 入力契約

### English

Candidate inputs are:

- `Δ_unres`: unresolved difference or mismatch,
- `R_nr`: non-recoverability / irreversibility weighting candidate,
- `P_info`: external information pressure,
- context variables not yet formalized.

A provisional problem-salience variable may be written only as a placeholder:

`Q = Φ(Δ_unres, R_nr, context)`

The function `Φ` is not yet specified.

`R_nr` must not be interpreted as "more irreversible = more meaningful."  
It is only a candidate weight on unresolved difference.

### 日本語

入力候補は以下である。

- `Δ_unres`：未解決差分または不一致
- `R_nr`：非回収可能性／不可逆性の重み候補
- `P_info`：外部情報圧
- 未定式化の文脈変数

問題顕著性の暫定表現は、プレースホルダとしてのみ、

`Q = Φ(Δ_unres, R_nr, context)`

と置く。

関数 `Φ` はまだ定義しない。

`R_nr` を「不可逆性が高いほど意味が大きい」と解釈してはならない。  
未解決差分へ作用する候補重みに留める。

### 15.3 Gate contract / ゲート契約

### English

Higher-order U2 activity must not be modeled as a direct function of `Q` alone.

Use an abstract gate:

`G_U2 = Gate(Q, U_{1,O}^{(n)}, Threat, Context)`

with at least two possible qualitative outcomes:

- **exploration-permitting**: higher-order U2 activity can become salient,
- **preservation-dominant**: threat or foundation instability suppresses higher-order exploration.

No numerical form is fixed in v0.1.

### 日本語

高次U2活動を `Q` 単独の直接関数としてモデル化してはならない。

抽象ゲートとして、

`G_U2 = Gate(Q, U_{1,O}^{(n)}, Threat, Context)`

を置く。

少なくとも以下の二つの質的出力を許す。

- **exploration-permitting**：高次U2活動が前景化しうる。
- **preservation-dominant**：脅威または基盤不安定性により、高次探索が抑制される。

v0.1では具体的数式を固定しない。

### 15.4 U2 contract / U2契約

### English

`U_2^{(n)}` remains a higher-order layer/structure, not a scalar synonym for curiosity or problem salience.

For simulation, a scalar `u2_activity` may be introduced only as an operational proxy for activity within U2.

Therefore:

`Q ≠ U_2`

and

`u2_activity ≠ U_2^{(n)}`

ontologically.

### 日本語

`U_2^{(n)}` は高次層／構造であり、好奇心や問題顕著性の単純なスカラー同義語ではない。

シミュレーションでは、U2内部の活動を表す操作proxyとしてのみ `u2_activity` を導入できる。

したがって存在論的には、

`Q ≠ U_2`

かつ

`u2_activity ≠ U_2^{(n)}`

である。

### 15.5 Modifier contract: `L_log`
### 修飾契約：`L_log`

### English

`L_log` is provisionally assigned to **structural processing**, not U2 activation.

Working role:

- organize relations,
- detect contradictions,
- represent causal structure,
- improve structural coherence of candidate schemas.

The safest first placement is downstream of U2 activation and upstream of rebaselining:

`U2 activity → [L_log] → structured candidate → B_O`

This edge remains a working hypothesis.

### 日本語

`L_log` は暫定的に **構造処理** に割り当て、U2発火変数とはしない。

作業上の役割は、

- 関係の配置
- 矛盾検出
- 因果構造の表現
- 候補スキーマの構造整合性向上

である。

第一配置として最も安全なのは、U2活動の後、再基盤化の前である。

`U2 activity → [L_log] → structured candidate → B_O`

ただし、この矢印は作業仮説に留める。

### 15.6 Modifier contract: `K_conn`
### 修飾契約：`K_conn`

### English

`K_conn` is provisionally assigned to **semantic/self-relevant connectivity**, not hedonic preference strength.

Possible roles include:

- connecting incoming or processed information to an existing self-related network,
- increasing retention of self-relevant structures,
- supporting semantic integration before rebaselining.

For the first dynamic model, use only one placement to avoid over-parameterization:

`structured candidate → [K_conn] → semantically integrated candidate → B_O`

Input-selection effects of `K_conn` remain a later hypothesis.

### 日本語

`K_conn` は暫定的に **意味的・自己関連的接続性** に割り当て、快楽的嗜好強度とはしない。

候補役割は、

- 入力済み／処理済み情報を既存の自己関連ネットワークへ接続する
- 自己関連構造の保持を高める
- 再基盤化前の意味統合を支える

ことである。

最初の動的モデルでは過剰パラメータ化を避けるため、作用位置を一つに限定する。

`structured candidate → [K_conn] → semantically integrated candidate → B_O`

`K_conn` の入力選択作用は後続仮説として保留する。

### 15.7 Rebaselining contract / 再基盤化契約

### English

The existing definition remains authoritative:

`B_O(U_2^{(n)}) = (U_{1,O}^{(n+1)}, K_O^{(n+1)})`

For a simulation, the input to `B_O` may be an operationally filtered candidate derived from U2 activity, but this must not redefine `B_O` at the theoretical level.

The simulation must preserve the dual output:

- next-cycle foundation,
- possible rigidity.

### 日本語

既存定義を優先する。

`B_O(U_2^{(n)}) = (U_{1,O}^{(n+1)}, K_O^{(n+1)})`

シミュレーションでは、U2活動から操作的に抽出された候補を `B_O` の入力proxyとして用いてよいが、理論レベルの `B_O` 定義を変更してはならない。

また、以下の二重出力を保持する。

- 次周期基盤
- 硬直化可能性

### 15.8 U∞ contract / U∞契約

### English

`U_∞` is excluded from the mandatory minimal transition cycle.

It may later represent higher-order integration accumulated across cycles, but v0.1 does not define:

- an activation threshold,
- a transition equation,
- a required path from U2 to U∞,
- a required path from U∞ to the next U1.

### 日本語

`U_∞` を最小遷移循環の必須ノードから除外する。

将来的に複数周期にまたがる高次統合を表す可能性はあるが、v0.1では以下を定義しない。

- 発動閾値
- 遷移方程式
- U2からU∞への必須経路
- U∞から次周期U1への必須経路

### 15.9 `F_rec` contract / `F_rec`契約

### English

`F_rec` is a derived cycle-capacity measure, not a causal node.

The preferred model class after this audit is:

> flow/capacity constrained by bottlenecks

rather than a flat average.

A future minimal model may define transition efficiencies `T_i` and derive:

`F_rec = Capacity(T_input, T_gate, T_structure, T_connect, T_rebase)`

but no aggregation law is fixed in v0.1.

### 日本語

`F_rec` は因果ノードではなく、循環容量から導出される派生量である。

本監査後の第一候補は、

> ボトルネック制約を受ける flow/capacity 型

であり、平坦平均モデルではない。

将来の最小モデルでは遷移効率 `T_i` を導入し、

`F_rec = Capacity(T_input, T_gate, T_structure, T_connect, T_rebase)`

のように導出できる可能性がある。

ただしv0.1では集約則を固定しない。

---

## 16. Minimal Dynamic Model Requirements / 最小動的モデル要件

### English

The next simulation must satisfy all of the following:

1. preserve the existing `B_O` definition,
2. keep U∞ outside the mandatory cycle,
3. distinguish `Q`, `u2_activity`, `L_log`, and `K_conn`,
4. include a preservation-dominant branch when threat/foundation instability is high,
5. derive `F_rec` from transition performance rather than assign it exogenously,
6. retain rigidity `K_O` as a possible cost of successful rebaselining,
7. keep Absolute-0 / 0↔100 outside the numerical state space,
8. declare all new numerical functions as simulation hypotheses, not Core definitions.

### 日本語

次のシミュレーションは、以下をすべて満たさなければならない。

1. 既存の `B_O` 定義を維持する。
2. U∞を必須循環の外に置く。
3. `Q`, `u2_activity`, `L_log`, `K_conn` を区別する。
4. 脅威または基盤不安定性が高い場合の保存優位分岐を含める。
5. `F_rec` を外生的に与えず、遷移性能から導出する。
6. 成功した再基盤化にも硬直度 `K_O` というコストが生じうる構造を保持する。
7. Absolute-0 / 0↔100 を数値状態空間の外に保持する。
8. 新しい数値関数はすべてシミュレーション仮説とし、Core定義としない。


---

## 17. Model Form Audit v0.1 / 数式形監査 v0.1

### 17.1 Audit result / 監査結果

**PASS WITH REVISIONS**

The candidate one-cycle model is structurally usable, but four revisions are required before it should be treated as the minimal dynamic-model baseline.

1. remove theoretical dependence on `eps_num` and handle zero-capacity states explicitly,
2. prevent double counting of `P_info`,
3. interpret multiplicative flow only through explicit stage-transfer efficiencies and preserve residual flows,
4. do not fix the scalar aggregation law for `F_rec` until the processing architecture is specified.

### 日本語

**条件付きPASS（修正必須）**

一周期モデル候補は構造的には利用可能であるが、最小動的モデルの基準形とする前に以下の4修正を必要とする。

1. 理論式から `eps_num` 依存を外し、容量0を明示的に処理する。
2. `P_info` の二重計上を避ける。
3. 積型フローは明示的な段階通過効率に限定し、各段階の残差を保存する。
4. 処理アーキテクチャを確定するまで `F_rec` の単一集約則を固定しない。

---

### 17.2 Problem-salience function `Q`

The exponential candidate

`Q = 1 - (1 - Δ_unres)^(1 + β_R R_nr)`

satisfies the intended boundary and monotonicity conditions for `β_R ≥ 0`:

- `Δ_unres = 0 → Q = 0`,
- `Δ_unres = 1 → Q = 1`,
- increasing `R_nr` cannot create salience when `Δ_unres = 0`,
- `Q` increases monotonically with unresolved difference and non-recoverability.

However, the exponent has no established theoretical interpretation and may saturate rapidly.

For the minimal baseline, a simpler bounded interaction family is preferred:

`Q = Δ_unres + β_R R_nr Δ_unres (1 - Δ_unres)`

with

`0 ≤ β_R ≤ 1`.

This form preserves:

- `Q(0,R_nr)=0`,
- `Q(1,R_nr)=1`,
- `Q(Δ,0)=Δ`,
- monotonicity in `Δ_unres` and `R_nr`,
- boundedness `0 ≤ Q ≤ 1`.

It also makes the role of `R_nr` explicit: it amplifies an already existing unresolved difference, rather than generating difference by itself.

This remains a simulation hypothesis, not a theoretical definition of meaning.

### 日本語

指数型候補

`Q = 1 - (1 - Δ_unres)^(1 + β_R R_nr)`

は、`β_R ≥ 0` の範囲で意図した境界条件と単調性を満たす。

- `Δ_unres = 0 → Q = 0`
- `Δ_unres = 1 → Q = 1`
- `Δ_unres = 0` のとき `R_nr` 単独では顕著性を生成しない
- 未解決差分と非回収可能性が増えると `Q` は単調増加する

ただし、指数そのものに確立した理論的意味がなく、パラメータによっては飽和が速い。

最小基準形では、より単純な有界相互作用族を優先候補とする。

`Q = Δ_unres + β_R R_nr Δ_unres (1 - Δ_unres)`

ただし、

`0 ≤ β_R ≤ 1`

とする。

この形は、

- `Q(0,R_nr)=0`
- `Q(1,R_nr)=1`
- `Q(Δ,0)=Δ`
- `Δ_unres` と `R_nr` に対する単調性
- `0 ≤ Q ≤ 1`

を保持する。

また、`R_nr` は差分そのものを生成せず、既に存在する未解決差分を増幅する候補因子として明示できる。

これは意味の理論定義ではなく、シミュレーション仮説である。

---

### 17.3 Availability gate / 利用可能性ゲート

The candidate logistic form is retained provisionally:

`G_avail = sigmoid(κ(f_n - θ_F - λ_T Threat_n))`

with:

- `κ > 0`,
- `λ_T ≥ 0`.

The name is revised from "U2 gate" to **availability gate**.

Higher-order activity is represented as:

`X_U2 = Q · G_avail`

This separates:

- salience amplitude `Q`,
- availability to process that salience `G_avail`.

Therefore, low `Q` does not require a separate hard threshold, and a high `Q` does not guarantee high U2 activity when the foundation is unstable or threat is high.

The preservation-side residual at this gate is:

`R_gate = Q(1 - G_avail)`.

### 日本語

ロジスティック候補は暫定的に維持する。

`G_avail = sigmoid(κ(f_n - θ_F - λ_T Threat_n))`

ただし、

- `κ > 0`
- `λ_T ≥ 0`

とする。

名称は「U2ゲート」ではなく、**利用可能性ゲート**とする。

高次活動proxyは、

`X_U2 = Q · G_avail`

とする。

これにより、

- 顕著性の大きさ `Q`
- その顕著性を処理可能な状態 `G_avail`

を分離する。

したがって、`Q` が小さい場合に別のハード閾値を必須とせず、逆に `Q` が高くても基盤不安定または高脅威ならU2活動は高くならない。

ゲート段階で保存側へ残る量は、

`R_gate = Q(1 - G_avail)`

とする。

---

### 17.4 Information-pressure double counting / 情報圧の二重計上

The previous candidate placed `P_info` in both:

1. `T_info = 1/(1 + γP_info)`, and
2. `E_load = P_info/F_rec` while `F_rec` already contained `T_info`.

This creates a structural double-counting risk.

The revised ordering is:

1. derive **pre-load cycle capacity** `C_pre` from stage conditions that do not contain `P_info`,
2. compute effective load from `P_info` relative to `C_pre`,
3. derive `T_info` from that effective load.

Provisional ordering:

`C_pre = Capacity(G_avail, T_L, T_K, T_R)`

`E_load = Load(P_info, C_pre)`

`T_info = 1/(1 + γE_load)`

where `T_L`, `T_K`, and `T_R` are transfer-efficiency proxies defined below.

`P_info` is therefore introduced only once into the load path.

### 日本語

旧候補では `P_info` が、

1. `T_info = 1/(1 + γP_info)`
2. `T_info` を含む `F_rec` に対する `E_load = P_info/F_rec`

の両方に入っており、構造的な二重計上の危険がある。

改訂順序は以下とする。

1. `P_info` を含まない段階条件から **負荷前循環容量** `C_pre` を導出する。
2. `P_info` を `C_pre` に対する実効負荷へ変換する。
3. その実効負荷から `T_info` を導出する。

暫定順序は、

`C_pre = Capacity(G_avail, T_L, T_K, T_R)`

`E_load = Load(P_info, C_pre)`

`T_info = 1/(1 + γE_load)`

である。

ここで `T_L`, `T_K`, `T_R` は後述する段階通過効率proxyである。

これにより、`P_info` は負荷経路へ一度だけ導入される。

---

### 17.5 Zero-capacity contract / 容量0契約

The theoretical model should not define:

`E_load = P_info/(C_pre + eps_num)`

because `eps_num` is an implementation device and its value would artificially determine the magnitude of load near zero capacity.

Instead, define the operational load relation piecewise:

- if `P_info = 0`: `E_load = 0` as a model convention of zero external demand,
- if `P_info > 0` and `C_pre > 0`: `E_load = P_info/C_pre`,
- if `P_info > 0` and `C_pre = 0`: `E_load = +∞` in the extended operational model.

Numerical code may use a machine guard, but the guard is not part of the theoretical equation and has no relation to Absolute-0.

### 日本語

理論モデルでは、

`E_load = P_info/(C_pre + eps_num)`

を定義式としない。

`eps_num` は実装上の装置であり、容量0近傍の負荷量が任意の `eps_num` に依存してしまうためである。

代わりに操作的負荷関係を場合分けする。

- `P_info = 0` の場合：外部要求0というモデル上の規約として `E_load = 0`
- `P_info > 0` かつ `C_pre > 0` の場合：`E_load = P_info/C_pre`
- `P_info > 0` かつ `C_pre = 0` の場合：拡張操作モデル上で `E_load = +∞`

数値コードでは機械的ガードを用いてよいが、それは理論式の一部ではなく、Absolute-0とも関係しない。

---

### 17.6 Stage-transfer contract and flow conservation
### 段階通過契約とフロー保存

The multiplicative form is justified only if each factor is explicitly interpreted as the fraction of the same flow that passes a stage.

Therefore raw `L_log`, `K_conn`, and `K_O` must first be mapped to transfer efficiencies:

`T_L = ψ_L(L_log)`

`T_K = ψ_K(K_conn)`

`T_R = ψ_R(K_O)`

The identity proxies

`T_L=L_log`, `T_K=K_conn`, `T_R=1-K_O`

may be used only as first simulation hypotheses.

The flow is then:

`X_0 = Q`

`X_1 = X_0 G_avail`

`X_2 = X_1 T_info`

`X_3 = X_2 T_L`

`X_4 = X_3 T_K`

`Y_rebase = X_4 T_R`

with residuals:

`R_gate = X_0-X_1`

`R_info = X_1-X_2`

`R_L = X_2-X_3`

`R_K = X_3-X_4`

`R_rebase = X_4-Y_rebase`.

This gives the conservation identity:

`Q = Y_rebase + R_gate + R_info + R_L + R_K + R_rebase`.

The residuals are not interpreted yet. They may later represent unresolved material, preservation-side routing, unintegrated information, or next-cycle carryover, but those meanings require separate audit.

### 日本語

積型は、各因子が「同一情報流のうち、その段階を通過する割合」である場合にのみ正当化する。

したがって、生の `L_log`, `K_conn`, `K_O` は、まず段階通過効率へ写像する必要がある。

`T_L = ψ_L(L_log)`

`T_K = ψ_K(K_conn)`

`T_R = ψ_R(K_O)`

最初のシミュレーション仮説としてのみ、

`T_L=L_log`

`T_K=K_conn`

`T_R=1-K_O`

という恒等proxyを使用してよい。

その場合のフローは、

`X_0 = Q`

`X_1 = X_0 G_avail`

`X_2 = X_1 T_info`

`X_3 = X_2 T_L`

`X_4 = X_3 T_K`

`Y_rebase = X_4 T_R`

となる。

各段階の残差を、

`R_gate = X_0-X_1`

`R_info = X_1-X_2`

`R_L = X_2-X_3`

`R_K = X_3-X_4`

`R_rebase = X_4-Y_rebase`

と定義すると、

`Q = Y_rebase + R_gate + R_info + R_L + R_K + R_rebase`

というフロー保存恒等式が成立する。

残差の意味はまだ固定しない。将来的に未解決情報、保存側への分岐、未統合情報、次周期への持越し等として扱う可能性があるが、別監査を必要とする。

---

### 17.7 Capacity aggregation audit / 容量集約監査

The harmonic mean is **not rejected**, but it is not fixed as the definition of `F_rec`.

Different aggregators correspond to different processing architectures:

- `min(T_i)`: strict bottleneck / pipeline-capacity interpretation,
- harmonic mean: additive stage-time / serial-rate interpretation,
- geometric mean: multiplicative central-tendency interpretation,
- product `ΠT_i`: end-to-end retained-flow fraction.

These quantities are not interchangeable.

Therefore, until the architecture is specified, use a diagnostic capacity family:

`C_min = min(T_i)`

`C_H = HarmonicMean(T_i)`

`C_G = GeometricMean(T_i)`

and separately:

`R_cycle = ΠT_i`.

The first audit sweep found that the qualitative directions of the revised model were preserved under `C_min`, `C_H`, and `C_G`, while their absolute magnitudes differed.

Thus the current evidence supports the **flow/capacity family**, not a unique scalar aggregation law.

### 日本語

調和平均そのものは棄却しないが、`F_rec` の定義として固定しない。

集約則は異なる処理アーキテクチャを意味する。

- `min(T_i)`：厳密なボトルネック／パイプライン容量
- 調和平均：段階時間が加算される直列処理率
- 幾何平均：乗法的中心傾向
- 積 `ΠT_i`：端から端まで保持されたフロー割合

これらは同一ではない。

したがってアーキテクチャ確定前は、診断用容量族として、

`C_min = min(T_i)`

`C_H = HarmonicMean(T_i)`

`C_G = GeometricMean(T_i)`

を併記し、別に、

`R_cycle = ΠT_i`

を保持する。

第一回監査走査では、`C_min`, `C_H`, `C_G` のいずれでも改訂モデルの質的方向は維持されたが、絶対値は異なった。

したがって現在支持されるのは単一集約則ではなく、**flow/capacity 型モデル族**である。

---

### 17.8 Monotonicity and conservation audit / 単調性・保存監査

Using normalized variables on `[0,1]` and the revised bounded `Q` candidate, grid tests confirmed the intended qualitative directions for all three provisional capacity aggregators (`min`, harmonic, geometric):

- `Δ_unres ↑ → Q ↑`,
- `R_nr ↑ → Q ↑`,
- `foundation stability ↑ → Y_rebase ↑`,
- `Threat ↑ → Y_rebase ↓`,
- `L_log ↑ → Y_rebase ↑`,
- `K_conn ↑ → Y_rebase ↑`,
- `K_O ↑ → Y_rebase ↓`,
- `P_info ↑ → Y_rebase ↓`.

The staged formulation also satisfied the flow-conservation identity to numerical precision.

These are internal-consistency checks only. They do not validate the model empirically.

### 日本語

正規化変数を `[0,1]` に置き、改訂した有界 `Q` 候補を用いたグリッド試験では、3つの暫定容量集約（minimum、調和平均、幾何平均）のすべてで意図した質的方向が維持された。

- `Δ_unres ↑ → Q ↑`
- `R_nr ↑ → Q ↑`
- 基盤安定性↑ → `Y_rebase ↑`
- `Threat ↑ → Y_rebase ↓`
- `L_log ↑ → Y_rebase ↑`
- `K_conn ↑ → Y_rebase ↑`
- `K_O ↑ → Y_rebase ↓`
- `P_info ↑ → Y_rebase ↓`

また段階フロー形式は、数値精度の範囲でフロー保存恒等式を満たした。

これらは内部整合性試験であり、経験的妥当性を示すものではない。

---

### 17.9 Revised baseline after audit / 監査後の基準形

The safest current baseline is:

`Q = Δ_unres + β_R R_nr Δ_unres(1-Δ_unres)`

`G_avail = sigmoid(κ(f_n - θ_F - λ_T Threat_n))`

`C_pre ∈ {C_min, C_H, C_G}` during architecture audit

`E_load = Load(P_info,C_pre)`

`T_info = 1/(1+γE_load)`

`T_L = ψ_L(L_log)`

`T_K = ψ_K(K_conn)`

`T_R = ψ_R(K_O)`

followed by the conserved staged flow from `X_0=Q` to `Y_rebase`.

No single scalar `F_rec` aggregation is fixed yet.

### 日本語

現時点で最も安全な基準形は以下である。

`Q = Δ_unres + β_R R_nr Δ_unres(1-Δ_unres)`

`G_avail = sigmoid(κ(f_n - θ_F - λ_T Threat_n))`

アーキテクチャ監査中の `C_pre` は、

`C_pre ∈ {C_min, C_H, C_G}`

とする。

`E_load = Load(P_info,C_pre)`

`T_info = 1/(1+γE_load)`

`T_L = ψ_L(L_log)`

`T_K = ψ_K(K_conn)`

`T_R = ψ_R(K_O)`

とし、`X_0=Q` から `Y_rebase` までの保存型段階フローを用いる。

単一スカラーの `F_rec` 集約則はまだ固定しない。
