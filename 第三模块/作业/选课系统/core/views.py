# encoding: utf-8
import pickle
from .user import Administrator,Teacher,Student
from .school import School, Classes, Course
school_beijing = pickle.load(open('db/school/北京校区','rb'))
school_shanghai = pickle.load(open('db/school/上海校区','rb'))
# print(school_beijing.__dict__)
# print(school_shanghai.__dict__)

class BaseView(object):
    def __init__(self,current_user,passwd):
        if current_user.password == passwd:
            self.user = current_user
        else:
            print("密码输入错误")
            exit()


class TeacherView(BaseView):
    pass

class StudentView(BaseView):
    pass

class ManageView(BaseView):

    def add_teacher(self):
        pass

    def add_class(self):
        pass

    def add_course(self):
        pass

    def manage_view(username,passwd):
        pass
        # current_user = pickle.load(open('db/administrator/%s'%username,'rb'))
        # if current_user.password == passwd:
        #     print(
        #     """
        #     1.创建讲师
        #     2.创建班级
        #     3.创建课程
        #     4. 退出
        #     """)
        #     choice = input("输入序号选择功能").strip()
        #     if choice == '1':
        #         input_list = [input(i+':').strip() for i in ('姓名','密码','年龄','性别')]
        #         current_user.add_teacher(*input_list)
        # else:
        #     print('密码错误')



