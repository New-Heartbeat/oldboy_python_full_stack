# 一、大前提
# 闭包函数=名称空间与作用域+函数嵌套+函数对象
#       核心点：名字的查找关系是以函数定义阶段为准

# 二、什么是闭包函数
# 闭函数指的是该函数是内嵌函数
# 包函数指的该函数包含对外层作用域名字的引用（不是对全局作用域）

# 闭包函数：名称空间与作用域+函数嵌套
# def f1():
#     x = 33333333
#     def f2():
#         print(x)
#     f2()
#
# x = 111
# def bar():
#     x = 444444
#     f1()
#
# def foo():
#     x = 222222
#     bar()
#
# foo()

# 闭包函数：函数对象
# def f1():
#     x = 33333333
#     def f2():
#         print('函数f2', x)
#     return f2
#
# f = f1()
# print(f)
# x = 1111
# f()
# def foo():
#     x = 5555
#     f()
# foo()

# 三、为何要有闭包函数 => 闭包函数的应用
# 两种为函数传参的方式
# 方式一：直接把函数体需要的参数定义成形参
# def f1(x):
#     print(x)
# f1(2)

# 方式二：
# def f1():
#     x = 3
#     def f2():
#         print(x)
#     return f2
# f = f1()

import requests

def outter(url):
    def get():
        response = requests.get(url)
        print(len(response.text))
    return get
baidu = outter('http://www.baidu.com')
baidu()
baidu()
baidu()
baidu()

# 'http://www.baidu.com'
# 'http://bilibili.com'

