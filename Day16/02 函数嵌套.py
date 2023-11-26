# 函数嵌套
# 1、函数的嵌套调用：在调用一个函数的过程中又调用其他函数


# 2、函数的嵌套定义：在函数内定义其他函数
# def f1():
#     def f2():
#         pass

# 圆形
def circle(radius, action=0):
    from math import pi

    # 求周长：2*pi*radius
    def perimiter(radius):
        return 2*pi*radius

    # 求面积：pi*(radius**2)
    def area(radius):
        return pi*(radius**2)

    if action == 0:
        return perimiter(radius)
    else:
        return area(radius)

res = circle(1, 0)
print(res)

