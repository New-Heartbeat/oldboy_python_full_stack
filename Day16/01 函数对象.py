# 精髓：可以把函数当成变量去用
# func=内存地址
def func():
    print('from func')

print(func)
# 1、可以赋值
# f = func
# print(f, func)
# f()

# 2、可以当作函数的参数传入
# 3、可以当作另一个函数的返回值
# def foo(x):
#     return x
# res = foo(func)
# print(res)

# 4、可以当作容器类型的一个元素
# l = [func, 222]
# print(l)
# l[0]()




