"""
1、什么是迭代器
    迭代器指迭代取值的工具
    迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的

2、为何要有迭代器
    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型
    有：列表、字符串、元组、字典、集合、文件

    l = ['egon', 'liu', 'alex']
    i = 0
    while i < len(l):
        print(l[i])
        i += 1

    上述迭代取值的方式只适用于有索引的数据类型
    为了解决基于索引迭代器取值的局限性
    python必须提供一种能够不依赖于索引的取值方式，这就是迭代器

3、如何用迭代器

"""
# 可迭代对象：但凡内置有__iter__方法的都称之为可迭代对象
# 迭代器对象：内置有__next__方法和__iter__方法的对象
#               迭代器对象.__next__()：得到迭代器的下一个值
#               迭代器对象.__iter__()：得到迭代器本身，调了跟没调一个样
# 文件对象既是可迭代对象，也是迭代器对象
# dict = {'自己版本.py': 1, 'b': 2, 'c': 3}
# res = dict.__iter__()
# print(res)
# print(res.__iter__() is res)

# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())   # 抛出异常 StopIteration

# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break
#
# print('==============>')    # 上面取完之后，再对其取值取不到
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break

# for循环的工作原理
# dict = {'自己版本.py': 1, 'b': 2, 'c': 3}
# # 1.dict.__iter__()得到一个迭代器对象
# # 2.迭代器对象.__next__()拿到一个返回值，然后将返回值赋值给k
# # 3.循环往复步骤2，直到抛出StopIteration异常for循环会捕捉异常然后结束循环
# for k in dict:
#     print(k)

# list('hello') # 原理同for循环

# 迭代器优缺点总结
# 优点：1、为序列和非序列类型提供了一种统一的迭代取值方式
#      2、惰性计算
# 缺点：1、除非取尽，否则无法获取迭代器的长度
#      2、只能取下一个值，不能回到开始，更像是一次性的


