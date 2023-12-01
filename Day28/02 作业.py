class School:
    name = "oldboy"

    def __init__(self, nick_name, addr) -> None:
        self.nick_name = nick_name
        self.addr = addr
        self.classes = []

    def check_classes(self):
        for class_obj in self.classes:
            print("==================================")
            class_obj.class_info()

    def school_info(self):
        print(f"校区名称：{self.nick_name} 校区地址：{self.addr}")
        self.check_classes()


class Classes:
    def __init__(self, name, school) -> None:
        """initial

        Args:
            name (_type_): _description_
            school (School object): _description_
        """
        self.name = name
        self.school = school
        self.courses = []
        school.classes.append(self)

    def relate(self, course_obj):
        self.courses.append(course_obj)

    def class_info(self):
        print(f"班级名称：{self.name} 班级校区：{self.school.nick_name}")
        self.check_courses()

    def check_courses(self):
        for course in self.courses:
            course.course_info()


class Course:
    def __init__(self, name, period, price) -> None:
        self.name = name
        self.period = period
        self.price = price

    def course_info(self):
        print(f"课程名：{self.name} 课程周期：{self.period} 课程价格：{self.price}")


school_obj1 = School("魔都校区", "上海")
class1 = Classes("脱产第15期", school_obj1)
class2 = Classes("脱产第16期", school_obj1)
# school_obj1.check_classes()

python_course = Course("python", "12mons", 20000)
html_course = Course("html", "6mons", 10000)
sql_course = Course("sql", "2mons", 5000)
# python_course.course_info()

class1.relate(python_course)
class1.relate(html_course)
# class1.check_courses()
# class1.class_info()
class2.relate(sql_course)
class2.relate(html_course)
school_obj1.school_info()
