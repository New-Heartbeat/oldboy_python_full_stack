# 指针移动的单位都是以bytes/字节为单位
# 只有一种情况特殊：t模式下的read(n), n代表的是字符个数
# with open('b.txt', mode='rt') as f:
#     f.read(2)
#     res = f.read()
#     print(res)

# f.seek(n, 模式)
# n：指的是移动的字节个数
# 模式：
#   0：参照物是文件开头位置
#   1：参照物是当前指针位置
#   2：参照物是文件末尾，应该倒着移（n为负）
#   只有0模式可以在t模式下使用，1、2只能在b模式下用

# f.tell()：获取文件指针当前位置
with open('b.txt', mode='rb') as f:
    f.seek(7, 0)
    f.seek(-2, 1)
    print(f.tell())
