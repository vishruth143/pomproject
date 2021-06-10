import pytest


@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_editprofile(self, data_load):
        print(data_load)
        print(data_load[0])
        print(data_load[2])
