import sys
#说明：练习模板02：运算符+控制语句+函数
#======================================一、运算符 
# ===================1、算术运算
print(1+1)   #加
print(+12)   
print("a"+"b")   
print(21-1)   #减
print(21*2)   #乘
print(2**3)   #幂运算符号：2**3、3**2
print(21/2)   #除,精确值，带小数
print(21//2)  #除,整除运算：只取整数部分
print(11%2)   #除,取余数  #判断是偶数还是奇数 %2等于1为奇，=0为偶

#===================2、赋值运算符
#1、=最常见的一个赋值运算符号，要和==分开。
a=1+1 
a+=2 #相当于a=a+2 
a-=2 #相当于a=a-2 
a*=2 #相当于a=a*2 
a/=2 #相当于a=a/2 
a**=2 #相当于a=a**2 
a%=2 #相当于a=a%2 
a//=2 #相当于a=a//2
print(a)
#===================3、关系运算（比较运算）
print(12==13)
print(12!=13)
print(12>13)
print(12<13)
print(12<=13)
print(12>=13)
#===================4、逻辑运算符：主要是处理布尔类型数据（True和False），也可以有其他数据类型参与运算。所有为真则为真，有一个为假则为假
#运算符：
# and、同为true，则为真，否则为False （即都为真才满足）
# or、同为False，则为False，否则为True (即有一个为真则满足)
# not 非True即为False，非False即为True
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not False)
#结合关系运算和逻辑运算来使用
a=12
b=23
print((a<b) and (a==12))
#处理数据不是布尔值的情况(理解)
#and：如果and左侧的运算数是False,则结果是False；如果左侧不是False，则返回and右侧的值
#or:or左侧的运算数是True，则结果是True；左侧是False，则结果是右侧的值；如果左侧是非布尔值，则返回左侧的值
#not:运算数是非布尔类型的话，非0当作True处理；0当作False处理

#===================5、位运算符：位运算符：处理的运算数是二进制的0、1
#位运算符包括：&、|、~、^、<<、>>
#1、位与运算&：参与运算的两个位，同时为1则为1，否则为0
a=60
b=13
print(a&b)
#2、位或运算|：参与运算的两个位，同时为0则为0，否则为1
print(a|b)
#3、取反运算~：把每一位补码的运算数取反，0变1、1变0
print(~a)
#4、位异或运算^:参与运算的两个位数据相同则为0，不同则为1
print(a^b)
#5、<<左移运算:将二进制的补码数据，整体向左侧移动指定的位数，最左侧抛弃，右侧补零
#特点：往左移动n位，相当于原来数据乘以(2**n)
print(a<<2)
#6、>>右移运算:将二进制的补码数据，整体往右侧移动指定的位数，最左侧填零，最右侧抛弃
#特点：往右移动n位，相当于原来数据除以(2**n)
print(a>>1)
#练习：a=30,b=9
#a&b
#a|b
#~a
#a^b80 #a>>1
#a<<2

#===================6、成员运算符 in、notin 看某个元素是否是序列类型数据的成员
str1="ABCDEFG"
list1=list(str1)
tuple1=tuple(str1)
print(list1)
print(tuple1)
#in:判断元素是序列类型的成员吗？是就返回True，否则False
#notin:判断元素不是序列类型的成员吗？不是就返回True，否则False
print("A" in str1)
print("A" in list1)
print("A" in tuple1)

print("A" not in  str1)
print("A" not in list1)
print("A" not in tuple1)
#===================7、身份运算符 is、notis,返回值也是True和False
#身份判断其实比较的是数据存储的地址是否相同，id()是可以获取变量的地址的
str1="abc"
str2="cba"
str3=str1
print(id(str1))
print(id(str2))
print(id(str3))
print(str1 is str2)
print(str1 is str3)

#======================================二、控制语句
#一、分支结构语句（if条件控制语句）
#python中的分支结构语句，只有if语句，没有switch语句。
#score=int(input("请输入你的考试成绩："))
score=112
if(score>90):
    print("优！！！")
