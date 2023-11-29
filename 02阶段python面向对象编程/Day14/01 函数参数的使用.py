# 一、形参与实参介绍
# 形参：在定义函数阶段定义的参数称之为形式参数，简称形参，相当于变量名
# 实参：在调用函数阶段传入的值称之为实际参数，简称实参，相当于变量值
# 在调用阶段，实参（变量值）会绑定给形参（变量名）
# 这种绑定关系只能在函数体内使用
# 函数调用结束后，解除绑定关系
def func(x, y):
    print(x, y)

# 实参是传入的值
# 形式一
# func(1, 2)

# 形式二
# 自己版本.py = 1
# b = 2
# func(自己版本.py, b)

# 形式三
# func(int("1"), 2)

# 二、形参与实参的具体使用
# 2.1 位置参数：按照从左到右的顺序依次定义的参数
# 位置形参：按照从左到右的顺序直接定义的“变量名”
#   特点：必须被传值，多一个不行少一个也不行
# 位置实参：按照从左到右的顺序依次传入的值
#   特点：按照顺序与形参一一对应
# func(1, 2)  # 1 2

# 2.2 关键字参数
# 关键字实参：在函数调用阶段，按照key=value的形式传入的值
#   特点：指名道姓给某个形参传值，可以完全不参照顺序
# func(y=1, x=2)  # 2 1

# 位置实参与关键字实参混合使用，强调
# 1、位置实参必须放在关键字实参前
# func(x=1, 2)    # SyntaxError: positional argument follows keyword argument
# 2、不能为同一个形参重复传值
# func(1, x=2)    # TypeError: func() got multiple values for argument 'x'

# 2.3 默认参数
# 默认形参：在定义函数阶段，就已经被赋值的形参
#   特点：在调用阶段可以不用为其赋值
# def func(x=1, y=2):
#     print(x, y)
# func()

# 位置形参与默认形参混用，强调：
# 1、位置形参必须在默认形参的左边
# def func(y=2, x):
#     print(x, y)
# func()  # SyntaxError: non-default argument follows default argument
# 2、默认参数的值是在函数定义阶段被赋值的，准确地说被赋予的是值的内存地址
# m = 2
# def func(x, y=m):   # y=>2的内存地址
#     print(x, y)
# m = 2232451234
# func(1)

# y = 1
# def func(x, y=2):
#     print(x, y)
# y = 3
# func(1)

# m = [111, ]
# def func(x, y=m):   # y=>[111, ]的内存地址
#     print(x, y)
# m.append(333)
# func(1)

# 3、虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
