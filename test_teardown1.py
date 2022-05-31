
def setup_module():
    print("Setup Module!")


def teardown_module():
    print("Teardown Module")

def setup_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unkknown test")


def teardown_function(function):
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2")
    else:
        print("\nTearing down unkknown test")


def test1():
    print("Executing test 1!")
    assert True


def test2():
    print("Executing test 2!")
    assert True
