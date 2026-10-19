#说明：练习模板06:面向对象+模块和异常处理+IO处理 之  IO处理
import time
import sys
import os

import csv
import json
import xlrd
import xlwt
# 一、open的使用（掌握）
# 文件流对象名 = open(文本文件全路径, 读写模式，指定字符集)
# 文件流对象名：就是一个变量名，后续对文件的处理就是对这个对象的处理
# 文本文件全路径：文件在磁盘的目录和文件名，一般采用自然字符串显示
# 读写模式：读取文件、写文件、读写文件、追加写入文件、以字节码的形式读写
# r ： 只读，不能写入，必须文件已经存在
# w：只写，只能写入，覆盖写入，没有文件它会创建文件并写入
# a：追加写入，在原文件的末尾继续写入
# r+ ： 读写模式，文件必须存在
# w+：读写模式，可以不存在，如果不存在则创建并写入
# b：字节码（二进制）读写，用于读取超文本（图片、html、视频等）,rb\wb:字节的读写

# IO：input-输入，output-输出
# 输入：只从键盘、文件、数据结构读取出数据
# 输出：从程序中将数据写入到终端、文件、数据结构等
# 本部分内容主要是对文件的IO处理（text、csv、json等）
# 一、键盘和终端
# input() : 从键盘获取数据到程序，python的标准输入，读取的一个字符串
# print() :  输出数据到终端

#========一、文件IO-（text文本文件）
# 读文件：open的使用（掌握）:文件流对象名 = open(文本文件全路径, 读写模式，指定字符集) 
# 读取路径：path1=r"D:\Project1\hg_auto_test\pythonTest01\demo\demo-test5-class\test-files\allen.txt"
path1=os.path.abspath(os.path.dirname(__file__))+r"\test-files\allen.txt" #__file__：动态获取当前文件所在目录的绝对值  
print(path1)  
list2=["a\n","b\n","c"]

#=== 1、with语句实现文件的打开并读写 【常用方法】
# 更安全，可以帮自动关闭文件对象。对于读写模式为b的不用加encoding
with open(path1,"w",encoding="utf-8") as f3:
    print("练习")
    # print(f3.read())
    # print(f3.readlines()) 
    print(f3.writelines(list2)) #write(str)
"""
# ===2、读文件 
f=open(path1,"r",encoding="utf-8") #打开文件
# print(f.read()) #f.read(size):读取指定size个数读取，不指定全部读 
# print(f.readline())  #不指定size，读取一行，指定size，则读取指定size字节长度的数据
# print(f.readlines()) #一次性把所有的行数据读取出，将其每行数据作为元素存储在一个列表中
list1=[]
for i in f.readlines():
    print(i)
    list1.append(i) #读取文件保存到LIST中
    time.sleep(1)# 定时每隔开一秒，刷新一行
print(list1)
f.close() #关闭文件


#=== 3、写文件
# write(str):将指定的字符串str写入到文件中,是覆盖写入
# writelines():参数是一个列表，把列表的元素作为行写入，如果需要换行，每个元素结尾要带\n字符
f2=open(path1,"w",encoding="utf-8") #打开文件的模式就是w （覆盖写入）或者a（追加写入）
# f2.write("覆盖写入TEST") #将指定的字符串str写入到文件中,是覆盖写入
f2.writelines(list2) #参数是一个列表，把列表的元素作为行写入，如果需要换行，每个元素结
f.close() #关闭文件

"""


#========二、文件IO-（CSV本文件）
# 创建excel文件并编辑数据，另存为csv文件（utf8格式，逗号分隔）
# 创建text文本文件，修改后缀名为.csv，超级记事本软件(notepad)将编码改为utf-8
path2=os.path.abspath(os.path.dirname(__file__))+r"\test-files\allen2.csv" #__file__：动态获取当前文件所在目录的绝对值  
print(path2)  
# ===2、读文件 
with open(path2,"r+",encoding="utf-8") as f5:
    data=csv.reader(f5)
    for d in data:
        print(d)  #读第一列d[0]
# ===3、写入csv 
# 采用python中的csv模块的写入方法writer来实现。
data6=[1,"allean7","6666666"] # 写入的时候也是按照列表写入的，分隔符默认也是使用逗号
data6=[
    [11,"allean71","6666661"],
    [12,"allean72","6666662"],
    [13,"allean73","6666663"]
]
with open(path2,"a+",encoding="utf-8",newline="") as f6:  #newline=""则不默认回车
    writerSCV=csv.writer(f6,dialect="excel")
    #  writerSCV.writerow(data6)   #写入一行数据
    writerSCV.writerows(data6)    #写入多行数据


