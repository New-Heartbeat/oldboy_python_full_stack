
# import导入模块
# 优点：肯定不会与当前名称空间中的名字冲突
# 缺点：必须加前缀”模块.“


# from ... import ... 导入也发生了三件事
# 1、产生一个模块的名称空间
# 2、运行foo.py将运行过程中产生的名字都丢到模块的名称空间去
# 3、在当前名称空间拿刀一个名字，该名字与
# from foo import x
from foo import get
from foo import change

# print(x)
# x = 3333
# print(x)
# get()
# change()
# print(x)
# get()
# x = 1
# print(x)
# from foo import x
# print(x)
# get()

# from ... import ...
# 优点：不用加前缀，代码更精简
# 缺点：容易与当前名称空间混淆

# *：导入模块中的所有名字
# from foo import *



