# 不可变类型：值变，id也得跟着变
# 可变类型：值变，id可以不变

# 1.整型：不可变
# x = 10
# print(id(x))
# x = 11
# print(id(x))

# 2.浮点型：不可变
# x = 5.1
# print(id(x))
# x = 1.5
# print(id(x))

# 3.字符串类型：不可变
# x = 'egon'
# print(id(x))
# x = 'wj'
# print(id(x))

# 4.列表类型：可变
# 只要赋值，就会产生新的空间

# 这里产生了新的空间存放新赋值的列表[0, 'b', 3.0]，并让x指向新的列表，故id值变了
x = [1, 'b', 3.0]
id1 = id(x)
x = [0, 'b', 3.0]
id2 = id(x)
print(id1 == id2)

# 这里产生新的空间存放x[0]，但x与列表的联系没变，故id值不变
x = [1, 'b', 3.0]
id1 = id(x)
x[0] = 0
id2 = id(x)
print(id1 == id2)

# 5.字典类型：可变，原理同列表
# 注：字典的 key 必须是不可变类型
x = {'自己版本.py': 1, 'b': 'egon'}
id1 = id(x)
x = {'自己版本.py': 18, 'b': 'egon'}
id2 = id(x)
print(id1 == id2)

x = {'自己版本.py': 1, 'b': 'egon'}
id1 = id(x)
x['自己版本.py'] = 18
id2 = id(x)
print(id1 == id2)

# 6.bool类型：不可变
x = True
id1 = id(x)
x = False
id2 = id(x)
print(id1 == id2)

# 总结：整型、浮点型、字符串、bool的值都是不可分割的整体，都是不可变类型
