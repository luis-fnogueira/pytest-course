import pytest


@pytest.fixture()  # Also can use autouse = True, so it's not necessary to pass it as param
def setup():
    print("\nSetup!")


def test1(setup):
    print("Executing test 1")
    assert True


@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test 2")
    assert True
