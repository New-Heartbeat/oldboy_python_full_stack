# 如果在局部想要修改全局的名字对应的值（不可变类型），需要用global
# x = 111
# def f1():
#     global x
#     x = 222
# f1()
# print(x)

# l = [111, 222]
# def f2():
#     l.append(333)
# f2()
# print(l)

# nonlocal（了解）：修改函数外层函数包含的名字对应的值（不可变类型）
x = 0
def f1():
    # global x
    x = 11
    def f2():
        # global x
        nonlocal x
        x = 22
    f2()
    print('f1内的x：', x)
f1()
print(x)