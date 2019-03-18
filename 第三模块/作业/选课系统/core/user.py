# encoding: utf-8
import pickle
from bin.metas import test_log, Base
from .school import Course


class User(Base):
    def __init__(self, name, password, age, sex):
        super().__init__(name)
        self.password = password
        self.age = age
        self.sex = sex


class Student(User):

    def registere(self):
        pass

    def pay_tuition(self):
        pass

    def choose_class(self):
        pass


class Teacher(User):

    def __init__(self, name, password, age, sex, school):
        super().__init__(name, password, age, sex)
        self.school = school

    def manage_classes(self):
        pass

    def choice_classes(self):
        pass

    def query_students_info(self):
        pass

    def modify_mark(self):
        pass


class Administrator(User):
    def add_teacher(self, shcool, *args):
        name, password, age, sex = args
        Teacher(name, password, age, sex, shcool)

    def add_courses(self, *args):
        Course(*args)

    def add_class(self, *args):
        name, = args
