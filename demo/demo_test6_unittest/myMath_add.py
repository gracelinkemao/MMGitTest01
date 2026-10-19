# 该模块实现对myMath类中的add方法的单元测试
# 使用unittest框架，设计测试用例
# add加法运算测试用例：1+1；-1+2；-1+（-2）；1.1+2.2；'a'+'b'
# 1、导包
import unittest
from myMath import myMath

# 2、创建一个单元测试类（继承了unittest.TestCase的类）
class myMath_add(unittest.TestCase):
    # 3、单元测试用例的三部分：3个方法
    # 初始化
    def setUp(self):
        # 先创建myMath的对象
        self.mm = myMath()

    # 单元测试用例的主体方法
    def test_add_01(self):
        # 文档注释必须放在代码块的第一行可执行代码位置
        """实现1+1的功能"""
        # 通过mm对象调用add方法，获取实际结果
        actualValue = self.mm.add(1,1)
        # 确定1+1的预期结果
        expectValue = 2
        #  断言，unittest提供了很多断言方法
        # assertEqual (first: Any, second: Any, msg: Any = ...)：判断两个值是否相等
        self.assertEqual(actualValue,expectValue,"预期结果和实际结果不一致！")

    # 单元测试用例的主体方法
    def test_add_02(self):
        """实现-1+1的加法功能"""
        print("222222222222222222")
        # 通过mm对象调用add方法，获取实际结果
        actualValue = self.mm.add(-1,2)
        expectValue = 1
        #  断言
        self.assertEqual(actualValue,expectValue,"预期结果和实际结果不一致！")

    # 单元测试用例的主体方法
    def test_add_03(self):
        """实现-1+(-2)的加法功能"""
        # 通过mm对象调用add方法，获取实际结果
        actualValue = self.mm.add(-1,-2)
        expectValue = -3
        #  断言
        self.assertEqual(actualValue,expectValue,"预期结果和实际结果不一致！")

    # 单元测试用例的主体方法
    def test_add_04(self):
        """实现a+b的加法功能"""
        # 通过mm对象调用add方法，获取实际结果
        actualValue = self.mm.add('a','b')
        expectValue = "ab"
        #  断言
        self.assertEqual(actualValue,expectValue,"预期结果和实际结果不一致！")

    # 单元测试用例的主体方法
    def test_add_05(self):
        """实现a+2的加法功能"""
        print("5555555555555555555")
        # 通过mm对象调用add方法，获取实际结果
        actualValue = self.mm.add('a',2)
        expectValue = "a2"
        #  断言
        self.assertEqual(actualValue,expectValue,"预期结果和实际结果不一致！")
    # 资源释放方法
    def tearDown(self):
        self.mm = None

# 先执行一下这一条用例
if __name__=="__main__":
    # 执行单元测试类myMath_add中所有的测试用例
    # 定制执行测试用例的数量和顺序，怎么办？
    # 需求：只想执行第二条和第五条，而且顺序上先五后二。
    # unittest.main()
    # 引入测试集合解决这个问题
    # 1、创建测试集合的对象suitt
    suitt = unittest.TestSuite()
    # <unittest.suite.TestSuite tests=[]>
    # 2、测试集合对象有个addTest(),作用是将一条用例追加到测试集合
    # addTest(单元测试类名("用例方法名"))
    suitt.addTest(myMath_add("test_add_05"))
    suitt.addTest(myMath_add("test_add_02"))
    # <unittest.suite.TestSuite tests=[<__main__.myMath_add testMethod=test_add_05>]>
    # 3、运行测试集合即可
    # 通过run来执行测试集合suitt中的测试用例，执行的结果应该保存在哪？存在TestResult对象中
    result = unittest.TestResult()
    # 执行集合，把结果保存在result中
    # suitt.run(result)
    # 4、查看结果
    # print(result.__dict__)

    # 也可以单个用例执行
    case = myMath_add("test_add_05")
    case.run(result)
    print(result.__dict__)
