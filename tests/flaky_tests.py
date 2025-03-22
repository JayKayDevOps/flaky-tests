import random
import unittest

class TestFlaky(unittest.TestCase):
    def test_flaky_function(self):
        """Simulates a flaky test that randomly fails."""
        outcome = random.choice([True, False])  # 50% chance of failure
        self.assertTrue(outcome, "Flaky test failed!")

if __name__ == "__main__":
    unittest.main()