elif(score>=60 and score<=60):
    print("及格了！！！")
else:
    print("未级格")
print("不同层级，和IF无关了！！！")
# 判断是否被2、3整除
#data=int(input("请输入一个整数"))
data=12
if(data%2==0):
    if(data%3==0):
         print("可以同时被2和3整审")
    else:
        print("可以被2整审，不能被3整除")
else:
    if(data%3==0):
         print("可以被3整审，不能被2整除")
    else:
        print("不能被2整审，也不能被3整除")

#二、循环控制语句-for 
for i in "0123456":
    print(i) 
#从LIST集合中取值
student_name=["allen","小王","小张"]
for ui in student_name:
    print(ui) 
#字典，从键值对中取值
userInfo={"username":"allen","password":"123456"}
for ui in userInfo:
    print(ui)
    print(userInfo[ui])
for key in userInfo.keys():
    print(key)
for value in userInfo.values():
    print(value)
for item in userInfo.items(): 
    print(item[0])
    print(item[1])
#range（）的使用:range(start,end,step):生成一个序列，从start开始，每隔step间隔，直到end结束所组成的序列。左闭右开
#rstart:开始值，是可以取到
#rend：结束值，是取不到的
#rstep：步进，间隔，默认是1，可以设置为其他
for i in range(0,9,2):
    print("输出的是"+str(i))
for i in range(10,0,-1):
    print("输出从10到0"+str(i))
#双层for循环（掌握）
for i in range(1,10):
    for j in range(1,10):
        print("两个值分别是%d：%d"%(i,j))

# 九九乘法中决表
for nrow in range(1,10):
#内层for循环控制列的输出，内层循环次数就节省了很多
    for ncol in range(1,nrow+1):
        print("%d*%d=%2d"%(ncol,nrow,ncol*nrow),end="\t")
#内层for循环结束后，需要回车换行
    print()

# 1至10偶数的和
sum=0
for i in range(2,11,2):
    sum+=i
print("方法1：1至10偶数的和"+str(sum))
sum=0
for i in range(1,11):
    if(i%2==0):
         sum+=i
print("方法2：1至10偶数的和"+str(sum))



#三、使用冒泡算法对列表进行排序
#有一个列表list1=[6,2,1,7,9,2]
#通过for循环实现列表元素的排序（从小到大排序），不能用sort方法。
#1、冒泡排序方法：比较相邻的两个数据，较大者往后移动
list1=[6,2,1,7,9,2]
#外层控制排序的次数n是列表长度‐1
for n in range(0,len(list1)-1):
    #内层for循环来做比较的次数,相邻的两个数据的比较，较大值往后排
    for m in range(0,len(list1)-1):
        if(list1[m] >= list1[m+1]):
            #交换两个位置的数据11 #1、定义临时遍历
             temp1 = list1[m]
             list1[m]=list1[m+1]
             list1[m+1]=temp1

             #2、多变量赋值
            # list1[m],list1[m+1]=list1[m+1],list1[m]

            #3、算术运算
            # list1[m]=list1[m]+list1[m+1]
            # list1[m+1]=list1[m]-list1[m+1]
            # list1[m]=list1[m]-list1[m+1]

            #4、使用异或运算
            # list1[m]=list1[m]^list1[m+1]
            # list1[m+1]=list1[m]^list1[m+1]
            # list1[m]=list1[m]^list1[m+1]
print(list1)


#2、快速排序方法
list2=[6,2,1,7,9,2]
list2.sort()
print(list2)

#四、循环控制语句-while ：一般用于循环次数不确定的场景。，while和for循环是可以相互转化的
while(a<=5):
    a+=1
else:
    print(a)
print("关我啥事！")

#纸厚度0.01，要折多少次，才能高于8848
houdu=0.01
height=8848
count=0
while houdu<height:
    houdu*=2
    count+=1
