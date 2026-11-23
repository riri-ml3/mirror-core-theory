from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class ExperimentConfig:
    x2: float = 0.5184
    t_r: float = 0.85
    t_l_high: float = 0.80
    t_l_low: float = 0.30
    t_k_high: float = 0.70
    t_k_low: float = 0.50


@dataclass(frozen=True)
class ModelObservation:
    model: str
    condition: str
    t_l: float
    t_k: float
    mid: float
    y_rebase: float


def _validate_unit(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be in [0,1], got {value}")
    return value


def _validate_config(cfg: ExperimentConfig) -> None:
    for name in (
        "x2",
        "t_r",
        "t_l_high",
        "t_l_low",
        "t_k_high",
        "t_k_low",
    ):
        _validate_unit(name, getattr(cfg, name))

    if cfg.t_l_low > cfg.t_l_high:
        raise ValueError("t_l_low must be <= t_l_high")
    if cfg.t_k_low > cfg.t_k_high:
        raise ValueError("t_k_low must be <= t_k_high")


def observe(model: str, x2: float, t_l: float, t_k: float, t_r: float) -> Tuple[float, float]:
    """Return (mid, y_rebase) for a competing structural model.

    Models
    ------
    LK:
        L-stage precedes K-stage.
        mid = x2 * t_l

    KL:
        K-stage precedes L-stage.
        mid = x2 * t_k

    COLLAPSED_PRE:
        No distinct L/K internal stage is represented at the probe.
        Probe is upstream of the collapsed transformation.
        mid = x2

    COLLAPSED_POST:
        No distinct L/K internal stage is represented at the probe.
        Probe is downstream of the collapsed transformation.
        mid = x2 * t_l * t_k

    All four models have the same endpoint:
        y_rebase = x2 * t_l * t_k * t_r

    Therefore endpoint-only data are structurally insufficient to identify
    stage order under this multiplicative kernel.
    """
    if model == "LK":
        mid = x2 * t_l
    elif model == "KL":
        mid = x2 * t_k
    elif model == "COLLAPSED_PRE":
        mid = x2
    elif model == "COLLAPSED_POST":
        mid = x2 * t_l * t_k
    else:
        raise ValueError(f"unknown model: {model}")

    y_rebase = x2 * t_l * t_k * t_r
    return mid, y_rebase


def run_experiment(cfg: ExperimentConfig = ExperimentConfig()) -> List[ModelObservation]:
    _validate_config(cfg)

    conditions = (
        ("HH", cfg.t_l_high, cfg.t_k_high),
        ("LH", cfg.t_l_low, cfg.t_k_high),
        ("HL", cfg.t_l_high, cfg.t_k_low),
        ("LL", cfg.t_l_low, cfg.t_k_low),
    )
    models = ("LK", "KL", "COLLAPSED_PRE", "COLLAPSED_POST")

    rows: List[ModelObservation] = []
    for model in models:
        for condition, t_l, t_k in conditions:
            mid, y = observe(model, cfg.x2, t_l, t_k, cfg.t_r)
            rows.append(
                ModelObservation(
                    model=model,
                    condition=condition,
                    t_l=t_l,
                    t_k=t_k,
                    mid=mid,
                    y_rebase=y,
                )
            )
    return rows


def intervention_signature(
    rows: Iterable[ModelObservation],
) -> Dict[str, Dict[str, float]]:
    """Return normalized intervention effects at mid and endpoint.

    Effect = 1 - low_condition / high_condition.

    L intervention compares LH with HH.
    K intervention compares HL with HH.
    """
    by_model: Dict[str, Dict[str, ModelObservation]] = {}
    for row in rows:
        by_model.setdefault(row.model, {})[row.condition] = row

    out: Dict[str, Dict[str, float]] = {}
    for model, cells in by_model.items():
        hh = cells["HH"]
        lh = cells["LH"]
        hl = cells["HL"]

        if hh.mid == 0 or hh.y_rebase == 0:
            raise ZeroDivisionError("baseline HH must be positive")

        out[model] = {
            "E_L_mid": 1.0 - lh.mid / hh.mid,
            "E_K_mid": 1.0 - hl.mid / hh.mid,
            "E_L_y": 1.0 - lh.y_rebase / hh.y_rebase,
            "E_K_y": 1.0 - hl.y_rebase / hh.y_rebase,
        }
    return out


def predicted_signature_class(signature: Dict[str, float], tol: float = 1e-12) -> str:
    l = abs(signature["E_L_mid"]) > tol
    k = abs(signature["E_K_mid"]) > tol

    if l and not k:
        return "L_BEFORE_K"
    if k and not l:
        return "K_BEFORE_L"
    if not l and not k:
        return "NO_DISTINCT_MID_OR_PROBE_UPSTREAM"
    return "COLLAPSED_OR_PROBE_DOWNSTREAM"


def markdown_summary(cfg: ExperimentConfig = ExperimentConfig()) -> str:
    rows = run_experiment(cfg)
    signatures = intervention_signature(rows)

    lines = [
        "| Model | E_L(mid) | E_K(mid) | E_L(endpoint) | E_K(endpoint) | Signature |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for model in ("LK", "KL", "COLLAPSED_PRE", "COLLAPSED_POST"):
        s = signatures[model]
        lines.append(
            f"| {model} | {s['E_L_mid']:.6f} | {s['E_K_mid']:.6f} | "
            f"{s['E_L_y']:.6f} | {s['E_K_y']:.6f} | "
            f"{predicted_signature_class(s)} |"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    print(markdown_summary())
