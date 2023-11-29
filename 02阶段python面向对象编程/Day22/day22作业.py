# 今日作业：
#     1、检索文件夹大小的程序，要求执行方式如下
#         python3.8 run.py 文件夹
# import sys
# import os

# dirname = sys.argv[1]
# dirname = r'D:\老男孩python全栈\Day21'

# print(os.listdir(dirname))
# print(os.path.isdir(dirname))
# os.path.getsize()

# size = 0
# def getdirsize(dirname):
#     global size
#     file_list = os.listdir(dirname)
#     for file_path in file_list:
#         abs_file_path = os.path.join(dirname, file_path)
#         if os.path.isdir(abs_file_path):
#             getdirsize(abs_file_path)
#         else:
#             res = os.path.getsize(abs_file_path)
#             size += res
#     return size

# if __name__ == '__main__':
#     dirsize = getdirsize(dirname)
#     print(dirsize)
#     print(dirname)

#     2、明天上午日考：随机验证码、模拟下载以及打印进度条、文件copy脚本

# 随机验证码
# import random
#
# def get_code(n=6):
#     code = ''
#     for i in range(n):
#         num = str(random.randint(0, 9))
#         alp = chr(random.randint(65, 90))
#         res = random.choice([num, alp])
#         code += res
#     print(code)
# get_code()


# 模拟下载以及打印进度条
# import time
#
# recv = 0
# ttl_size = 33333
#
# while recv < ttl_size:
#     recv += 1024
#     time.sleep(0.3)
#     percent = int(recv / ttl_size * 100)
#     if percent > 100:
#         percent = 100
#     strip = '#' * int(percent * 0.5)
#     # print(percent)
#     print('\r[%-50s] %s%%' % (strip, percent), end='')


# 文件copy脚本
# python3.8 day22作业.py src_file dst_file

import sys

src_file = sys.argv[1]
dst_file = sys.argv[2]

with open(src_file, mode='rb') as f1, open(dst_file, mode='wb') as f2:
    for line in f1:
        f2.write(line)














