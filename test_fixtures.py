import pytest


@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session!")


@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module!")


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")


def test1():
    print("Executing test 1")
    assert True


def test2():
    print("Executing test 2")
    assert True
