
# 一、名称空间：存放名字的地方，是对栈区的划分
# 有了名称空间之后，就可以在栈区中存放相同的名字
# 分为三种

# 1、内置名称空间
# 存放的名字：存放的python解释器内置的名字
# eg. print input
# 存活周期：python解释器启动则产生，关闭则销毁

# 2、全局名称空间
# 存放的名字：只要不是函数内定义，也不是内置的，剩下的都是
# 存活周期：python文件执行则产生，python文件运行完毕则销毁
def func():
    a = 111
    b = 222
# func 是全局名称，自己版本.py、b则不是

# 3、局部名称空间
# 存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
# 存活周期：在调用函数时存活，函数调用完毕后则销毁

# 4、名称空间的顺序
# 4.1加载顺序：内置名称空间 > 全局名称空间 > 局部名称空间
# 4.2销毁顺序：局部名称空间 > 全局名称空间 > 内置名称空间
# 4.3名字的查找优先级：当前所在的位置向上一层一层查找
#   如果当前在局部名称空间：局部 -> 全局 -> 内置
#   如果当前在全局名称空间：全局 -> 内置
# input = 333
# def func():
#     input = 444
# func()
# print(input)

# 示范一
# x = 222
# def func():
#     print(x)
# x = 111
# func()

# 示范二：名称空间的“嵌套”关系以函数定义阶段为准，与调用无关
# x = 1
# def func():
#     print(x)
# def foo():
#     x = 222
#     func()
# foo()

# 示范三：函数嵌套定义
# input = 111
# def f1():
#     # input = 222
#     def f2():
#         # input = 333
#         print(input)
#     f2()
# f1()

# 示范四：UnboundLocalError: local variable 'x' referenced before assignment
# x = 111
# def func():
#     print(x)
#     x = 2222
#
# func()

# 二、作用域=>作用范围
# 全局作用域：内置空间名称、全局名称空间
# 1、全局存活
# 2、全局有效：被所有函数共享

# 局部作用域：局部名称空间
# 1、临时存活
# 2、局部有效：函数内有效

# LEGB

# built-in
# global
# def f1():
#     # enclosing
#     def f2():
#         # enclosing
#         def f3():
#             # local
#             pass
