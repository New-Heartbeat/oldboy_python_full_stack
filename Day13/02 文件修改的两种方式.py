# 1、将文件内容取出后进行修改，并将修改后的内容存入内存，再打开文件将修改后的内容写入
# with open('自己版本.py.txt', mode='rt') as f:
#     res = f.read()
#     print(res)
# data = res.replace('alex', 'egon')
# with open('自己版本.py.txt', mode='wt') as f:
#     f.write(data)

# 2、将修改后的文件内容写入另一个文件
# import os
#
# with open('自己版本.py.txt', mode='rt') as f1, open('自己版本.py.txt.swap', mode='wt') as f2:
#     for line in f1:
#         res = line.replace('alex', 'egon')
#         f2.write(res)
#
# os.remove('自己版本.py.txt')
# os.rename('自己版本.py.txt.swap', '自己版本.py.txt')



