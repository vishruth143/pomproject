import pytest


@pytest.mark.usefixtures("setup_demo")
class TestExample:

    def test_fixturedemo(self):
        print("I will execute steps in fixturedemo method")

    def test_fixturedemo1(self):
        print("I will execute steps in fixturedemo1 method")

    def test_fixturedemo2(self):
        print("I will execute steps in fixturedemo2 method")

    def test_fixturedemo3(self):
        print("I will execute steps in fixturedemo3 method")
