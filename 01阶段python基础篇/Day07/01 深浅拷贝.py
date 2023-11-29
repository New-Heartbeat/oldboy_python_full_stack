list1 = ['egon', 'lxx', [1, 2]]
list2 = list1
# 二者分隔不开，list改list2也跟着改，因为指向的是同一个内存地址
# list1[0] = 'EGON'
# print(list2)

# 需求：
# 1、拷贝一下原列表产生一个新的列表
# 2、想让两个列表完全独立开，针对的是改操作的独立而不是读操作
# 3、如何copy列表

# 3.1 浅拷贝:把原列表第一层的内存地址不加区分完全copy一份给新列表
list3 = list1.copy()
# print(list3)
# print(id(list1) == id(list3))
# print(id(list1[0]), id(list1[1]), id(list1[2]))
# print(id(list3[0]), id(list3[1]), id(list3[2]))

# list1[0] = 'EGON'
# list1[1] = 'LXX'
# list1[2][0] = 123
# list1[2][1] = 321
# print(list1)
# print(list3)

# 要想copy得到的新列表与原列表的改操作完全独立开来
# 必须有一种可以区分开可变类型与不可变类型的copy机制
# 3.2 深拷贝：
import copy

list4 = copy.deepcopy(list1)
# print(id(list1))
# print(id(list4))
# print(id(list1[0]), id(list1[1]), id(list1[2]))
# print(id(list4[0]), id(list4[1]), id(list4[2]))
# 相比于浅拷贝，这里对可变类型list1[2]中的列表的复制分配了新的空间
# print(id(list1[2][0]), id(list1[2][1]))
# print(id(list4[2][0]), id(list4[2][1]))

list1[0] = 'EGON'
list1[1] = 'LXX'
list1[2][0] = 123
list1[2][1] = 321
print(list1)
print(list4)

# 总结：深拷贝可以对原列表所有类型的值进行独立的改操作