#========三、文件IO-（JSON文件）
# 1）创建txt文件，重命名为xx.json，将其编码集改为utf-8
# 2）按照下面的个数输入数据即可json数据的格式: []、{}来定义，其中字符串使用 双引号 定义，具体的数据使用{}
# 定义定字典，他们之间是可以相互嵌套。
# 在{}的最后一个元素后面不需要逗号，其他的都需要加,在[]的最后一个元素后面也不需要逗号，其他的需要加
# load() : 参数是json文件,将json文件中的数据结构读取为代码中列表和字典。
# loads()：参数是字符串，将字符串（必须是由[]、{}、""）转为字典和列表形式。
path3=os.path.abspath(os.path.dirname(__file__))+r"\test-files\allen5.json" #__file__：动态获取当前文件所在目录的绝对值  
print(path3)  
# ===2、读文件 
# load()
with open(path3,"r+",encoding="utf-8") as f6:
    data6=json.load(f6)
    # print(data6)
    for d in data6:
        print(d)
        # print(d["name"]) 
        # print(d["name"][0])  拿字典里姓名的第一个

# loads() json这个模块还能处理字符串,将字符串转为JSON字典
str1="abdc"
str3='{"name":"lily","age":28,"sex":"男","id":"1333984010","address":["陕西省","西安市","高新区"]}'
data1=json.loads(str3)
print(data1)
print(type(data1))

#=== 3、写文件
# 使用dump函数直接将list列表写入json文件
# json.dump(list1,f,indent=1,ensure_ascii=False)
with open(path3,"w",encoding="utf-8",newline="\r\n") as f7:  #newline="\r\n" 换行写入
    # 定义数据
    list7=[
    {"name":"韩昌佩","age":28},
    {"name":"allen","age":28},
    {"name":"allen","age":28}
    ]
# 使用jumps转化为字符串，并通过wirte方法写入json文件
    data7=json.dumps(list7,indent=1,ensure_ascii=False)
    f7.write(data7)


#========四、文件IO-（EXCEL文件）
# 读excel的模块是xlrd，写excel用xlwt模块，因为是第三方的模块，需要安装后再使用。
# xlrd在1.2.0之前支持xlsx的excel文件格式的.安装xlrd模块: pip install xlrd
# xlrd在2.0.0之后支持xls格式
path4= os.path.abspath(os.path.dirname(__file__))+r"\test-files\allen6.xls" #__file__：动态获取当前文件所在目录的绝对值  
# f8=xlrd.open_workbook(r"e:\allen.xlsx")
f8=xlrd.open_workbook(path4)
# 2、选择工作簿中的一个sheet页，获取其中的表格数据
sheet1=f8.sheet_by_index(0)
# sheet1=f8.sheet_by_name("Sheet1")
# sheet1=f8.sheets()[1]
# 3、获取sheet1中单元格数据(第二行第二列)
rowData=sheet1.row_values(1)
# 获取单元格数据
print("第二行第二列数据为:%s"%rowData[1])
cellData=sheet1.cell_value(1,1) # cell_value(行索引号,列索引号)，索引号都是从0开始的
print("第二行第二列数据为:%s"%cellData)
# 4、遍历获取所有的数据（所有行和所有单元格）
# 前提是知道sheet1中表有多少行多少列
# sheet1.nrows：返回sheet1的行数的字段
# sheet1.ncols：返回sheet1的列数的字段
rows=sheet1.nrows
cols=sheet1.ncols
# i就是行号的索引（第一行的索引就是0）
# for i in range(0,rows):
#     data = sheet1.row_values(i)
#     print(data[1])

# 所有单元格
for n in range(0,rows):
    for m in range(0,cols):
        data = sheet1.cell_value(n,m)
        print(data)

#=== 3、写入excel文件
# 安装xlrd模块: pip install xlwt
path5= os.path.abspath(os.path.dirname(__file__))+r"\test-files\allen6.xls" #__file__：动态获取当前文件所在目录的绝对值  
# 2、打开excel工作簿文件
f9=xlwt.Workbook(encoding="utf-8")
# 3、指定写入数据的sheet页
sheet=f9.add_sheet("Sheet1")
# 4、写入第二行第二列中
# sheet.write(行索引，列索引，值)
# sheet.write(1,1,"你好")
# 如何写入一行数据呢
# rowData=["name","password","id","address"]
# 遍历一行中列的索引号col
# for col in range(0,len(rowData)):
#     sheet.write(0,col,rowData[col])

