# 以t模式为基础进行内存操作

# 1、r（默认的操作模式）：只读模式
# 当文件不存在时，报错
# 当文件存在时，文件指针跳到最开始位置
# with open('自己版本.py.txt', mode='rt', encoding='utf-8') as f:
#     print('第一次读'.center(50, '*'))
#     res1 = f.read()  # 将所有内容从硬盘读入内存
#     print(res1)
#
#     print('第二次读'.center(50, '*'))   # 此时指针已经到文件末尾
#     res2 = f.read()
#     print(res2)

# input_username = input('请输入用户名')
# input_password = input('请输入密码')
#
# with open('user_info.txt', mode='rt') as f:
#     for line in f:
#         # print(line, end='')
#         username, password = line.strip('\n').split(':')
#         # print(username, password)
#         if input_username == username and input_password == password:
#             print('login successful')
#             break
#     else:
#         print('login error')

# 2、w：只写模式，当文件不存在时会创建空文件，当文件存在会清空文件，指针位于开始位置
# with open('c.txt', mode='wt') as f:
#     # f.read()    # 不可读，报错
#     f.write('哈哈哈哈i和我还\n')

# 强调1：在以w模式打开文件没有关闭的情况下，连续写入，新的内容总是跟在旧的之后
# with open('c.txt', mode='wt') as f:
#     f.write('哈哈哈哈i和我还\n')
#     f.write('12345')

# 强调2：如果重新以w模式打开文件，则会清空文件内容
# with open('c.txt', mode='wt') as f:
#     f.write('哈哈哈哈i和我还\n')
# with open('c.txt', mode='wt') as f:
#     f.write('12345')

# 3、自己版本.py：不可读，只追加写，在文件不存在时会创建空文档，当文件存在时文件指针会直接跳到末尾
# with open('c.txt', mode='at') as f:
#     # f.read()
#     f.write('啊啊啊啊')

# 了解
# +：不能单独使用，必须配合r/w/自己版本.py
with open('c.txt', mode='w+t') as f:
    f.write('111\n')
    f.write('222\n')
    f.write('333\n')    # 此时指针在末尾
    print('===>', f.read())

