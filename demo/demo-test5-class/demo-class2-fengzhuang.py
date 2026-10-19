#说明：练习模板03：面向对象+模块和异常处理+IO处理
#二、封装：私有化：在变量或方法前添加两个下划线__。 self.__age、 __study()。
# 私有化访问：_类名__属性(变量名)
class student():
    #1、初始化
    def __init__(self,name,age,sex):
        self.name=name
        self.__age=age #self.__age=age 私有化变量
        self.sex=sex

    #2、提供功能的访问方式（私有属性的查看、修改getXxx()、SetXxx()
    def getAge(self):#获取年龄
        return self.__age
    def setAge(self,age): #修改年龄
        if(age>0 and age<=120):
            self.__age=age
        else:
            print("输入的年龄不符合实际情况")


    def study(self):
        print("学生的本职工作就是学习")


# 3、实例对象
xiaoli=student("小李","28","女")
# print(xiaoli.age)
print(xiaoli._student__age) #私有化访问，_类名__属性
print(xiaoli.getAge()) #获取年龄 
xiaoli.setAge(22)      #修改年龄
print(xiaoli.getAge())
 