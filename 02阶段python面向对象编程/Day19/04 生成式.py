
# 1、列表生成式
# [expression for item in iterable if condition]
# l = ['alex_dsb', 'lxx_dsb', 'wxx_dsb', 'xxq_dsb', 'egon']

# new_l = []
# for name in l:
#     if name.endswith('dsb'):
#         new_l.append(name)
# print(new_l)

# new_l = [name for name in l if name.endswith('dsb')]
# print(new_l)

# 把所有小写字母变成大写
# new_l = [name.upper() for name in l]
# print(new_l)
# 把所有的名字去掉后缀_dsb
# new_l = [name.split('_')[0] for name in l]
# print(new_l)

# 2、字典生成式
# dict = {'name': 'egon', 'age': 18, 'gender': 'male'}
# res = {key:None for key in dict}
# print(res)

# items = [('name', 'egon'), ('age', 18), ('gender', 'male')]
# dict = {k: v for k, v in items}
# print(dict)

# 3、集合生成式
# keys = ['name', 'age', 'gender']
# set1 = {key for key in keys}
# print(set1, type(set1))

# 4、生成器表达式
# g = (i for i in range(10) if i > 3)
# !!!!!!!强调
# 此时g内部一个值也没有
# print(g, type(g))
# print(next(g))
# print(next(g))
# print(next(g))
with open('笔记', mode='rt') as f:
    # 方式一
    # res = 0
    # for line in f:
    #     res += len(line)

    # 方式二
    # res = sum([len(line) for line in f])

    # 方式三：效率最高
    # res = sum((len(line) for line in f))
    # 可简写为
    res = sum(len(line) for line in f)
    print(res)
