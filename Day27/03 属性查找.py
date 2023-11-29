class Student:
    stu_school = "oldboy"
    count = 0

    def __init__(obj, x, y, z) -> None:
        Student.count += 1

        obj.stu_name = x
        obj.stu_age = y
        obj.stu_gender = z

    def tell_info(obj):
        print(
            "学生信息 姓名：%s 年龄：%s 性别：%s"
            % (
                obj.stu_name,
                obj.stu_age,
                obj.stu_gender,
            )
        )

    def set_info(obj, x, y, z):
        obj.stu_name = x
        obj.stu_age = y
        obj.stu_gender = z


# 属性访问
# 一、类属性与对象属性
# 1.在类中定义的名字，都是类的属性，类有两种属性：数据属性和函数属性
# 可以通过__dict__访问属性的值，但Python提供了专门的属性访问语法
# print(Student.__dict__["stu_school"])
# print(Student.stu_school)
# 可以通过该访问方法对属性进行增加、修改
Student.new_attr = "新属性"
print(Student.new_attr)
Student.new_attr = "新属性-new"
print(Student.new_attr)

# 2.对象属性
# 访问方法和类一样
stu1_obj = Student("egon", 18, "male")
# print(stu1_obj.stu_school)

# 二、属性查找顺序与绑定方法
# 对象的名称空间里只存放着对象独有的属性，而对象们相似的属性是存放于类中的。
# 对象在访问属性时，会优先从对象本身的__dict__中查找，未找到，则去类的__dict__中查找
# print(stu1_obj.__dict__)
# print(Student.__dict__)

# 1.类的数据属性
# 类的数据属性是共享给所有对象用的，指向相同的内存地址
stu2_obj = Student("alex", 32, "female")
# Student.stu_school = "OLDBOY"
# print(stu1_obj.stu_school)
# print(stu2_obj.stu_school)
# print(Student.stu_school)

# print(stu1_obj.count)
# print(stu2_obj.count)
stu3_obj = Student("Bob", 0, "male")
# print(stu1_obj.count)

# 2、类的函数属性
# 类的函数属性是绑定给对象用的，虽然所有对象指向的都是相同的功能
# 但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同
# print(Student.tell_info)
# print(stu1_obj.tell_info)
# print(stu2_obj.tell_info)

# 类调用自己的函数必须严格按照函数的定义传参
Student.tell_info(stu1_obj)


# 绑定到对象的方法特殊之处在于：谁来调用绑定方法就会将谁当做第一个参数自动传入
stu1_obj.tell_info()  # Student.tell_info(stu1_obj)
