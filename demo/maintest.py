import unittest
from HtmlTestRunner import HTMLTestRunner
import time
from pathlib import Path

# 是testLoader的一个子类中实现的方法
test_dir = Path(__file__).resolve().parent / "allure-report"
discover = unittest.defaultTestLoader.discover(str(test_dir), pattern="myMath*.py")
# 为了保存每次执行的结果，你输出的报告文件名称不能是固定的（后来的会覆盖前面的），需要变化
# 时间会重复吗，以时间作为文件名
# strftime: 将当前的时间按照指定的格式转化为字符串,2022-05-25-17-27.py
# 每天可以执行一次：2022-05-25
# 每小时执行一次：2022-05-25-17
report_name = time.strftime("%Y-%m-%d-%H-%M-%S")
# 使用HTMLTestRunner运行运行测试集合discover
runner = HTMLTestRunner(
    output=str(test_dir),
    verbosity=1,
    report_title="单元测试执行报告",
    report_name=report_name,
    add_timestamp=False,
    combine_reports=True,
)
runner.run(discover)
