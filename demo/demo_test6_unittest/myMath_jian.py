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
    def test_jian_01(self):
    
        # 通过mm对象调用add方法，获取实际结果
        actualValue = self.mm.minus(1,1)
        # 确定1-1的预期结果
        expectValue = 0
        #  断言，unittest提供了很多断言方法
        # assertEqual (first: Any, second: Any, msg: Any = ...)：判断两个值是否相等
        self.assertEqual(actualValue,expectValue,"预期结果和实际结果不一致！")

        # assertNotEqual():判断两个值是否不相等，不相等则通过还是失败？
        # 不相等就通过，相等了就失败
        # a = 12
        # b = 12
        # self.assertNotEqual(a,b)

        # flag = True
        # flag是True就通过，否则失败
        # self.assertTrue(flag)
        # self.assertFalse(flag)

        # 判断是不是同一个身份
        # assertIs(): 
        # assertIsNot()
        # a = "abc"
        # b = "bcd"
        # c = a
        # d = "abc"
        # c=a以及d="abc"和a="abc"其实是一样的，a\d\c三个变量都是指向了内存中"abc"所在地址内存
        # self.assertIs(a,d)

        # 判断是否是成员-in
        # assertIn(a，b) 判断a是否是b的成员
        # assertNotIn()

        # a = "12"
        # b = "123456"
        # c = ["12","23","233","123"]
        # self.assertIn(a,c)

        # 判断一个数据是否是一个数据类型的实例
        # assertIsInstance()
        # a = "abc"
        # b = 12
        # self.assertIsInstance(b,int)



    # 资源释放方法
    def tearDown(self):
        self.mm = None

# 先执行一下这一条用例
if __name__=="__main__":
    # 执行单元测试类myMath_add中所有的测试用例
    unittest.main()