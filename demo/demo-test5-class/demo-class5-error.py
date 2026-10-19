#说明：练习模板05:面向对象+模块和异常处理+IO处理 之  异常处理 
# 用try-except语言。finally，不管运行的是try还是except，最终都要运行finally中的代码块
# raise抛出异常

#========1、捕捉异常
try:
    list01=[1,2,3]
    print(list01[3]) #  索引越界
except Exception as e: 
    print("报错了...")#报错时可以对应进行代码处理逻辑
    print(e)
finally:
    print("不管你走的是try，还是except，最终都要运行这一句！")

#========2、通过关键字raise手动抛出自定义 # 需求：设计方法，参数为负值，则抛出数据无效异常
def jiaoyan(a):
    if a<0:
        raise Exception("不能为负数，输入异常",a) #抛出异常
    else:
        return a
print(jiaoyan(-2)) # Exception: ('不能为负数，输入异常', ‐2)


# ========3、自定义异常类,继承自Exception
class myException(Exception):
    def __init__(self,code,info):
        self.code=code
        self.info=info
 
def jiaoyan2(a):
    if a<0:
        raise myException("1001","数据无效") #手动抛异常
    else:
        return a
print(jiaoyan2(-2)) # __main__.myException: ('1001', '数据无效')