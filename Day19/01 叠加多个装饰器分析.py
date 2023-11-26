# 一、叠加多个装饰器的加载、运行分析（了解）
def deco1(func1):  # func1 = wrapper1的内存地址
    def wrapper1(*args, **kwargs):
        print('正在运行===>deco1.wrapper1')
        res1 = func1(*args, **kwargs)
        return res1

    return wrapper1


def deco2(func2):  # func2 = wrapper3的内存地址
    def wrapper2(*args, **kwargs):
        print('正在运行===>deco2.wrapper2')
        res2 = func2(*args, **kwargs)
        return res2

    return wrapper2


def deco3(x):
    def outter3(func3):  # func3 = 被装饰对象index函数的内存地址
        def wrapper3(*args, **kwargs):
            print('正在运行===>deco3.wrapper3')
            print(x)
            res3 = func3(*args, **kwargs)
            return res3

        return wrapper3

    return outter3


# 加载顺序自下而上
@deco1  # index = deco1(index) = deco1(wrapper2的内存地址）
@deco2  # index = deco2(index) = deco2(wrapper3的内存地址）
@deco3(111)  # index = x=111下的outter3(index) = wrapper3
def index(x, y):
    print('from index %s %s' % (x, y))


# print(index)
# 执行顺序自上而下，即wrapper1=>wrapper2=>wrapper3
index(1, 2)
