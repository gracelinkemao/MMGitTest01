import math
import random
#说明：练习模板01：基础语法+数据类型（含：集合list\set\tuple用法）

#这是注释单行
'''
这是注释多行
'''
# 文档字符串要放在类或方法第一行可执行代码位置
def aaa():
    '''文本注释'''
a=1
print("hello world你好")
#打印文档注释，起帮助文档的作用，说明方法
print(aaa.__doc__) 


# 同一个代码块需要有相同缩进 变量名或字符串过长可以用左斜杠来换行显示，
# 但对于大括号、中括号、小括号的可以直接换行，不借助左斜杠来进行换行
bbb="bbbbbb"
ccc="cccccc"
ddd=bbb+\
    ccc
print(ddd)
list1=[1,2,3,888,
999]
print(list1)

# 输入\出方法
age=12
# age =input("请输入年龄:")
print(age)
print(math.ceil(age))
# print(type(age))  # 打印类型
# print(help(max))  # 打印方案定义查看

# 随机数
print(random.random())# 输出一个0到1之间的随机浮点数
print(random.randint(1, 10))  # 输出一个1到10之间的随机整数

#自然字符串，字符串前加r,则不转义，一般路径时使用
ee="rr\n你好" 
ee2=r"rr\n你好" 
str3=r'D:\Node\node_modules'
print(ee)
print(ee2)
print(str3)
#将一个字符组成的字符串转化为unicode整数编码
#ord()：将python字符串（单个字符）转为unicode整数编码形式
#chr():将python中一个整数（0~0x10ffff之内）
print(ord("A"))
print(chr(97))
#utf‐8编码是可变长的unicode编码，一个汉字占用3个字节长度
print("好".encode("utf‐8"))
#使用decode()进行解码
bb=b'\xd0\xa1'
print(bb.decode("utf‐8"))

#%d:是整数占位符
#%m.nf:是浮点型数据占位符,m表示整数的宽度，n表示小数部分保留的精度
#%s:是字符串类型数据的占位符
str1="今天天气不错，我吃了%d包子"%3  
str2="今天天气不错，我吃了%d包子,还喝了%d瓶水！！！"%(4,2)
str31="今天天气不错，我吃了%d包子,还喝了%d瓶水,总共花了%1.2f元钱！！！"%(4,2,10.5)
str4="今天天气不错，我吃了%s包子,还喝了%s瓶水,总共花了%s元钱！！！"%(4,2,10.5)
print(str1)
print("今天天气不错，我吃了%d包子！！！"%4)

#index():获取索引号的方法
#获取str2中B字符的索引号‐index()
print(str2.index("气"))
#lstrip():裁剪str3左侧的空格，并返回裁剪后的字符串副本
#rstrip():裁剪str3右侧的空格，并返回裁剪后的字符串副本
#strip():裁剪str3两侧的空格，并返回裁剪后的字符串副本
str3="asdfallendd"
print(str3.lstrip())
print(str3)
print(str3.rstrip())
print(str3.strip())
#title()：将字符串首字母大写的方法
str4="abcdefg"
print(str4.title())
print(str4)
#split()：按照指定的分隔符，将一个字符串分隔成多个1
#186‐2198‐4010
str5="186‐2198‐4010"
print(str5.split("‐"))

#===========三、序列的通用运算符
str1="hello"
str2="world!!"
3 #+是拼接功能，拼接两个序列（字符串序列）
print(str1+str2)
#in、notin：成员运算符
str3="ABCDEFG"
print("a" in str3)
print("a" not in str3)
#索引：序列名[索引号]
print(str3[0])
#切片：从大的序列中切出一个小序列
#格式：序列名[start:end:step]
#start:开始的索引号
#end：结束的索引号
#step：步调，默认值是1，如果设置为2则隔一个取一个值；如果是‐1，则倒着挨个取
#左闭右开（可以取到start索引对应的值，但是取不到end对应的值）
print(str3[1:4])
print(str3[1:4:2])
print(str3[::])
print(str3[0:len(str3)])
print(str3[-len(str3):-3])
print(str3[-3:])
print(str3[::-1]) #字符串直接反转
# print(str3[‐1:‐7:‐1])
# print(str3[‐1:‐8:‐1])

