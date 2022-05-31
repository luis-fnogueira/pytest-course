import pytest


@pytest.fixture()  # Also can use autouse = True, so it's not necessary to pass it as param
def setup1():
    print("\nSetup 1!")
    yield
    print("\nTeardown 1!")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A!")

    def teardown_b():
        print("\nTeardown B!")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("Executing test 1")
    assert True


def test2(setup2):
    print("Executing test 2")
    assert True
