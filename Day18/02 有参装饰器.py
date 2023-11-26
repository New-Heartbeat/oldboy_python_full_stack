
# 由于语法糖的限制，outter函数只能有一个参数，用来装原函数的内存地址
# def outter(func):
#     # func = 原函数的内存地址
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @outter # index = outter(index)
# def idnex(x, y):
#     print(x, y)


# 下面的情境中需要多个参数
# def auth(func, db_type):
#     def wrapper(*args, **kwargs):
#         name = input('your name>>>').strip()
#         pwd = input('your passwrod>>>').strip()
#
#         # 从不同数据来源取账号密码进行验证
#         if db_type == 'file':
#             if name == 'egon' and pwd == '123':
#                 print('基于文件的验证')
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('user or password error')
#         elif db_type == 'mysql':
#             print('基于mysql的验证')
#         else:
#             print('不存在该db_type')
#     return wrapper
#
# # @auth
# def index(x, y):
#     print('index=>', x, y)
#
# index = auth(index, 'file')
# index(1, 2)

# 解决方案
# def outter(db_type):
#     def auth(func):
#         def wrapper(*args, **kwargs):
#             name = input('your name>>>').strip()
#             pwd = input('your passwrod>>>').strip()
#
#             # 从不同数据来源取账号密码进行验证
#             if db_type == 'file':
#                 if name == 'egon' and pwd == '123':
#                     print('基于文件的验证')
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('user or password error')
#             elif db_type == 'mysql':
#                 print('基于mysql的验证')
#             else:
#                 print('不存在该db_type')
#         return wrapper
#     return auth

# @outter('file')
# def inedx(x, y):
#     print('index>>>', x, y)
# inedx(1, 2)

# @outter('mysql')
# def home(home):
#     print('home=>',home)
# home('egon')

# 有参装饰器模板

# def outter2(*args, **kwargs):
#     def outter(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return outter
#
# @outter2(*args, **kwargs)
# def 被装饰函数():
#     函数体