# 序列的通用方法
str2="12ABCDE23F44GGG"
#获取序列的长度（元素的个数），个数：len(序列名)
print(len(str1))
#获取最大、最小元素：max(序列名)、min(序列名)
print(max(str2))
print(min(str2))
#获取元素索引:序列名.index(元素值,start,end)
print(str2.index("E"))
print(str2.index("E",4,10))
#substringnotfound
#print(str2.index("E",7,10))
#获取序列中某个元素出现的次数‐count()
print(str2.count("2"))
print(str3[str3.index("BC")::str3.index("BC")+len("BC")])
str4="AB CD EF G"
print(str4.split(" "))
print(str4.split(" ")[-1]) #拆分
print(str4.replace("EF","maomin")) #替换
print(str4.upper()) #字母转换大写
print(str4.lower) #字母转换小写
print(str3[str3.index("EF"):str3.index("EF")+len("EF")]) #将EF提取出来 

#使用print结合input，点位符，换行等多行字符串显示
# print("========\n\
#     姓名：%s\n\
#     职位：%s\n\
#     ======="%(input("输入姓名："),input("输入职位：")))

#字符串find方法(index 通用，在列表和元组中也能用，但find只能用于字符串)
print(str3.index("C"))
print(str3.find("C"))

# ===========四、列表类型
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 创建list1的时候查看一次地址
print(id(list1))
list2 = ["a", "b", "c", "d"]
list3 = [1, 2, 3, "a", "b", 'c', [1, 2, 3], 1, "a"]
print((list1[1]))
list1[1]=20
print((list1[1]))
print(id(list1))
print(list3[2:])
print(list3[2:5])
print(list2+list3)
print(list2*3)
#"a"是list1中的一个元素嘛？
print("a" in list2)
print("a" not in list2)
#index方法,在列表中不支持find方法
print(list2.index("a"))
print(list3.index([1,2,3])) #查找数组不用引号
#5、max()和min()
print(max(list2))
print(min(list2))
#6、count()
print(list2.count("a"))
#7、len():统计列表中元素的个数
print(len(list2))

#列表的常用方法-增删改查的方法 
list1 = [1, 2, 3, "a", "b", 'c', [1, 2, 3], 1, "a"]
#使用索引方式查看列表的元素(分别取第一个和最后一个)
print(list1[0])
print(list1[-1])
print(list1[:])
#列表逆序
print(list1[::-1])
list2=list1[::-1]
print(list2)
list1.reverse()  #逆序反转
print(list1)

# 列表的常用方法-增删改查的方法
#第一种：append方法‐‐追加，给列表的末尾追加元素
#None3 #
print(list1.append("allen"))
#列表是有序的
list1.append("allen")
list1.append("lucy")
list1.append("lily")
#[1,2,3,'a','b','c',[1,2,3],1,'a',12,23,34,'allen']
print(list1)
#第二种：insert方法‐‐插入，就会出现按照指定位置插入元素
#insert(插入位置的索引号，插入的元素)，原索引号位置及其后的元素都要右移动一个索引
list1.insert(1,"allen")
#[1,'allen',2,3,'a','b','c',[1,2,3],1,'a',12,23,34]
print(list1)
#第三种：extend方法‐‐扩展列表，把一个列表中(list2)的元素分别追加到另外一个列表中(list1)
list2=["allen","小王","小李"]
#[1,2,3,'a','b','c',[1,2,3],1,'a',12,23,34,['allen','小王','小李']]
list1.append(list2)
#[1,2,3,'a','b','c',[1,2,3],1,'a',12,23,['allen','小王','小李'],34]
list1.insert(-1,list2)
#[1,2,3,'a','b','c',[1,2,3],1,'a',12,23,34,'allen','小王','小李']
list1.extend(list2)
print(list1)

