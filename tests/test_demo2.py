import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello"  # operations
    assert msg == "Hi", "Test failed because strings do not match"


def test_secondcreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match."
