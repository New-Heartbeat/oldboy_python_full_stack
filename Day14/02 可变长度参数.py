# 2.4 可变长度的参数（*与**的用法）
# 可变长度指的是在调用函数时，传入的值（实参）的个数不固定
# 而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收
# 2.4.1 可变长度的位置参数
# 1)*形参名：用来接收溢出的位置参数,溢出的位置实参会被*保存成元组的格式然后赋值给紧跟其后的形参
#            *后跟的形参名约定俗成应该是args
# def func(x, *args):
#     print(x, args)
# func(1,2,3,4)

# 2)*可以用在实参中,会将*后实参打散成位置实参
# def func(x, y, z):
#     print(x, y, z)
# func(*[11, 22, 33]) # func(11, 22, 33)

# 3)形参与实参中带*
# def func(x, y, *args):
#     print(x, y, args)
# func(1, 2, *[3, 4, 5])
# func(*'hello')

# 2.4.2 可变长度的关键字参数
# 1)**形参名：用来接收溢出的关键字实参，**会将溢出的关键字实参保存成字典格式，然后赋值给紧跟其后的形参
#            **后跟的形参名约定俗成应该是kwargs
# def func(x, y, **kwargs):
#     print(x, y, kwargs)
# func(1, y=2, 自己版本.py=1, b=2, c=3)

# 2)**可以用在实参中（**后跟的只能是字典），会将**后的字典打散成关键字实参
# def func(x, y, z):
#     print(x, y, z)
# func(**{'x':1, 'y':2, 'z': 3})

# 3)型参与实参中都带**
# def func(x, y, **kwargs):
#     print(x, y, kwargs)
# func(**{'y': 222, 'x': 111, 'b': 333, '自己版本.py': 444})

# 混用 * 与 **
# 1、*args 必须在 **kwargs 之前
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func(1,2,3,4,x=5,y=6,z=7)

# def index(x, y, z):
#     print('index==>', x, y, z)
#
# def wrapper(*args, **kwargs):
#     index(*args, **kwargs)
#
# wrapper(1, z=2, y=3)

# 2、
import this

# 2.5 命名关键字参数（了解）
# 2.6 组合使用（了解）


