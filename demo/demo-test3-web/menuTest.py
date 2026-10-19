# 使用python中的下面技术实现功能：
# 1、使用csv文件存储学员信息（姓名、性别、出生日期、班级、学号（不允许重复））
# 2、对列表进行增、删、改、查
# 3、通过input方法输入信息
# 4、通过if语句判断选项菜单（比如1表示增加新学员功能）
# 5、每次增删改的数据都要存入csv文件
# 6、将代码封装一个死循环中（如果选择了5菜单，则终止死循环）
# 7、更新功能可以二选一：按照学号、姓名查询
# 8、删除功能可以二选一：按照学号、姓名删除
# 9、查询功能可以二选一：按照学号、姓名查询


# 导入csv包
import csv
import sys

# 把现有的功能封装在一个方法中
# 把所有的代码封装到一个类中(参数的初始化,学员信息管理的功能)
# 定义存储数据的csv文件全路径（后续的读写动作都是对这个文件的操作）
class students():
    # 初始化的过程,封装在构造方法中
    def __init__(self):
        self.dataPath = r"D:\Project1\hg_auto_test\files\studentInfo.csv"
        self.title = ["id","name","sex","date","class"]
        self.students = [
            ["00001","张三","男","1990","001"],
            ["00002","李四","男","1991","003"],
            ["00003","王五","女","1992","001"],
            ["00004","赵六","男","1993","002"]
        ]

        # 用w+更合适，初始化的时候覆盖写入更合适
        with open(self.dataPath,"w+",newline="\n",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.title)
            writer.writerows(self.students)

    # 定义数据：
    def  studentManage(self):
        # 一开始执行代码，要先进行数据的初始化（要将初始数据写入到csv文件）
        while True:
            print("==================学生信息管理===================")
            print("1-增加    2-更新    3-删除    4-查询      5-退出")
            print("================================================")
            # 选择选型
            choice = int(input("请输入菜单选项："))
            if choice==1:
                print("==================增加学生信息===================")
                newId = input("请输入一个新学员的学号:")
                # 希望往csv文件中写入一条新的数据,(学号不能重复)
                # 只能把数据读取出来进行判断,定义一个变量来表示重复的标识  
                flag = False
                with open(self.dataPath,"r",encoding="utf-8") as f :
                    data = csv.reader(f)
                    for student  in data:
                        # 新输入的学号是否与文件中现有的学号相同
                        if(student[0]==newId):
                            flag = True
                            print("输入新学员学号重复啦!!")
                            break
                if flag==False:
                    newName = input("请输入一个新学员的姓名:")  
                    newSex = input("请输入一个新学员的性别:")  
                    newDate = input("请输入一个新学员的日期:")  
                    newclass = input("请输入一个新学员的班级:")  
                    newStudent = [newId,newName,newSex,newDate,newclass]
                    # 一定采用a追加写入数据
                    with open(self.dataPath,"a",newline="\n",encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow(newStudent)
                print("================================================")        
            elif choice==2:
                # 更新csv文件中的学员信息
                # 更新\删除都是对源文件中数据的处理,需要读出所有数据\处理完成后再写回去
                # 按照姓名判断来更新数据
                print("==================更新学生信息===================")
                newName= input("请输入要更新的学员姓名")
                # 定义一个变量来临时存储csv文件中的数据
                tempStudents = []
                # 读取文件数据
                with open(self.dataPath,"r",encoding="utf-8") as f:
                    data = csv.reader(f)
                    for student in data:
                        tempStudents.append(student)
                # 现在要处理列表,先要找到列表中的一个学生信息是newname,并且要记录这个学生所在列表中位置
                indexStudent = -1
                index = 0
                for student in tempStudents:
                    indexStudent += 1
                    if(student[1]==newName):
                        # 记录更新的那一行的索引号,默认修改出现的第一个查到的信息
                        # 想改出现的第一个,就加break,不加break就该最后一条
                        index = indexStudent
                        break
                
                # 判断是否有要更新的信息,有的话就新的值替换一下
                if index!=0:
                    newId = tempStudents[index][0]
                    newName = input("请输入一个新学员的姓名:")  
                    newSex = input("请输入一个新学员的性别:")  
                    newDate = input("请输入一个新学员的日期:")  
                    newclass = input("请输入一个新学员的班级:")  
                    newStudent = [newId,newName,newSex,newDate,newclass]
                    tempStudents[index] = newStudent
                    # 覆盖写入
                    with open(self.dataPath,"w",newline="\n",encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerows(tempStudents)
                else:
                    print("没有找到你要更新的那个人名!!")

                print("================================================")
            elif choice==3:
                # 删除数据的思路和更新一致的(按学号删除)
                print("==================删除学员学生信息查询==================")
                tempStudents = []
                with open(self.dataPath,"r",encoding="utf-8") as f:
                    data = csv.reader(f)
                    for student in data:
                        tempStudents.append(student)
                
                #输入一个要删除的学员id
                idStu = input("请输入要删除学员的ID号:")
                indexStudent = -1
                index = 0
                for student in tempStudents:
                    indexStudent += 1
                    if idStu in student:
                        index = indexStudent
                        # 遇到要删除的id的话就退出即可
                        break
                
                # 判断index值是否为0
                if index !=0:
                    tempStudents.pop(index)
                    with open(self.dataPath,"w",newline="\n",encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerows(tempStudents)
                else:
                    print("没有找到要删除的学员ID,重新输入!!")
                print("================================================")

            elif choice==4:
                print("==================学生信息查询==================")
                # 你希望打印出title吗？
                # 直接读取文件
                with open(self.dataPath,"r",encoding="utf-8") as f:
                    data = csv.reader(f)
                    for student in data:
                        # 直接输出student就是带title的
                        # print(student)
                        # 去掉首行
                        if student[0] != "id":
                            print(student)
                
                print("================================================")
            elif choice==5:
                print("==================退出学生信息管理================")
                print("提示：欢迎再次使用学生信息管理系统！！")
                # 终止程序运行
                print("================================================")
                sys.exit(0)
            else:
                print("==================学生信息管理===================")
                print("提示：你选择的菜单选项错误，不在范围内，请选择1~5！！")
                print("================================================")

# 到这我们就把面向过程编程改为了面向对象编程了
if __name__=="__main__":
    # studentManage()
    qianfengTest = students()
    qianfengTest.studentManage()
    