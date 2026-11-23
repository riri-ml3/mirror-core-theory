import unittest

from structural_kernel_v0_1 import (
    StructuralKernelInput,
    run_structural_kernel,
)


class StructuralKernelTests(unittest.TestCase):
    def base(self, **overrides):
        data = dict(
            delta_unres=0.6,
            r_nr=0.7,
            beta_r=0.5,
            foundation_stability=0.8,
            threat=0.2,
            kappa=8.0,
            theta_f=0.4,
            lambda_t=0.5,
            t_info=0.8,
            l_log=0.85,
            k_conn=0.75,
            k_o=0.2,
        )
        data.update(overrides)
        return StructuralKernelInput(**data)

    def test_delta_zero_produces_zero_realized_flow(self):
        out = run_structural_kernel(self.base(delta_unres=0.0))
        self.assertEqual(out.q, 0.0)
        self.assertEqual(out.y_rebase, 0.0)
        self.assertEqual(
            out.r_gate
            + out.r_info
            + out.r_l
            + out.r_k
            + out.r_rebase,
            0.0,
        )

    def test_delta_one_makes_q_one_independent_of_nonrecoverability(self):
        for r_nr in (0.0, 0.3, 1.0):
            out = run_structural_kernel(
                self.base(delta_unres=1.0, r_nr=r_nr)
            )
            self.assertAlmostEqual(out.q, 1.0, places=14)

    def test_q_is_bounded_on_grid(self):
        for i in range(21):
            delta = i / 20
            for j in range(21):
                r_nr = j / 20
                for k in range(11):
                    beta_r = k / 10
                    out = run_structural_kernel(
                        self.base(
                            delta_unres=delta,
                            r_nr=r_nr,
                            beta_r=beta_r,
                        )
                    )
                    self.assertGreaterEqual(out.q, 0.0)
                    self.assertLessEqual(out.q, 1.0)

    def test_stage_flow_is_nonincreasing(self):
        out = run_structural_kernel(self.base())
        xs = [
            out.x0,
            out.x1,
            out.x2,
            out.x3,
            out.x4,
            out.y_rebase,
        ]
        self.assertTrue(
            all(
                downstream <= upstream + 1e-15
                for upstream, downstream in zip(xs, xs[1:])
            )
        )

    def test_salience_flow_accounting_identity(self):
        out = run_structural_kernel(self.base())
        accounted = (
            out.y_rebase
            + out.r_gate
            + out.r_info
            + out.r_l
            + out.r_k
            + out.r_rebase
        )
        self.assertAlmostEqual(out.q, accounted, places=14)
        self.assertAlmostEqual(out.accounting_error, 0.0, places=14)

    def test_each_zero_transfer_blocks_downstream_realized_flow(self):
        for key in ("t_info", "l_log", "k_conn"):
            out = run_structural_kernel(self.base(**{key: 0.0}))
            self.assertEqual(out.y_rebase, 0.0)

        out = run_structural_kernel(self.base(k_o=1.0))
        self.assertEqual(out.y_rebase, 0.0)

    def test_r_cycle_matches_realized_ratio_when_q_positive(self):
        out = run_structural_kernel(self.base())
        self.assertGreater(out.q, 0.0)
        self.assertAlmostEqual(
            out.r_cycle,
            out.y_rebase / out.q,
            places=14,
        )

    def test_r_cycle_is_counterfactual_when_q_zero(self):
        out = run_structural_kernel(self.base(delta_unres=0.0))
        self.assertEqual(out.y_rebase, 0.0)
        self.assertGreater(out.r_cycle, 0.0)

    def test_final_product_does_not_identify_stage_order(self):
        a = run_structural_kernel(
            self.base(t_info=0.4, l_log=0.9)
        )
        b = run_structural_kernel(
            self.base(t_info=0.9, l_log=0.4)
        )

        # End-to-end multiplication is commutative.
        self.assertAlmostEqual(
            a.y_rebase,
            b.y_rebase,
            places=14,
        )

        # Ordered intermediate states retain the stage distinction.
        self.assertNotAlmostEqual(a.x2, b.x2, places=12)

    def test_soft_gate_does_not_force_hard_zero_at_foundation_zero(self):
        out = run_structural_kernel(
            self.base(foundation_stability=0.0)
        )
        self.assertGreater(out.g_avail, 0.0)
        self.assertGreater(out.y_rebase, 0.0)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            run_structural_kernel(self.base(delta_unres=-0.1))

        with self.assertRaises(ValueError):
            run_structural_kernel(self.base(kappa=0.0))

        with self.assertRaises(ValueError):
            run_structural_kernel(self.base(lambda_t=-0.1))


if __name__ == "__main__":
    unittest.main()
