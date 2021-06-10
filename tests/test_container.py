import pytest


@pytest.fixture()
def setup():
    print("\n Before Method")
    yield
    print("\n After Method")


@pytest.mark.smoke
def test_smoke(setup):
    print("\n Smoke")


@pytest.mark.regression
def test_regression(setup):
    print("\n Regression")
