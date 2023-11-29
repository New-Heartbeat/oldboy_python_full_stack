# 1、作用：按位置存放多个值
# 2、定义
# l = [1, 1.2, "自己版本.py", [1, 2]]
# print(type(l))

# 3、类型转换：但凡能够被for循环遍历的类型都可以当作参数传给list()转成列表
# res = list('hello')
# print(res)
#
# res = list({'k1': 111, 'k2': 222, 'k3': 333})
# print(res)

# 4、内置方法
# 优先掌握的操作
# 1.按索引取值（正向+反向）：既可以取也可以改
# l = [111, 'egon', 'hello']
# print(l[0])
# l[0] = 222  # 索引存在则修改对应的值
# print(l)
# # 索引不存在则报错
# l[3] = 333

# 2.切片（顾头不顾尾，步长）
# l1 = [111, 'egon', 'hello', [1, 2, 3]]
# l2 = l1[:]  # 等同于拷贝行为，相当于浅拷贝
# print(l1, l2)
# l1[0] = 222
# l1[-1][0] = 1111111
# print(l1, l2)

# 3.长度
# l1 = [111, 'egon', 'hello', [1, 2, 3]]
# print(len(l1))

# 4.成员运算 in 和 not in
# l1 = [111, 'egon', 'hello', [1, 2, 3]]
# print('egon' in l1)

# 5.追加
# l = [111, 'egon', 'hello']
# l.append(333)
# l.append(444)
# print(l)

# 6.插入值
# l = [111, 'egon', 'hello']
# l.insert(0, 'alex')
# print(l)

# 7.扩展可迭代对象
# l1 = [111, 'egon', 'hello']
# l2 = [1, 2, 3]
# l1.extend(l2)
# print(l1,l2)
# print(l1.extend('abc')) # 返回None
# print(l1)

# 7.删除
# 方式一：通用的删除方法，只是单纯的删除，没有返回值
# l1 = [111, 'egon', 'hello']
# del l1[0]
# x = del l1  # 抛出异常，不支持赋值语法
# print(l1)

# 方式二：l.pop()根据索引删除，默认删除最后一个，会返回删除的那个值
# l1 = [111, 'egon', 'hello', 258]
# res = l1.pop(2)
# print(l1, res)
# l1.pop()
# print(l1)

# 方式三：l.remove()根据元素删除，返回None
# l1 = [111, 'egon', 'hello', 258]
# res = l1.remove('egon')
# print(l1, res)


# 8.循环
# l1 = [111, 'egon', 'hello', [1, 2, 3]]
# for x in l1:
#     print(x)

# 其他需要掌握的操作
# l1 = [111, 'egon', 'hello', [1, 2, 3], 111]
# count：计数
# print(l1.count(111))

# clear：清除列表内的值
# res = l1.clear()
# print(l1, res)

# reverse：翻转列表
# res = l1.reverse()
# print(l1, res)

# index
# print(l1.index(111))
# print(l1.index('xxxxxxxxx'))    # 找不到报错

# sort：排序，默认从小到大，升序
# 列表里的元素必须是同种类型
# 字符串比较：按ASCI码表 字典型比较,从第一个元素的第一个字母开始比
# 加参数reverse=True 则是从大到小排序，降序
# l1 = ['自己版本.py', 'wd', 'acw', 'wa']
# res = l1.sort()
# print(l1, res)
#
# l1 = [[1, 2, 3, 4], [3, 2, 1], [3, 1, 2]]
# res = l1.sort()
# print(l1, res)

# 补充
# 1、队列：FIFO，先进先出
# 2、堆栈：LIFO，后进先出


