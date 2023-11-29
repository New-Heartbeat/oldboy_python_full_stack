# 一、读相关操作
# 1、readline：一次读一行
# with open('b.txt', mode='rt') as f:
#     # res1 = f.readline()
#     # res2 = f.readline()
#     # print(res2)
#     while True:
#         res = f.readline()
#         if len(res) == 0:
#             break
#         print(res, end='')

# 2、readlines
# with open('b.txt', mode='rt') as f:
#     res = f.readlines()
#     print(res)

# 强调：不适用于一行数据过长的场景

# 二、写相关操作
# 1、f.writelines()
# with open('d.txt', mode='wt') as f:
#     # f.writelines('111\n222\n33333\n')
#     l = ['111\n', '222', '333']
#     f.writelines(l)

# with open('d.txt', mode='wb') as f:
    # f.writelines('111\n222\n33333\n')
    # l = [
    #     '111as\n'.encode('utf-8'),
    #     'abc'.encode('utf-8'),
    #     '651wd'.encode('utf-8')
    #
    # ]

    # 如果是纯英文数字字符，可以直接加前缀b得到bytes类型
    # l = [
    #     b'111as\n',
    #     b'abc',
    #     b'651wd'
    # ]
    # f.writelines(l)

# 2、flush：强制写入（正常情况下，系统会等装满一卡车再写入）
# with open('d.txt', mode='wt') as f:
#     f.write('哈哈哈')
#     # f.flush()

# 三、其他操作
with open('d.txt', mode='wt') as f:
    print(f.readable())
    print(f.writable())
    print(f.closed)
    print(f.encoding)
    print(f.name)

print(f.closed)
