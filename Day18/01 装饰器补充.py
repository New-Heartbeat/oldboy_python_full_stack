#
# def outter(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper


# @outter # index = outter(index)
# def index(x, y):
#     """这个是主页功能"""
#     print(x, y)

# 偷梁换柱：即将原函数名指向的内存地址偷梁换柱成wrapper函数
#           所以应该将wrapper做的跟原函数一样才行
from functools import wraps

# index.__name__ = 原函数.__name__
# index.__doc__ = 原函数.__doc__
def outter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    # 手动将原函数的属性赋值给wrapper函数
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

@outter # index = outter(index)
def index(x, y):
    """这个是主页功能"""
    print(x, y)

print(index)
print(index.__doc__)




