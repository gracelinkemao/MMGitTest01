# 说明：练习模板04：面向对象+模块和异常处理+IO处理 之   模块
# 四 、模块： 在python中的有很多内置模块（标准模块Python\Lib）、还可以通过pip安装第三方模块（Python\Lib\site-packages）。
# 模块是可以将指定功能的代码写在一个模块中，方便代码的管理
# 包：是包括多个模块的文件夹，文件夹中一定要有一个__init__.py文件
# 包的作用：带包导入模块

# 2、创建模块
# 就是创建.py文件。

# 3、模块(包)
# 导入：导入random模块，把random模块中代码，做一个副本拿到当前模块中
import random  # import 模块名/包名
from random import randint  # from 模块名/包名 import 类名/方法名/变量名 .从random模块中导入其中一个方法randint()，导入更精确了
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By #带包导入

# 4、动态获取当前文件目录，并加入默认目录，则在导入包时不用再加路径 （导入的模块在当前文件的上一级目录）
import sys
import os

# print(sys.path) #python在导包的时候默认（sys.path）要找4个目录
# sys.path.append(r"D:\Project1\hg_auto_test\pythonTest01")#若导入的包不在默认目录，需要将你要导包的模块所在目录加入到sys.path，绝对路径
# sys.path.append(r"./")# 在vscode 指的是当前工程目录，相对路径。但在cmd中不能使用
# os.path.dirname(__file__):__file__:当前文件路径，获取当前文件所在目录（相对值），在vscode可以，但在cmd不行
# os.path.abspath(os.path.dirname(__file__)):将目录转化为绝对值 ,在vscode\cmd都可以运行
path1 = os.path.abspath(os.path.dirname(__file__))  # __file__：动态获取当前文件所在目录的绝对值， 即可在CMD，也可以在VSCODE，也不使用绝对路径
path2 = os.path.abspath(os.path.dirname(path1))
print(path2)
sys.path.append(path2)  # 将对应模块路径加入到sys.path中
# sys.path 中的元素是什么：
# 当前模块所在的文件夹目录
# python的原码目录
# python的根目录
# python的标准库lib
# python的第三方库:site-package

#  开始导包
# import test01

# 4、动态获取当前文件目录，如 test1在day08，test2在day09（导入的模块在当前的同级目录）
# 1、直接将day08获取并追加到sys.path
#  __file__: 当前文件
#  os.path.dirname(__file__)：获取当前文件所在的目录（相对值）（vscode中可以，但是在cmd不识别）
#  os.path.abspath(os.path.dirname(__file__))：将获取的目录转化为绝对值的形式（vscode、cmd运行都正常）
path1 = os.path.abspath(os.path.dirname(__file__))
#  获取上一级目录
path2 = os.path.abspath(os.path.dirname(path1)) + r"/day08"
#  把path2追加到sys.path
# sys.path.append(path2)
# import test01


# 5、__name__ 内置变量，固定写法。当前类中对应的值就是 __main__。非当前文件中执行，而是通过导包在其他类执行则不会是__main__
# 在m1中写此代码，则执行时其值为 __main__
# 在m2中调用时执行时其值不为__main__，而是m1
# 所以一般调试使用，这样只在当前文件类执行才会执行，其他类调用不会执行。后续写代码都加上此句
if __name__ == "__main__":
    print(__name__)
    print("执行，，")
else:
    print(__name__)

"""
# 跨目录导模块（包）
# 希望在当前文件中导入day08目录下test01.py
from importlib.resources import path
import os
import sys
# 2、将day08定义成包：__init__.py
# __file__: 当前文件
# os.path.dirname(__file__)：获取当前文件所在的目录（相对值）（vscode中可以，但是在cmd不识别）
# os.path.abspath(os.path.dirname(__file__))：将获取的目录转化为绝对值的形式（vscode、cmd运行都正常）
path1 = os.path.abspath(os.path.dirname(__file__))
# 获取上一级目录
path2 =  os.path.abspath(os.path.dirname(path1))
# 在day08中天见__init__.py文件
# 把path2追加到sys.path
sys.path.append(path2)

# 如果day08是包的话，是可以直接带包导入的
# 因为python能够定位到pythonDemo目录，就能检索其下的模块和包
import day08.test0120 from  day08.test01 import playGame
"""
