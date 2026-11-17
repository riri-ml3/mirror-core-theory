# Temporal Structure — Psychological Time Reintegration v0.2
## Reintegrating early affective-time hypotheses into tau–Theta–Psi separation

> Status: companion specification for `bridge_mirror_x_temporal_structure.md`
> Scope: psychological-time submodel; fixed v0.1 Core is unchanged.

---

## 0. Purpose / 目的

本書は、初期時間論で扱われた「大きくポジティブな心理状態では時間が速く感じられ、大きくネガティブな心理状態では遅く感じられる」という仮説を、現在の `tau_O`, `Theta_O`, `Psi_O` 分離へ再統合する。

初期仮説はそのまま普遍則として保持しない。感情価そのものが直接時間速度を決めるのではなく、感情・覚醒が注意配分、没入、探索、時間監視、記憶構造化へ影響し、それらを介して主観時間と構造的時間へ異なる経路で作用する候補として再定義する。

---

## 1. Time variables / 時間変数

- `tau_O`: physical proper time
- `Theta_O`: observer-relative structural temporal history
- `Psi_pro,O`: prospective / online experienced duration or passage of time
- `Psi_retro,O`: retrospective reconstructed duration

Required separation:

`tau_O != Theta_O != Psi_pro,O != Psi_retro,O`

Passage-of-time judgment and duration estimation are also not assumed to be identical observables.

---

## 2. Psychological state variables / 心理状態変数

To avoid reducing the model to positive/negative valence alone, the following variables are separated:

- `V_aff`: affective valence
- `A_aro`: arousal / activation
- `E_eng`: engagement / absorption
- `X_expl`: exploratory, goal-directed information coupling with the world
- `A_time`: attention directed toward the passage of time
- `B_bor`: boredom / under-engagement
- `F_eff`: perceived effort

These variables are candidate mediators or moderators, not yet universal state variables with fixed coefficients.

---

## 3. Revision of the early valence rule / 初期感情価則の修正

Rejected as a universal law:

`positive -> time always feels fast`

`negative -> time always feels slow`

Retained as a weaker bridge hypothesis:

`affect/arousal -> attentional and engagement state -> experienced time`

and:

`affect/arousal -> exploratory/structural processing -> structural temporal history`

Therefore valence is an upstream variable, not the sole temporal mechanism.

---

## 4. Prospective pathway / 体験中の時間

Candidate pathway:

`V_aff, A_aro, B_bor, F_eff -> E_eng, X_expl, A_time -> Psi_pro,O`

A key hypothesis is that high attention to time may lengthen the experienced passage of time, whereas strong task engagement or absorption may reduce explicit monitoring of time.

Example:

bored waiting:

`B_bor high -> A_time high -> Psi_pro feels slow/long`

engaged research or play:

`E_eng high, X_expl high, A_time low -> Psi_pro may feel fast/short`

This is a candidate psychological pathway, not an identity with `Theta_O`.

---

## 5. Structural pathway / 構造更新経路

Exploration and engagement can also influence information processing:

`E_eng, X_expl -> G_T, C_T, J?, R_T -> Theta_O`

where:

- `G_T`: belief-update magnitude
- `C_T`: structural reconfiguration
- `J?`: optional independent representational jump
- `R_T`: persistence / consolidation variables

Important:

`mental activity != structural learning`

A system may have high cognitive load or repetitive rumination while producing little durable structural reorganization.

Therefore:

`high mental load != high Theta_O`

and:

`high raw information != high Theta_O`

---

## 6. Retrospective pathway / 事後的時間再構成

`Psi_retro,O` is treated as a reconstruction from multiple inputs rather than a direct copy of `tau_O`.

Candidate architecture:

`Psi_retro,O = F(tau_O, event structure, memory, attention, affect, Theta_O, ...)`

The theory does not yet fix a universal scalar function `F`.

The empirical question is whether variables derived from structural-update history provide additional predictive value beyond known predictors such as event-boundary count, remembered subevent number, surprise, and memory strength.

---

## 7. Possible prospective-retrospective dissociation / 前向き・回顧的乖離

A theoretically important configuration is:

`Theta_O high`

while:

`Psi_pro,O feels short/fast`

because attention is absorbed by task processing rather than time monitoring.

Later, the same interval may yield:

`Psi_retro,O feels rich/long`

if many durable event boundaries or structural changes are reconstructable from memory.

This means:

`Theta_O high != Psi_pro,O long`

and potentially:

`Theta_O high -> Psi_retro,O high`

only as an empirical hypothesis to be tested.

---

## 8. Passive vs active / 受け身と攻めの再定義

The everyday contrast 'passive vs active' is too coarse.

A physically passive activity such as watching a film can involve high engagement and strong information coupling, while an overtly active task can remain psychologically disengaged.

The preferred research construct is:

`goal-directed observer-world information coupling`

represented provisionally by `X_expl` together with `E_eng`.

