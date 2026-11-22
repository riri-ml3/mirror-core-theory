from __future__ import annotations

from dataclasses import asdict, dataclass
from math import exp
from typing import Dict


def _unit_interval(name: str, x: float) -> float:
    x = float(x)
    if not 0.0 <= x <= 1.0:
        raise ValueError(f"{name} must be in [0, 1], got {x}")
    return x


def _sigmoid(z: float) -> float:
    if z >= 0:
        e = exp(-z)
        return 1.0 / (1.0 + e)
    e = exp(z)
    return e / (1.0 + e)


@dataclass(frozen=True)
class StructuralKernelInput:
    delta_unres: float
    r_nr: float
    beta_r: float
    foundation_stability: float
    threat: float
    kappa: float
    theta_f: float
    lambda_t: float
    t_info: float
    l_log: float
    k_conn: float
    k_o: float

    def validate(self) -> None:
        for name in (
            "delta_unres",
            "r_nr",
            "beta_r",
            "foundation_stability",
            "threat",
            "theta_f",
            "t_info",
            "l_log",
            "k_conn",
            "k_o",
        ):
            _unit_interval(name, getattr(self, name))

        if self.kappa <= 0:
            raise ValueError("kappa must be > 0")
        if self.lambda_t < 0:
            raise ValueError("lambda_t must be >= 0")


@dataclass(frozen=True)
class StructuralKernelResult:
    q: float
    g_avail: float
    t_info: float
    t_l: float
    t_k: float
    t_r: float
    x0: float
    x1: float
    x2: float
    x3: float
    x4: float
    y_rebase: float
    r_gate: float
    r_info: float
    r_l: float
    r_k: float
    r_rebase: float
    r_cycle: float
    accounting_error: float

    def as_dict(self) -> Dict[str, float]:
        return asdict(self)


def run_structural_kernel(inp: StructuralKernelInput) -> StructuralKernelResult:
    """Structural Kernel v0.1.

    Boundaries:
    - All [0,1] values are manifest-layer computational variables.
    - Numerical 0/1 are not Absolute-0/Absolute-1.
    - This is a one-cycle salience-flow accounting kernel.
    - It is not a time-resolved cognitive dynamics model.
    - It is not a throughput/service-capacity model.
    - Identity transfer maps are provisional simulation hypotheses:
        T_L = L_log
        T_K = K_conn
        T_R = 1 - K_O
    """

    inp.validate()

    d = inp.delta_unres

    # Problem-salience candidate.
    # R_nr amplifies an existing unresolved difference but cannot create
    # salience when delta_unres == 0.
    q = d + inp.beta_r * inp.r_nr * d * (1.0 - d)

    # Soft availability gate. This does not impose a hard-zero rule when
    # foundation_stability == 0; that stronger claim is not part of v0.1.
    g_avail = _sigmoid(
        inp.kappa
        * (
            inp.foundation_stability
            - inp.theta_f
            - inp.lambda_t * inp.threat
        )
    )

    # Provisional identity transfer maps.
    t_l = inp.l_log
    t_k = inp.k_conn
    t_r = 1.0 - inp.k_o

    # Ordered accounting states.
    x0 = q
    x1 = x0 * g_avail
    x2 = x1 * inp.t_info
    x3 = x2 * t_l
    x4 = x3 * t_k
    y_rebase = x4 * t_r

    # Stage residuals. These are accounting residuals, not yet assigned
    # ontological meanings such as memory loss, suppression, or carryover.
    r_gate = x0 - x1
    r_info = x1 - x2
    r_l = x2 - x3
    r_k = x3 - x4
    r_rebase = x4 - y_rebase

    # End-to-end rebaselining reach-through rate.
    # If q > 0, r_cycle == y_rebase / q.
    # If q == 0, it is a counterfactual structural coefficient only.
    r_cycle = g_avail * inp.t_info * t_l * t_k * t_r

    accounted = (
        y_rebase
        + r_gate
        + r_info
        + r_l
        + r_k
        + r_rebase
    )
    accounting_error = q - accounted

    return StructuralKernelResult(
        q=q,
        g_avail=g_avail,
        t_info=inp.t_info,
        t_l=t_l,
        t_k=t_k,
        t_r=t_r,
        x0=x0,
        x1=x1,
        x2=x2,
        x3=x3,
        x4=x4,
        y_rebase=y_rebase,
        r_gate=r_gate,
        r_info=r_info,
        r_l=r_l,
        r_k=r_k,
        r_rebase=r_rebase,
        r_cycle=r_cycle,
        accounting_error=accounting_error,
    )
