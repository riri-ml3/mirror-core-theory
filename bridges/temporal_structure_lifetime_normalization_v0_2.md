# Temporal Structure — Lifetime Normalization v0.2
## Lifetime-normalized coordinate Lambda_O

> Status: companion specification for `bridge_mirror_x_temporal_structure.md`
> Scope: life-course normalization only; fixed v0.1 Core is unchanged.

---

## 0. Purpose / 目的

本書は、初期時間論で扱われてきた「20年生きた観測者と80年生きた観測者も、それぞれ自身の生涯全体を100%とすれば同じ位置構造として扱える」という直感を、物理時間・構造的時間・主観時間と混同しない形で定式化する。

この主張は `20 years = 80 years` を意味しない。等しいのは、生涯全体に対する無次元の相対的位置である。

---

## 1. Physical lifetime / 物理的生涯長

Observer O has birth proper time `tau_b,O` and terminal proper time `tau_d,O`.

`L_O = tau_d,O - tau_b,O`

`L_O` is a physical duration measured along the observer's worldline.

For two observers A and B:

`L_A != L_B`

may hold even when both lifetimes are complete.

---

## 2. Lifetime-normalized coordinate / 生涯正規化座標

Define:

`Lambda_O(tau) = (tau - tau_b,O) / (tau_d,O - tau_b,O)`

with:

`0 <= Lambda_O <= 1`

and endpoint conditions:

`Lambda_O(tau_b,O) = 0`

`Lambda_O(tau_d,O) = 1`

Therefore a 20-year lifetime and an 80-year lifetime are not equal in physical duration, but both map to the same normalized interval:

`[tau_b,A, tau_d,A] -> [0,1]`

`[tau_b,B, tau_d,B] -> [0,1]`

### 日本語

20年と80年が同じなのではない。出生から死亡までの有限区間を各観測者自身の全生涯で正規化したとき、両者が同じ `[0,1]` 形式へ写像できるという意味である。

---

## 3. Equality claim / 「同じ」の厳密な意味

For observer A with a 20-year lifetime:

`Lambda_A(10 years after birth) = 0.5`

For observer B with an 80-year lifetime:

`Lambda_B(40 years after birth) = 0.5`

The equality:

`Lambda_A = Lambda_B = 0.5`

means equal relative life-course position, not equal physical age, biological state, experience amount, information content, or structural history.

---

## 4. Four-way temporal separation / 四層分離

The temporal variables are explicitly separated:

- `tau_O`: physical proper time
- `Lambda_O`: normalized lifetime position
- `Theta_O`: observer-relative structural temporal history
- `Psi_O`: subjective experienced time

Required distinction:

`tau_O != Lambda_O != Theta_O != Psi_O`

`Lambda_O` is a normalized coordinate derived from physical lifetime endpoints. It is not itself a physical clock and not an information-processing measure.

---

## 5. Ex-post character / 事後座標としての性質

The denominator contains `tau_d,O`, the terminal time.

During life, the observer normally does not know the true terminal time.

Therefore the exact value of `Lambda_O` is generally not an online observable available to the observer.

It is primarily an:

`ex-post lifetime coordinate`

that becomes fully definable once the lifetime interval is fixed.

### Boundary statement

This does not imply postmortem observation by the deceased observer.

`observer endpoint != observer's postmortem observation`

The claim is only that the completed interval can be defined from an external or meta-level description.

---

## 6. Relation to structural time / Theta_O との関係

Define total structural temporal accumulation over the lifetime:

`Theta_life,O = Theta_O(tau_d,O) - Theta_O(tau_b,O)`

If `Theta_life,O > 0`, a normalized structural coordinate may be defined:

`Theta_bar_O(tau) = [Theta_O(tau) - Theta_O(tau_b,O)] / Theta_life,O`

Then:

`Lambda_O` measures physical life-course progress,

while:

`Theta_bar_O` measures progress through the observer's total structural-update history.

These need not coincide.

Example:

`Lambda_O = 0.5`

while:

`Theta_bar_O = 0.8`

is mathematically possible.

This expresses:

`physical life progress != structural life progress`

without assigning normative value to either quantity.

---

## 7. Optional diagnostic difference / 診断量候補

A descriptive difference may be defined:

`Delta_life,O = Theta_bar_O - Lambda_O`

This quantity would indicate whether structural updating is concentrated earlier or later than physical lifetime progress.

At present this is only a descriptive candidate, not an established biological or psychological law.

---

## 8. Separation from Absolute-0 / Absolute-100

The normalized endpoints `Lambda_O = 0` and `Lambda_O = 1` are ordinary endpoints of a normalized finite life interval.

They must not be identified with the theory's stronger nonmanifest Absolute-0 / Absolute-100 concepts.

Required boundary:

`Lambda_O = 1 != Absolute-100`

and:

`Lambda_O = 0 != Absolute-0`

unless a future theory provides an independent derivation.

Death is therefore modeled here only as the terminal point of O's local observation/update trajectory, not as a demonstrated transition to Absolute-100.

---

## 9. Relation to death / 死の最小定義

Observer O follows a physical worldline:

`x_O^mu(tau)`

with an observer-specific update interval:

`tau in [tau_b,O, tau_d,O]`

At `tau_d,O`, O-specific observation/update processes terminate in the minimal model.

This does not imply:

`death of O = end of physical time`

Other worldlines and physical processes may continue.

---

## 10. Research status / 研究状態

Established here by definition:

- lifetime interval normalization
- separation of `tau_O`, `Lambda_O`, `Theta_O`, and `Psi_O`
- ex-post character of exact `Lambda_O`
- separation from Absolute-0 / Absolute-100

Not established:

- a universal relation between `Lambda_O` and `Theta_O`
- a biological law for `Delta_life,O`
- any claim that shorter and longer lives are equal in value, experience, or information
- any postmortem observer model

---

## 11. Decision

`Lambda_O` is retained as a life-course normalization coordinate within the Temporal Structure project.

It is not required for Experiment A3 and should not be inserted into short-timescale jump simulations unless the research question explicitly concerns life-course scaling.