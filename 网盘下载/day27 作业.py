"""
选课系统项目中涉及到诸多数据与功能，要求引入面向对象的思想对其进行高度整合
# 1、学校数据与功能整合
# 2、课程数据与功能进行整合
# 3、学生数据与功能进行整合
# 4、讲师数据与功能进行整合
# 5、班级数据与功能进行整合
ps：不会写的同学，可以先用普通的方式，先把数据与功能都给写好，再考虑基于面向对象的思想进行整合

数据部分：
    校区的名字：如"老男孩上海校区"
    校区的地址：如"上海虹桥"

    班级名字
    班级所在校区

    学生的学校
    学生的姓名
    学生的年龄
    学号
    学生的性别

    课程名字
    课程周期
    课程价格

    老师的名字
    老师的年龄
    老师的薪资
    老师的等级

功能部分：
    校区创建完毕后，可以为每个校区创建班级

    班级创建完毕后，可以为每个班级创建课程

    学生创建完毕后，学生可以选择班级

    老师创建完毕后，可以为学生打分
"""


class School:
    def __init__(self, name, addr) -> None:
        self.name = name
        self.addr = addr

    def create_class(self, class_name):
        self.class_name = Class(class_name, self.name)

    def func(self):
        print("hello world")


class Class:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school


class Student:
    def __init__(self, school, name, age, stu_id, gender) -> None:
        self.school = school
        self.age = age
        self.name = name
        self.gender = gender
        self.stu_id = stu_id


class Course:
    def __init__(self, name, period, price) -> None:
        self.name = name
        self.period = period
        self.price = price


class Teacher:
    def __init__(self, name, age, salary, level) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.level = level


school = School("29期egon班", "天津")
school.create_class("python全栈课程")
print(school.class_name)
cla = school.class_name
print(cla.name)
print(cla.school)
