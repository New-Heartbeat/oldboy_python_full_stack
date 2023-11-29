"""
一、什么是装饰器
    器指的是工具，可以定义成函数
    装饰指的是为其他事物添加额外的东西点缀

    合到一起的解释：
        装饰器指的定义一个函数，该函数是用来装饰其他函数的（为其他函数添加额外的功能）

二、为何要用装饰器
    开放封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的是对修改源代码是封闭的

    装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能

三、如何用
"""
import time

# def index(x, y):
#     time.sleep(2)
#     print('welcome %s %s to index page' % (x, y))

# 增加计时功能
# 方案一：修改源代码
# def index(x, y):
#     start = time.time()
#     time.sleep(2)
#     print('welcome %s %s to index page' % (x, y))
#     stop = time.time()
#     print(stop - start)
# index(111, 222)

# 方案二：代码冗余，每次调用都需要加上这几行代码
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)

# 方案三：修改了原函数的调用方式
# def wrapper(x, y):
#     start = time.time()
#     index(x, y)
#     stop = time.time()
#     print(stop - start)
# wrapper(111, 222)
# # 优化
# def wrapper(*args, **kwargs):
#     start = time.time()
#     index(*args, **kwargs)
#     stop = time.time()
#     print(stop - start)
# wrapper(111, 222)

# 方案四：用闭包函数
# def index(x, y, z):
#     time.sleep(2)
#     print('index %s %s %s' % (x, y, z))
# print(index)
# def outter(func):
#     # func=index的内存地址
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#     return wrapper
#
# index = outter(index) # index=wrapper的内存地址
# print(index)
# index(1, 2, 3)
# index(1, z=3, y=2)

# 当需要拓展的函数有多个时
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, *kwargs)
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper

# 在被装饰对象正上方的单独一行写 @装饰器名字
# @timmer # index=timmer(index)
# def index(x, y, z):
#     time.sleep(2)
#     print('index %s %s %s' % (x, y, z))
#
# @timmer
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' % name)
#     return name

# home = timmer(home)
# index = timmer(index)

# res = home('egon')
# print('返回值=>', res)

# 总结：
# 优化思路：修改源代码=>在调用函数附近修改代码=>在新函数里调用原函数并进行功能拓展=>
# 无参装饰器模板
# def outter(func):
#     def wrapper(*args, **kwargs):
#         # 1、调用原函数
#         # 2、为其增加新功能
#         res = func(*args, **kwargs)
#         return res
#     return wrapper

