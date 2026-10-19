# 创建单元测试用例步骤：
# 导包unittest
# 创建单元测试类
# 定义单元测试用例的三个方法
# 设计test开头方法
# 执行单元测试用例
import  unittest

from pytest import skip
from myMath import myMath

# 创建单元测试类
class myMath_chu(unittest.TestCase):
    # 定义一个标志位（flag=1，表示功能都实现了，flag=0表示功能未实现）
    flag = 1
    # 定义单元测试用例的三个方法
    def setUp(self):
        self.mm = myMath()
    
    # 如果该方法的功能尚未实现，我们能不能写用例？能不能执行？
    # 被跳过的用例执行用s来表示；执行通过的用例用.来表示
    @unittest.skip("无条件地调过该用例的执行")
    def test_chu_01(self):
        # 实际结果
        actualValue= self.mm.devide(5,2)
        # 预期结果
        expectValue = 2.5
        # 断言（断言失败--failure）
        # 脚本有语法错误会报error
        self.assertEqual(actualValue,expectValue,"预期结果与实际结果不一致！！")
    @unittest.skipIf(flag==0,"flag为0则跳过执行该用例！")
    def test_chu_02(self):
        # 实际结果
        actualValue= self.mm.devide(5,2)
        # 预期结果
        expectValue = 2.5
        # 断言（断言失败--failure）
        # 脚本有语法错误会报error
        self.assertEqual(actualValue,expectValue,"预期结果与实际结果不一致！！")

    # 这条用例抛出异常，合不合理？
    # 预期的该用例要抛出:expected failures=1
    @unittest.expectedFailure
    def test_chu_03(self):
        # 实际结果
        actualValue= self.mm.devide(5,0)
        # 预期结果
        expectValue = 2.5
        # 断言（断言失败--failure）
        # 脚本有语法错误会报error
        self.assertEqual(actualValue,expectValue,"预期结果与实际结果不一致！！")
    
    # 非预期的通过了，unexpected successes=1
    @unittest.expectedFailure
    def test_chu_04(self):
        # 实际结果
        actualValue= self.mm.devide(5,2)
        # 预期结果
        expectValue = 2.5
        # 断言（断言失败--failure）
        # 脚本有语法错误会报error
        self.assertEqual(actualValue,expectValue,"预期结果与实际结果不一致！！")


    def tearDown(self):
        self.mm = None

if __name__ == "__main__":
    # unittest.main()
    # 1、创建3个所需对象
    # 创建测试集合对象
    suitt = unittest.TestSuite()
    # 创建一个TestLoader对象
    loader = unittest.TestLoader()
    # 创建结果对象
    result = unittest.TestResult()

    # 2、loader负责将测试用例加载到suitt中去
    # 参数可以是： a module, a test case class, a test method
    # 指定模块名，会把模块中的所有用例加载进来
    # suitt.addTest(loader.loadTestsFromName("myMath_chu"))
    # 指定模块中的某个类名
    # suitt.addTest(loader.loadTestsFromName("myMath_chu.myMath_chu"))
    # 指定模块中类中的某条测试用例名
    suitt.addTest(loader.loadTestsFromName("myMath_chu.myMath_chu.test_chu_01"))


    # 3、执行
    suitt.run(result)

    # 4、查看结果
    print(result.__dict__)