#作为单元测试的测试对象
class myMath():
    #实现加法运算
    def add(self,a,b):
        if(isinstance(a,str) or isinstance(b,str)):
            return str(a)+str(b)
        else:
            return a+b
    #实现减法运算(实现上有问题，是一个bug)
    def minus(self,a,b):
        return a-b
    #实现乘法运算
    def multi(self,a,b):
        return a*b
    #实现除法运算（b为0的情况未处理）
    def devide(self,a,b):
        return a/b

if __name__=="__main__":
    mm = myMath()
    print(mm.add(12,23))