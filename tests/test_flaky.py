import pytest
import sys
import random


@pytest.mark.flaky(reruns=5)
def test_example():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example1():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=5, condition=sys.platform.startswith("win32"))
def test_example():
    assert random.choice([True, False])
