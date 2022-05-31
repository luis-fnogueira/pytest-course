

class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nSetup TestClass!")
    
    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")
    
    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unkknown test")
    
    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unkknown test")
    
    def test1(self):
        print("Executing test 1!")
        assert True
    
    def test2(self):
        print("Executing test 2!")
        assert True
