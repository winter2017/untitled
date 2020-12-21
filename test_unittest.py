import unittest

class Demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testclass01")
        self.assertEqual(1,1,"不相等")

    def test_case02(self):
        print("testcase02")
        self.assertIn("123","12345","后面字符串不包含前面的子串")

class Demo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_demo1_case01(self):
        print("testdemo1class01")
        self.assertEqual(1,1,"不相等")

    def test_demo1_case02(self):
        print("testdemo1case02")
        self.assertIn("123","12345","后面字符串不包含前面的子串")

if __name__ == "__main__":
    #执行方法1,执行当前模块的所有用例
    # unittest.main()
    #执行方法2，添加到测试用例套件
    # suite = unittest.TestSuite()
    # suite.addTest(Demo("test_case01"))
    # suite.addTest(Demo1("test_demo1_case01"))
    # unittest.TextTestRunner().run(suite)
    #执行方法3，同时执行多个测试方法类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo1)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)
    #执行方法4，执行某一路径下所有文件
    pass
    pass