# 列表的元素删除
#1、pop():弹出，每执行一次pop，默认的总是把列表中的最后一个元素弹出并返回
print(list3.pop())
print(list3)
#pop(index):按照指定的索引号index删除数据并返回该数据
print(list3.pop(1))
print(list3)
#2、dellist3[2]:删除列表中指定的元素
del list3[2]
print(list3)
#3、通过切片的方式删除
list3[3:6]=[]
print(list3)
#4、remove(删除的值)：按照指定的值（列表第一次出现的）删除
list3.remove("b")
#[1,2,3,'b','c',[1,2,3],1,'a',12,23,34]
print(list3)

# 列表元素的修改
list3[0]=10
list3[0:2]=["allen","小王","小张"]
list3[0]=["allen","小王","小张"]
print(list3)

# 列表取最大整型元素
list1=[1,2,3,12,23,34]
print(max(list1))
print(list1.index(max(list1))) 

# 列表增删改查
student_name=["allen","小王","小张"]
student_name.append("小李") #增
print(student_name)
student_name[student_name.index("小李")]="小李2" #改
print(student_name)
# student_name.remove("小李2") #删
del student_name[student_name.index("小李2")]
print(student_name)

#===================五、元组，是有序的。不能被改变（和字符串相似），但其元素可以是可变数据类型，小括号定义且至少有一个逗号
tuple1=(1,2,3,4,5,6)
print(tuple1)
print(tuple1[1])
print(tuple1[:]) #正向切片所有数据
print(tuple1[::-1]) #反着切换所有数据

#元组不能被修改
# tuple1[1]=10
# print(tuple1)
#但元组里可变数据类型的值可以改
tuple1=(1,2,3,["a","c"],4,5,6)
tuple5=(1,2)
tuple1[3][0]="d"
print(tuple1)
# tuple1[3]=["aa","cc"]  #元组不能被修改
tuple2=(1)
print(type(tuple1)) #小括号定义且至少有一个逗号才能被识别为元组
print(type(tuple2))
print(tuple1+tuple5)
print(tuple1 *2 )
print(1 in tuple1)

print(len(tuple1))
print(max(tuple5))
print(min(tuple5))
print(tuple1.index(2))
print(tuple1.count(2))

#===================六、Set集合，无序，不重复元素，用()或{}来创建，使用{}时不能为空
set1={1,2,3,4,5,3,2}
print(set1)
set2={2,5,8,9}
print(set1-set2) #差集
print(set1|set2) #并集
print(set1&set2) #交集

#===================七、字典（dict），映射类型的数据结构，（键:值对组成元素）
# 空字典：dict1={}
# 非空字典：dict2={"邓超":"孙俪","郑凯":"苗苗","黄晓明":"baby","文章":"马伊利"}
# 在字典中不能使用索引，可以通过键来或者值：dict2["邓超"]
dict2={"邓超":"孙俪","郑凯":"苗苗","黄晓明":"baby","文章":"马伊利"}
print(dict2["邓超"]) 
dict2["邓超"]="孙俪2"
print(dict2["邓超"]) 
print(dict2.keys()) #获取字典中所有的键组成是列表
print(dict2.values()) #获取字典中所有的值组成是列表
print(dict2.items()) #返回的是键值对 
# print(dict2.clear()) #清空字典

# get()：通过键获取值(熟练使用)
print(dict2.get("文章"))
print(dict2["文章"])
#6、给字典增加元素
dict2["杜江"]="霍思燕"
print(dict2)
dict3={"陈小春":"应采儿"}
#采用update的方法
dict2.update(dict3) # 将dict3更新到dict2
print(dict2)
#{'Jim':'a','Mary':'a','Rose':'a','Tom':'a','Jack':'a'}
dict4={}.fromkeys({'Tom','Jim','Mary','Tom','Jack','Rose'},'a')
print(dict4)

