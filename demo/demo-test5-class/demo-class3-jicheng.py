#说明：练习模板03：面向对象+模块和异常处理+IO处理 之 面向对象
#二、继承： 支持单继承、多继承、多层继承
#格式 class 子类名(父类名):
#           子类的代码块

#定义动物类 ：父类
class anmial():
    type="动物"
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age  
        self.sex=sex 

    def eat(self):
        print("动物吃肉")
    def playGame(self):
        print("动物玩游戏")
    def sleep(self):
        print("动物要睡觉")

#定义小狗：子类，继承父类 动物类
class dog(anmial):
    type="狗类"
    #重写，子类将父类方法重写，方法名相同
    def eat(self,shiwu):
        print("动物吃%s"%(shiwu)) 
    #子类特有的方法
    def huaqian(self):
        print("花钱") 

#创建小狗对象
d=dog("小黑","12","male")
print(d.age)
d.eat("骨头")#子类生写了父类此方法，则需要按子类进行传参使用
d.sleep() #调用父类方法
d.huaqian()

#定义人类
class person(anmial):
    type="人类"
    def __init__(self,name,age,sex,xuexi):
        anmial("小红","12","male")
        self.xuexi=xuexi

class dog2():
    pass
class dog3(anmial,dog2): #多继承
    pass
 

#  多态（了解）
# 多态指的同一个对象在不同场景下可能具备不同的形态。
# 叫小花的猫（具体的对象）是一只猫（cat类）。
# 叫小花的猫（具体的对象）是一只动物（animal类）。
# python中的多态不像java语言中多态那么明显，像python这种动态语言中的多态我们称之为鸭子多态
