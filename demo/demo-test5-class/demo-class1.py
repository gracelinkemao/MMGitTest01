#说明：练习模板03：面向对象+模块和异常处理+IO处理
#一、创建类、变量
class animal():
    """
    功能描述：实现动物类
    """
    #1、创建类变量（给所有对象使用），在类中方法外定义，是所有的对象共享变量
    type="动物"

    #2、创建实例变量（固定给某一个变量使用），在类的方法中的变量，self开头
    #先写一个方法 eat(),要求方法的第 一个参数必须是self:eat(self)
    def eat(self,shiwu):
        self.shixing=shiwu  #self开头的才是实列变量，所以 self.shixing 是实例变量
        # aa=12 #局部变量
        print("动物都要吃%s"%(shiwu))
    #定时INFO方法，来初始化动物的属性名称和性别
    def info(self,xingming,xingbie):
        self.name=xingming
        self.sex=xingbie
    #定时睡觉方法
    def sleep(self):
        print("动物都要睡觉")

    #========1、无参数构造： 创建对象的时候默认自动调用初始化。方法名固定，只能 __init__
    # def __init__(self):
    #     # pass # 空语句
    #     self.name="花花"
    #     self.sex="male"
    #========2、带参数构造：不同的对象有不同的属性值
    def __init__(self,xingming,xingbie):
        # pass # 空语句
        self.name=xingming
        self.sex=xingbie


#3、调用
#创建小猫对象
# cat=animal() #无参数构造
cat=animal("红红","male")  #带参数构造，创建对象时就传入init对应参数
print(cat.type)
cat.info("红红","male")#通过info方法就,初始化变量，给小猫确定了名字和性别
#name和sex就是 实例变量（cat这个对象的实例变量）
print(cat.name)
print(cat.sex)

cat.eat("鱼")
print(cat.shixing)

#4、构造方法，给成员变量赋值
dong=animal("红红","male") 
print(dong.type)
dong.type="狗"
print(dong.type)
 