# 1、作用：可以存放多个值，主要用于去重、关系运算
# 是可变类型
# s1 = {1, 2, 3}
# print(s1, id(s1))
# s1.add(4)
# print(s1, id(s1))
# 2、定义：在{}内用逗号分隔开多个元素，集合具备以下三个特点：
#       自己版本.py.每个元素必须是不可变类型
#       b.集合内没有重复的元素
#       c.集合内元素无序
# s = {1, 2, 3, 4}  # 本质：s = set({1, 2, 3, 4})
# 注意：列表类型是索引对应值，字典是key对应值，均可以取得单个指定的值
# 集合类型既没有索引也没有key与值对应，所以无法取得单个的值
# 而且对于集合来说，主要用于去重与关系元素，根本没有取出单个指定值这种需求

# s = {}  # 空字典
# print(type(s))
# s = set()  # 空集合
# print(type(s))

# 3、类型转换
# 但凡能被for循环的遍历的数据类型（遍历出的每一个值都必须为不可变类型）
# 都可以传给set()转换成集合类型
# print(set('hello'))
# print(set([1, 2, 'aaa', 2, 1]))
# print(set({'k1': 111, 'k2': 222, 'k1': 123}))
# print(set((1, 2, 3)))

# 4、使用
# 4.1 关系运算
# friends1 = {"zero", "kevin", "jason", "egon"}
# friends2 = {"Jy", "ricky", "jason", "egon"}
# # 自己版本.py.交集
# print(friends1 & friends2)
# # b.并集
# print(friends1 | friends2)
# # c.差集
# print(friends1 - friends2)
# # d.对称差集：求两个用户独有的好友们
# print(friends1 ^ friends2)
# # aaa.txt.值是否相等
# print(friends1 == friends2)
# # f.父子集
# s1 = {1, 2, 3}
# s2 = {1, 2}
# print(s1 > s2)

# 4.2 去重
# 集合去重有限性：
# 只能针对不可变类型
# 集合本身是无序的，去重之后无法保留原来的顺序
# l = [1, '自己版本.py', 'z', 1, 1, 'd']
# s = set(l)
# l = list(s)
# print(l)

# 4.3 其他操作
# 长度 len
# 成员运算 in 和 not in
# 循环

# pop：删掉原集合的一个值（元组无序，不确定会删除哪个值），会返回被删掉的值
# s1 = {1, 2, 3}
# res = s1.pop()
# print(s1, res)

# clear
# s1 = {1, 2, 3}
# res = s1.clear()
# print(s1, res)

# update：接收一个可迭代对象并将该对象每个元素添加到集合中；没有返回值
# s1 = {1, 2, 3}
# res = s1.update('abc2')
# print(s1, res)

# remove：移除集合中的元素，如果原集合没有该元素会报错；没有返回值
# s1 = {1, 2, 3}
# res = s1.remove(2)
# print(s1, res)

# discard：移除集合中的元素，

# add：添加一个元素；没有返回值，如果原集合没有该元素不会报错；没有返回值
# s1 = {1, 2, 3}
# res = s1.discard('ab')
# print(s1, res)

# s1.difference(s2)：不改变原集合，返回值为集合s1-s2
# friends1 = {"zero", "kevin", "jason", "egon"}
# friends2 = {"Jy", "ricky", "jason", "egon"}
# res = friends1.difference(friends2)
# print(res)
# print(friends1 - friends2)

# s1.intersection(s2)：返回s1和s2的交集
# friends1 = {"zero", "kevin", "jason", "egon"}
# friends2 = {"Jy", "ricky", "jason", "egon"}
# res = friends1.intersection(["Jy", "ricky", "jason"])
# print(res)

# isdisjoint：判断两个集合的交集是否为空
# friends1 = {"zero", "kevin", "jason", "egon"}
# friends2 = {"Jy", "ricky"}
# res = friends1.isdisjoint(friends2)
# print(res)
