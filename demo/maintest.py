import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from pathlib import Path

# 是testLoader的一个子类中实现的方法
test_dir = Path(__file__).resolve().parent / "demo_test6_unittest"
discover = unittest.defaultTestLoader.discover(str(test_dir), pattern="myMath*.py")
# 为了保存每次执行的结果，你输出的报告文件名称不能是固定的（后来的会覆盖前面的），需要变化
# 时间会重复吗，以时间作为文件名
# strftime: 将当前的时间按照指定的格式转化为字符串,2022-05-25-17-27.py
# 每天可以执行一次：2022-05-25
# 每小时执行一次：2022-05-25-17
filename = time.strftime("%Y-%m-%d-%H-%M-%S") + ".html"
filepath = test_dir / filename
# 使用HTMLTestRunner运行运行测试集合discover
with open(filepath, "wb") as f:
    runner = HTMLTestRunner(f, verbosity=1, title="单元测试执行报告", description="第一次执行结果")
    runner.run(discover)
