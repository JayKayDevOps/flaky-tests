import random
import pytest

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_flaky():
    """A test with a 16% chance of failure."""
    failure_chance = 0.16
    assert random.random() > failure_chance, "Flaky test failed!"