# 写入多行数据
rowData=[
    ["name","password","id","address"],
    ["name1","password1","id1","address1"],
    ["name2","password2","id","address2"],
    ["name3","password3","id","address3"]
    ]

row = len(rowData)
for r in range(0,row):
    for c in range(0,len(rowData[r])):
        sheet.write(r,c,rowData[r][c])

# 5、写完之后别忘了保存文件(将内存中的数据写入到文件中)
# f9.save(r"e:\allen.xls")
f9.save(path5)


#========五、文件IO-（图片文件）
# f10=open(r"e:\data\123.jpg","rb") #使用 rb 格式读
# print(f10.read())
# f10.close()


#======练习:文件增删除改查======
def __studentManage(): 
    path6=os.path.abspath(os.path.dirname(__file__))+r"\test-files\studentInfo.csv"
    #1、写入CSV
    # title=["id","name","sex","date","class"]
    # students=[
    #     ["001","张三1","男","2025-02-01","class1"],
    #     ["002","张三2","女","2025-02-02","class2"]
    #     ]
    # with open(path6,"w+",newline="\n",encoding="utf-8") as f11: #初始化的时候覆盖写入更合适 w+
    #     writer=csv.writer(f11)
    #     writer.writerow(title)
    #     writer.writerows(students)

    #2、读取
    with open(path6,"r",encoding="utf-8") as f12: 
        data12=csv.reader(f12)
        for student in data12:
            #直接输出带TITLE
            # print(student)
            #去掉首行显示
            if student[0] !="id":
                print(student)


    # 3、写入一条新数据，学号不能重复.则先把数据读取,定义一个变量,再判断
    newId="003"
    flag=False
    with open(path6,"r",encoding="utf-8") as f13:
        data12=csv.reader(f13)
        for student in data12:
                # 判断新学号是否与现有重复
            if student[0]==newId:
                flag=True
                print("学号重复，请重新填写")
                break
    if flag==False:
        print("继续处理")
        newName="张三3" #input("请输入姓名:")
        newSex="男"
        newDate="2025-02-03"
        newClass="class3"
        newStudent=[newId,newName,newSex,newDate,newClass]
        with open(path6,"a+",newline="\n",encoding="utf-8") as f11: #追加写入a+
            writer=csv.writer(f11)
            writer.writerow(newStudent)

    #4、更新
    newName="张三3"
    tempStudents=[]
    with open(path6,"r",encoding="utf-8") as f12: 
        data12=csv.reader(f12)
        for student in data12:
            tempStudents.append(student) #将查询的所有数据赋值以列表
    #处理列表
    indexcount=-1
    index=0
    for student in tempStudents: 
        indexcount+=1
        if student[1]==newName:
            #记录需要更新的那一行的索引号。默认修改出现的第一个查询到的信息
            index=indexcount
            break
    if index!=0:
        newId=tempStudents[index][0]
        newName="张三5" #input("请输入姓名:")
        newSex="男"
        newDate="2025-02-05"
        newClass="class5"
        newStudent=[newId,newName,newSex,newDate,newClass]
        tempStudents[index]=newStudent
        with open(path6,"w",newline="\n",encoding="utf-8") as f11:  
            writer=csv.writer(f11)
            writer.writerows(tempStudents)
    else:
        print("没找到需要更新的人员相关信息")

    #5、删除 （按学号删除）
    stuId="001"
    tempStudents=[]
    with open(path6,"r",encoding="utf-8") as f12: 
        data12=csv.reader(f12)
        for student in data12:
            tempStudents.append(student) #将查询的所有数据赋值以列表
    #处理列表
    indexcount=-1
    index=0
    for student in tempStudents: 
        indexcount+=1
        if stuId in student:
            #记录需要删除的那一行的索引号。
            index=indexcount
            break
    if index!=0: 
        tempStudents.pop(index)
        with open(path6,"w",newline="\n",encoding="utf-8") as f11:  
            writer=csv.writer(f11)
            writer.writerows(tempStudents)
    else:
        print("没找到需要删除的人员相关信息")


#调用练习的方法
if __name__ == '__main__':
    __studentManage()
    