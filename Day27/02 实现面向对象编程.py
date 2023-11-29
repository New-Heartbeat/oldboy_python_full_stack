# 一、先定义类
# 类是对象相似数据与功能的集合体
# 所以类体中最常见的是变量与函数的定义，但是类体中是可以包含任意其他代码的
# 注意：类体代码是在类定义阶段就会立即执行，会产生类的名称空间
class Student:
    # 1、变量的定义
    stu_school = "oldboy"

    # 2、功能的定义
    def tell_info(stu_obj):
        print(
            "学生信息 姓名：%s 年龄：%s 性别：%s"
            % (
                stu_obj["stu_name"],
                stu_obj["stu_age"],
                stu_obj["stu_gender"],
            )
        )

    def set_info(stu_obj, x, y, z):
        stu_obj["stu_name"] = x
        stu_obj["stu_age"] = y
        stu_obj["stu_gender"] = z

    def test():
        pass

    # print('=======>')


# print(Student.__dict__)
# 属性访问的语法
print(Student.stu_school)  # Student.__dict__['stu_school']
print(Student.__dict__["tell_info"])  # Student.__dict__['tell_info']

# 二、再调用类产生对象
stu1_obj = Student()
stu2_obj = Student()
print(stu1_obj.__dict__)
stu1_obj.stu_name = "egon"  # stu1_obj.__dict__["stu_name"] = "egon"
stu1_obj.stu_age = 18
stu1_obj.stu_gender = "male"
print(stu1_obj.__dict__)
print(stu1_obj.stu_school)


# 解决方法1
def init(obj, x, y, z):
    obj.stu_name = x
    obj.stu_age = y
    obj.stu_gender = z


stu3_obj = Student()
init(stu3_obj, "alex", 20, "female")
print(stu3_obj.__dict__)


# 解决方法2
# 在创建类的时候就添加__init__方法
# 它会在创建对象（调用类阶段）自动触发
class Student:
    def __init__(obj, x, y, z) -> None:
        obj.stu_name = x
        obj.stu_age = y
        obj.stu_gender = z

        # return None  # 返回None以外的结果会报错


# 调用类的过程又称之为实例化，发生了三件事
# 1、先产生一个空对象
# 2、自动调用类中的__init__方法，将空对象与调用类时括号内传入的参数一同传给该方法
# 3、返回初始完的对象
stu4_obj = Student("Mary", 50, "female")
print(stu4_obj.__dict__)