else:
    #厚度大于8848
    print("折叠厚度%d，折了%d次"%(houdu,count))

#break和continue
#break结束单层for循环（循环到第二次遇到了break,后续的七次都不做了）
#continue是结束本次循环（循环到第二次遇到了continue，Continue后面的代码不再执行，然后进入第三次循环）
#python中不存在++、‐‐运算符
for i in range(1,5):
    for j in range(1,5):
        if(j%2==0):
            break
        print("输出数据：%d:%d"%(i,j))

# 练习：
# 阶乘:5的阶乘,5*4*3*2*1
# str1="54321"
# jiecheng=1
# for i in str1:
#     jiecheng *=int(i)
# print(jiecheng)

# 阶乘:10的阶乘
jiecheng=1
for i in range(10,0,-1):
    jiecheng *=i
print(jiecheng)

# 将输入的4位整数倒序输出，3421==>1，2，4，3
#方法1
#zhengshu=int(input("请输入4位整数："))
zhengshu=3421
str1=str(zhengshu)
for i in str1[::-1]:
    print(jiecheng)
#方法2
list1=list(str1)
list1.reverse() #反转列表
for i in list1:
    print(i)

#百钱买百鸡，公鸡5钱一只，母鸡3钱一只，小鸡1钱3只，问100钱买100只鸡，分别怎么购买？
# 买公鸡X只，母鸡Y只，小鸡Z只，则 X+Y+Z=100 and 5*x+3*y+z/3=100
#第一层控制买公鸡的数量
for x in range(1,21):
    #第二层控制买母鸡的数量
    for y in range(1,34):
        #第三层控制买小鸡的数量
        for z in range(1,101): #能买300只，但题目不超过100只
            if (x+y+z==100 and 5*x+3*y+z/3==100):
                print("买公鸡%d只，母鸡%d只，小鸡%d只，可以满足要求。"%(x,y,z))

#100至999的整数，各位数的立方等于它本身这个数
count=0
for a in range(100,1000):
    bai=a//100 #百位的数
    shi=a//10%10 #十位的数
    ge=a%10 #个位的数
    if(bai**3+shi**3+ge**3==a):
        print("水仙花数为:"+str(a))
        count+=1
print("水仙花数总共有%d个:"%count)

#100至999的整数，
count=0
for a in range(100,1000):   
    he=0 #获取个十百数字的立方和的变量
    for i in str(a): #将几位数分别循环获取
        he+=int(i)**3
    if(he==a):
        print("水仙花数为:"+str(a))
        count+=1
print("水仙花数总共有%d个:"%count)


# ======================================三、函数
# def方法名（参数列表）：
#   方法代码块
#   return返回值

#======一、 定义一个无参数的方法
def ninenine():
    # 九九乘法中决表
    for nrow in range(1,10):
        for ncol in range(1,nrow+1):
            print("%d*%d=%2d"%(ncol,nrow,ncol*nrow),end="\t")
        print()
# 定义一个有参数、有返回值的方法
def sum1(a,b):
    sum2=a+b
    return sum2

#调用
#1、直接调用，没有返回值
ninenine()
# 2、输出调用，把方法的调用放在print()方法中，一般要求带返回值，用只用一次
print(sum1(1,2))
# 3、赋值调用，将返回值赋值给一个新的变量，新的变量参与后续运算
a=sum1(1,2)
print(a+3)

def sumTwo():
    a=int(input("请输入第一个整数:"))
    b=int(input("请输入第一个整数:"))
    c=a+b
    return c

#======二、参数特点
#不可变参数：字符串\元组\数字 作为参数，不能更改实际参数的值
a=12
b=23
def change(a):
    a=13
print(change(b))
print(b)
print(a)

#可变参数:列表\字典 作为形式参数使用,是可以更改实际参数的值的
list1=[1,23,34,4]
def change2(listt):
    listt.append("123")
change2(list1)
print(list1)


