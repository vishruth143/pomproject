import pytest


@pytest.mark.smoke
def test_firstProgram(setup_demo):
    print("Hello")


@pytest.mark.xfail
def test_secondgreetcreditCard():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser[0])
