# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
# egon male 18 3000
# alex male 38 30000
# wupeiqi female 28 20000
# yuanhao female 28 10000

# 要求:
# 从文件中取出每一条记录放入列表中
# 列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
keys = ['name', 'sex', 'age', 'salary']
with open(r'../Day19/day19homework.txt', mode='rt') as f:
    l1 = []
    for line in f:
        values = line.strip('\n').split(' ')
        d = dict(zip(keys, values))
        l1.append(d)
# print(l1)

# 2 根据1得到的列表,取出所有人的薪资之和
# salary_ttl = sum(int(info['salary']) for info in l1)
# print(salary_ttl)

# 3 根据1得到的列表,取出所有的男人的名字
# male_set = [info['name'] for info in l1 if info['sex']=='male']
# print(male_set)

# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
# for info in l1:
#     info['name'] = info['name'].capitalize()
# print(l1)

# 5 根据1得到的列表,过滤掉名字以a开头的人的信息
# l2 = [info for info in l1 if not info['name'].startswith('自己版本.py')]
# print(l2)

# 6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 5 8 13 21...)
# def func(n):
#     if n < 2:
#         return n
#     res = func(n-1) + func(n-2)
#     return res
# print(func(7))

# 7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值
# l = [1, 2, [3, [4, 5, [6, [7, [8, 9, [10, 11, 12]]]]]]]
# l2 = [1, 2, [3, 4]]
# def func(list1):
#     for l in list1:
#         if type(l) is list:
#             func(l)
#         else:
#             print(l)
# func(l2)

# 选做作业：同昨天