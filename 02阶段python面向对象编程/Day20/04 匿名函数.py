
# 1、有名函数
# func=函数的内存地址
# def func(x, y):
#     return x + y
# print(func)

# 2、lambda用于定义匿名函数
# print(lambda x, y: x + y)

# 3、调用匿名函数
# 方式一：
# res = (lambda x, y: x + y)(2, 3)
# print(res)

# 方式二：
# func = lambda x, y: x + y
# print(func)
# res = func(2, 3)
# print(res)

# 4、匿名用于临时调用一次的场景：更多的是将匿名与其他函数配合使用

salaries = {
    'sir': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}

# ============max、min============
# 需求1：找出薪资最高的那个人
# res = max(salaries)
# print(res)    # tom

# max：先迭代第一个参数的内容, key可传入比较方法的函数
# res = max(salaries, key=lambda x: salaries[x])
# print(res)  # lili

# ============sorted============
# res = sorted(salaries)
# print(res)
# res = sorted(salaries, key=lambda x: salaries[x])
# print(res)

# ============map============
# l = ['alex', 'lxx', 'wxx', '薛嫌弃']
# new_l = [name + '_dsb' for name in l]
# print(new_l)
# res = map(lambda name: name+'_dsb', l)
# print(res)

# ============filter============
# l = ['alex_dsb', 'lxx', 'wxx_dsb', '薛嫌弃']
# res = [name for name in l if name.endswith('dsb')]
# print(res)
# res = filter(lambda name: name.endswith('dsb'), l)
# print(res)

# ============reduce============
# from functools import reduce
# res = reduce(lambda x, y: x+y, [1, 2, 3], 10)   # 16
# print(res)

# res = reduce(lambda x, y: x+y, ['自己版本.py', 'b', 'c'], 'hello')    # helloabc
# print(res)
