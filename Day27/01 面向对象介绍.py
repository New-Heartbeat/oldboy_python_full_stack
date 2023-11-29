"""
面向过程：
    核心是“过程”二字

    过程的终极奥义就是将程序流程化
    过程是“流水线”，用来分步骤解决问题

面向对象：
    核心是“对象”二字

    对象的终极奥义就是将程序“整合”
    对象是“容器”，用来盛放数据与功能的

    类也是“容器”，该容器用来存放同类对象共有的数据与功能
"""
# 程序=数据+功能
# 学生的容器=学生的数据+学生的功能
# 课程的容器=课程的数据+课程的功能


# 学生的功能
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


stu_obj = {
    "stu_name": "egon",
    "stu_age": 18,
    "stu_gender": "male",
    "tell_stu_info": tell_info,
    "set_info": set_info,
}

tell_info(stu_obj)