#练习题 ===================列表
L=['a','b','c']
L1=[1,2,'a','b']
L.append("d")
print(L)
L.insert(2,"e")
print(L)
L.append(L1) #将L1整个作为一个元素追加
L.extend(L1) #将L1里每个元素分别作为一个元素追加到L
L.insert(0,"f") #L的开头追加
print(L)
print(len(L))
print(L.pop()) #删除最后一个元素 L.pop(-1)
print(len(L))
del L[-1] #删除最后一个元素 del L[len(L)-1] 
del L[len(L)-1] 
print(L) 
#删除a元素 ['f', 'a', 'b', 'e', 'c', 'd', [1, 2, 'a', 'b'], 1]
L.remove("a")
print(L) 
L[5].remove("a")
print(L) 
L2=[1,2,4,3]
L2.sort() #排序 顺序
L2.sort(reverse=True) #排序 倒序
print(L2) 
print(L2[0]) #排序后取第一个就是最大\最小
print(L2[-1])
print(max(L2))
print(min(L2))
# 对排序好的列表进行逆序排列
# 方法1 ：直接排序 倒序
# L2.sort(reverse=True) 
# 方法2 ：先顺序后，再从后往前输出
L2.sort()
print(L2[::-1])

#练习题  ===================字典diction
dict6={"邓超":"孙俪","郑凯":"苗苗","黄晓明":"baby","文章":"马伊利"}
#增加key 方法1
dict6["a"]="b" 
#增加key 方法2 update
dict7={"c":"d"}
dict6.update(dict7)
print(dict6)
# 获取所有KEY值
dict6.keys()
# 获取所有value值
dict6.values()
# 获取所有键值对
dict6.items()
# 删除KEY为a的值
dict6.pop("a")
print(dict6)

#数据类型转换
#在python的使用中，存在需要将一些数据转换为其他类型的场景。                                    
#只需要使用该数据类型作为方法名使用即可转化。                                                  
#方法名有：int(str)、str(其他类型)、list(其他类型)、tuple(其他类型)等                          
#input():是可以将键盘录入的数据转为python字符串格式                                            
#1、需求：希望将键盘录入的数据转换数据类型为整性数据（int）                                    
#处理方式：直接使用int作为方法名转换即可，int(str字符串)                                       
#str字符串:必须是数字类型的字符串，"1233",'222'                                                
#ValueError: invalid literal for int() with?base?10: 'ab'                                      
#age=int(input("请输入你的年龄："))                                                          
##<class 'str'>                                                                              
#print(type(age))                                                                             
##TypeError:%dformat:anumber is required, not str           
age=int("213")                             
print("我的年龄是：%d"%age)                                                                  
                                                                                               
#2、str(其他类型)：将其他数据类型转为字符串                                                   
#将整数转为字符串                                                                             
student_id=str(12345)                                                                        
print(type(student_id))                                                                        
                                                                                               
#将列表转为字符串                                                                             
student_name=str(["allen","lucy","李雷","韩梅梅"])                                           
print(type(student_name))                                                                      
print(student_name)                                                                            
                                                                                                                                                                                       
#3、eval():将一个字符串表达式转为对象28 #"print('hello?world')"‐‐‐>print('hello?world')
str1="print('hello world')"                                                                  
eval(str1)                                                                                                                                                                                   
#4、list():将其他类型序列转为列表                                                             
str2="abcdefg"                                                                               
list1=list(str2)                                                                             
print(type(list1))                                                                             
print(list1)                                                                                   
                                                                                               
tuple1=(1,2,3,4,5)                                                                           
list2=list(tuple1)                                                                           
print(type(list2))                                                                             
print(list2)                                                                                   
                                                                                               
#5、字符串和列表转元组的方法（tuple()）‐‐课下练习                                           
#6、dict():将一个元组转为字典                                                                 
#{'name':'allen','name1':'allen1'}                                                         
dict1=dict([("name","allen"),("name1","allen1")])                                            
print(type(dict1))                                                                             
print(dict1)                                                                                   



