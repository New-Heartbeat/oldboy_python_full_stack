# 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# def func(str):
#     num = 0
#     alpha = 0
#     space = 0
#     other = 0
#     for i in str:
#         if i.isdigit():
#             num += 1
#         elif i == ' ':
#             space += 1
#         elif i.isalpha():
#             alpha += 1
#         else:
#             other += 1
#     print(f'数字：{num}, 字母：{alpha}, 空格：{space}, 其他：{other}')
#     return
# func('asv1519 qw24-+')

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def func(x):
#     if len(x) > 5:
#         print('True')
#     else:
#         print('False')
# func('dwqf13')

# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(x):
#     x.remove(x[0])
#     return x[::2]
# res = func([1, '自己版本.py', 2, 9, 15])
# print(res)

# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
# 选做作业：同昨天
