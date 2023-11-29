# 逻辑运算符
# not and or
# 优先级：() > not > and > or

# 1、not
# 把紧跟其后的条件取反，与紧跟其后的条件是一个不可分割的整体
print(not 2 > 1)
print(not None)
print(not [])

# 2、and
# 用来连结左右两个条件，两个条件同时为True，最终结果才为真
print(True and 10 > 3 and 10 and 0)
print(True and 10 > 3 and 10 and 1 > 2)
print(0 and 10 > 3 and 10 and 1 < 2)

# 3、or
# 连结的两个条件但凡有一个为真，最终结果就为真
print(10 or False or [])

# 补充：短路运算
# 偷懒原则：偷懒到哪个位置，就把当前位置的值返回
print(10 or 5)
print(5 or 10)  # or只要看到一个真就会停下，故会偷懒到第一个为真的位置
print(10 and 5)     # and需要确认所有都为真，故会偷懒到最后一个位置
