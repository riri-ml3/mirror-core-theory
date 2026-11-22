import unittest

from discriminating_structural_experiment_v0_1 import (
    ExperimentConfig,
    intervention_signature,
    observe,
    predicted_signature_class,
    run_experiment,
)


class DiscriminatingStructuralExperimentTests(unittest.TestCase):
    def setUp(self):
        self.cfg = ExperimentConfig()

    def test_endpoint_equivalence_across_model_order(self):
        args = (
            self.cfg.x2,
            self.cfg.t_l_high,
            self.cfg.t_k_high,
            self.cfg.t_r,
        )
        ys = [
            observe(model, *args)[1]
            for model in ("LK", "KL", "COLLAPSED_PRE", "COLLAPSED_POST")
        ]
        for y in ys[1:]:
            self.assertAlmostEqual(y, ys[0], places=14)

    def test_lk_signature(self):
        sig = intervention_signature(run_experiment(self.cfg))["LK"]
        self.assertGreater(sig["E_L_mid"], 0)
        self.assertAlmostEqual(sig["E_K_mid"], 0.0, places=14)
        self.assertEqual(predicted_signature_class(sig), "L_BEFORE_K")

    def test_kl_signature(self):
        sig = intervention_signature(run_experiment(self.cfg))["KL"]
        self.assertAlmostEqual(sig["E_L_mid"], 0.0, places=14)
        self.assertGreater(sig["E_K_mid"], 0)
        self.assertEqual(predicted_signature_class(sig), "K_BEFORE_L")

    def test_collapsed_pre_signature(self):
        sig = intervention_signature(run_experiment(self.cfg))["COLLAPSED_PRE"]
        self.assertAlmostEqual(sig["E_L_mid"], 0.0, places=14)
        self.assertAlmostEqual(sig["E_K_mid"], 0.0, places=14)
        self.assertEqual(
            predicted_signature_class(sig),
            "NO_DISTINCT_MID_OR_PROBE_UPSTREAM",
        )

    def test_collapsed_post_signature(self):
        sig = intervention_signature(run_experiment(self.cfg))["COLLAPSED_POST"]
        self.assertGreater(sig["E_L_mid"], 0)
        self.assertGreater(sig["E_K_mid"], 0)
        self.assertEqual(
            predicted_signature_class(sig),
            "COLLAPSED_OR_PROBE_DOWNSTREAM",
        )

    def test_endpoint_intervention_effects_do_not_identify_order(self):
        sigs = intervention_signature(run_experiment(self.cfg))
        reference = sigs["LK"]
        for model in ("KL", "COLLAPSED_PRE", "COLLAPSED_POST"):
            self.assertAlmostEqual(
                sigs[model]["E_L_y"],
                reference["E_L_y"],
                places=14,
            )
            self.assertAlmostEqual(
                sigs[model]["E_K_y"],
                reference["E_K_y"],
                places=14,
            )

    def test_invalid_low_high_order_rejected(self):
        bad = ExperimentConfig(t_l_high=0.2, t_l_low=0.8)
        with self.assertRaises(ValueError):
            run_experiment(bad)


if __name__ == "__main__":
    unittest.main()