This construct concerns how strongly the observer is engaged in prediction, exploration, interpretation, and model updating, not merely bodily activity.

---

## 9. Rumination / 反芻の重要な対照条件

Rumination can involve high internal activity while repeatedly revisiting similar states.

Possible pattern:

`mental load high`

`G_T low or repetitive`

`C_T approx 0`

`R_T^struct low`

while:

`A_time and negative affect may remain high`

Such a state can therefore produce slow prospective time without implying large structural temporal accumulation.

This is the psychological analogue of the white-noise constraint.

---

## 10. Minimal causal architecture / 最小因果候補

Layer A — Affect:

`(V_aff, A_aro)`

Layer B — Engagement / attention:

`(E_eng, X_expl, A_time, B_bor, F_eff)`

Layer C — Structural update:

`(G_T, C_T, J?, R_T) -> Theta_O`

Layer D — Experienced time:

`Psi_pro,O` and `Psi_retro,O`

Candidate directional structure:

`(V_aff, A_aro) -> (E_eng, X_expl, A_time, B_bor, F_eff)`

`A_time, E_eng, B_bor, F_eff -> Psi_pro,O`

`E_eng, X_expl -> (G_T, C_T, J?, R_T) -> Theta_O`

`(tau_O, Theta_O, event structure, memory, affect, attention) -> Psi_retro,O`

These arrows are research hypotheses, not proven causal laws.

---

## 11. Relation to Experiment A3 / A3との接続

A3 should not use subjective duration alone as evidence for `J`.

For human-level A3, prospective and retrospective time must be modeled separately.

Required controls include:

- continuous posterior belief
- prediction error
- prediction uncertainty
- event-boundary variables
- boredom
- engagement
- attention to time
- memory strength

`J` remains justified only if an independent representational or organizational discontinuity remains after these continuous and known psychological factors are accounted for.

---

## 12. Falsification hooks / 反証条件

### P-F1

If valence alone explains time judgments and the proposed engagement/attention mediators add no reproducible value, the multi-path affect model should be simplified.

### P-F2

If `Theta_O`-derived structural variables add no held-out explanatory value for `Psi_retro,O` or temporal-order memory beyond event boundaries, surprise, memory, and physical duration, the claimed structural-time contribution to retrospective experience should be removed.

### P-F3

If prospective and retrospective timing are empirically indistinguishable under the intended tasks and measures, the present two-output psychological model requires revision.

### P-F4

If repetitive high-load states such as rumination systematically produce the same structural signatures as genuine model reorganization, the current structural-learning variables are insufficiently identified.

---

## 13. Literature anchors / 既存研究との照合

The following works are comparison anchors, not validation of the present theory:

- Moser EI, Kropff E, Moser M-B. The neural bases for timing of durations. Nature Reviews Neuroscience. 2022. PMID: 36097049. Prospective and retrospective timing are treated as computationally distinct.
- Ono F. Retrospective attention: The effects on time perception. Attention, Perception, & Psychophysics. 2024;86:1913–1922. DOI: 10.3758/s13414-024-02918-2.
- Wolff W, Özay-Otgonbayar S, Danckert J, Bieleke M, Martarelli CS. Effort and boredom shape our experience of time. Neuroscience & Biobehavioral Reviews. 2025;178:106375. DOI: 10.1016/j.neubiorev.2025.106375.
- Yue WWY, Liu J, Yao Z, et al. Retrospective duration judgments of naturalistic events depend on memories of event boundaries. Psychonomic Bulletin & Review. 2026;33:33. DOI: 10.3758/s13423-025-02833-z.
- Walker JA, Aswad M, Cousineau D, Lacroix G. How duration, difficulty, and boredom impact prospective and retrospective passage of time judgements and duration estimates. Attention, Perception, & Psychophysics. 2026;88(8). DOI: 10.3758/s13414-026-03366-w.
- Bratzke D. Emotional pictures and time: The effects of arousal and valence on the perception of duration and the subjective passage of time. Attention, Perception, & Psychophysics. 2026;88:98.

These sources support the need to separate affect, boredom/effort, attention, prospective/retrospective timing, and remembered event structure. They do not establish `Theta_O`.

---

## 14. Research status / 現在の研究状態

Retained:

- the early intuition that emotional state and time experience are related
- the distinction between engaged/exploratory states and bored/time-monitoring states
- the possibility that structural history affects retrospective reconstruction

Rejected as too strong:

- universal positive-fast / negative-slow law
- direct identity between structural time and subjective time
- simple equivalence between mental activity and structural learning

Open:

- whether `Theta_O` adds independent predictive value
- whether `J` survives A3 as an independent representational variable
- whether observer-world information coupling can be operationalized robustly

---

## 15. Decision

The early psychological-time model is retained only in this decomposed multi-path form.

The next empirical priority remains A3. New psychological variables should not be added unless they improve identifiability or are required by data.