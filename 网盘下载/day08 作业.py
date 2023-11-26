# 一：for循环
# 1.1 for循环嵌套之打印99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         res = i * j
#         print(f"{i} * {j} = {res}", end=' ')
#     print('\n', end='')

# 1.2 for循环嵌套之打印金字塔
# 提示分析如下
"""

             #max_level=5
    *        #current_level=1，空格数=4，*号数=1
   ***       #current_level=2,空格数=3,*号数=3
  *****      #current_level=3,空格数=2,*号数=5
 *******     #current_level=4,空格数=1,*号数=7
*********    #current_level=5,空格数=0,*号数=9

#数学表达式
空格数=max_level-current_level
*号数=2*current_level-1
"""
# max_level = 5
# for i in range(max_level):
#     curr_level = i + 1
#     space_num = max_level - curr_level
#     star_num = 2 * curr_level - 1
#     print(("*" * star_num).rjust(space_num + star_num, " "))

# 1.3 用for+range改写今日早晨默写的代码，作为明天默写内容


# 二：字符串操作
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）

name = " aleX"
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果
print(name.startswith("al"))
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果
print(name.endswith('X'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
print(name.replace("l", "p"))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
print(name.split('l'))
# 6)    将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
print(name[2])
# 10)    请输出 name 变量对应的值的后 2 个字符?
print(name[-2:])
# 11)    请输出 name 变量对应的值中 “aaa.txt” 所在索引位置?
print(name.find("aaa.txt"))
# 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
print(name[:-1])