#======三、函数的参数使用形式
#===1、位置参数：参数的个数和顺序要和定义的时候一致（个数和顺序）
#需求：输出用户名和性别，打印出
def printInfo1(name,sex):
    print("hello %s,%s,欢迎！"%(name,sex))
#调用
printInfo1("张三","男")

def printInfo2(name,sex):
    dict1={1:"先生",2:"女士"}
    if isinstance(sex,int):
        print("hello %s,%s,欢迎！"%(name,dict1[sex]))
    else:
        print("请输入整数")
printInfo2("张三",1)

#===2、关键字参数：
#使用key=value的格式进行传参（key指的是方法定义时候的形式参数的名称）
#关键字参数后面不允许出现位置参数
#位置参数后面可以出现关键字参数，不能给同一个位置变量重复传值。
printInfo2(sex=1,name="张三")

#===3、默认值参数：
#默认值在定义的时候赋值即可，调用的时候可以给值，也可以不给值
#在定义变量的时候，默认值参数要放在参数列表的靠右的位置（放在位置参数的右侧）
#默认值参数的值建议是定位不可变类型
listS=[]
def studentInfo(name,age,school="北京"):
    listS.append(name)
    listS.append(age)
    listS.append(school) 
studentInfo("allen",28)
studentInfo("allen",28,"西安")
studentInfo("allen",28,"深圳")
print(listS)

#===4、不定长参数：
#用来实现参数个数不确定的这种方法。
#使用*args、**kwargs来接受多余的值(2个*时，必须使用关键字进行传参)，分别存放在元组和字典中
def sum5(a,b,*args): 
    # print(args)
    result=a+b
    for i in args:
        result+=i
    return result
print(sum5(1,2,3,4,5,6,7,8))
print(sum5(2,3))

def sum6(a,b,**kwargs):  
    result=a+b
    for i in kwargs:
        result+=kwargs[i]
    return result 
print(sum6(1,2,c=3))


#======四、其他常用语句
# 1、return 多个值被封装在了元组中返回
def sum7(a,b):
    return a,b,a+b
result=sum7(2,3)
print(result)
# 2、lambda用法
# 匿名函数，不用def定义的函数，是lambda定义。
# 一般用于定义逻辑比较简单的方法。
# 该方法不会被其他方法重复调用（不需要以方法的形式存储在内存中了）
# 格式：变量名=lambda变量1，变量2:表达式
#定义一个匿名函数sum，求两个整数a和b的和
sum8 = lambda a,b:a+b
#调用匿名函数
print(sum8(1,2))


#练习
def studentManage():
    #循环实现学员的增删改查，需要写一个死循环
    studentName=["小五","小六"]
    while(True):
        print("===========学员管理菜单=======")
        print("1-新增 2-更新 3-删除 4-查询 5-退出")
        print("=============================")
        choice=int(input("请输入菜单编号："))
        if(choice==1):
            print("===========新增学员=======")
            name=input("请输入学员名称：")
            studentName.append(name)
            print("新增后的名单：%s"%studentName)
            # break #调试时使用
        elif(choice==2):
            # pass
            print("===========更新学员=======")            
            print("现在的名单：%s"%studentName)
            nameOld=input("请输入要更新的学员名称：")
            nameNew=input("请输入更新后的学员名称：")
            studentName[studentName.index(nameOld)]=nameNew 
            print("更新后的名单：%s"%studentName)
            # break
        elif(choice==3):
            print("===========删除学员=======")            
            print("现在的名单：%s"%studentName)
            namedel=input("请输入要删除的学员名称：") 
            studentName.remove(namedel)
            print("删除后的名单：%s"%studentName)
            # break
        elif(choice==4):
            print("===========查询学员=======")
            #实现把人员遍历出来并加上编号
            id=1
            for name in studentName:
                id+=1
                print("学员%d号姓名%s"%(id,name))
        elif(choice==5):
            print("===========欢迎再回来=======")
            #终止程序运行
            sys.exit(0)
            # break
        else:
            pass

studentManage()