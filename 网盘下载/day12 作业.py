# 1、通用文件copy工具实现
# src_file = input('源文件路径===>:').strip()
# dst_file = input('目标文件路径===>:').strip()
# with open(src_file, mode='rb') as f1, open(dst_file, mode='wb') as f2:
#     while True:
#         res = f1.read(1024)
#         if len(res) == 0:
#             break
#         f2.write(res)
#     print('copy successful')

# 2、基于seek控制指针移动，测试r+、w+、自己版本.py+模式下的读写内容
# 注：字符在内存/硬盘中都是以字节编码形式存在，1个中文占3个字节（utf-8中）
# 覆盖写的时候要注意字节的对应，
# 如原文'ab哈',文件加载到内存中是 1|1|3 字节，如果写入1个中文，会覆盖前三个字节，
# 导致原文哈占用的第一个字节被覆盖，虽然在底层里（内存和硬盘中）都是放的字节不会报错，
# 但如果想读内容的话，就会由于哈占用的第一个字节被覆盖导致按utf-8编码找不到对应的值而报错
# 而如果原文为'abc哈',文件加载到内存是 1|1|1|3 字节，如果写入1个中文，覆盖前3个字节所表示的'abc'，
# 并不会影响后面的'哈'所占用的字节，所以不会影响以utf-8读取文件内容
# f.seek()移位是针对字节数来的，1、2模式只能在b模式下使用
# 所有的写和读都是从当前指针位置开始
# r、w、a模式的不同之处在于初始指针的位置和是否会先清空原内容

# with open(r'../Day12/b.txt', mode='r+t', encoding='utf-8') as f:
#     print(f.tell())    # r模式打开 指针在开始位置
#     # f.write('abc')   # r+模式也可写，但是是覆盖写
#     # print(f.tell())
#     # f.write('def')
#     # print(f.tell())
#     f.write('覆盖')   # 写入两个中文，在utf-8中占6个字节
#     print(f.tell())  # 6，此时读的话只能读后面的内容
#
#     f.seek(-6, 1)    # 指针从当前位置往前移动6个字节，从而能读完整个文件
#     res2 = f.read()
#     print(res2)

# with open(r'../Day12/b.txt', mode='r+b') as f:
#     print(f.tell())
#     f.write('覆盖'.encode('utf-8'))
#     print(f.tell())
#     f.seek(-6, 1)  # seek的1、2模式只能在b模式下使用
#     print(f.read().decode('utf-8'))
#     print(f.tell())  # 读完指针就会到末尾
#     f.seek(-5, 1)
#     f.write('哈'.encode('utf-8'))
#     f.seek(0, 0)
#     print(f.read().decode('utf-8'))

# with open('../Day12/b.txt', mode='w+b') as f:
#     # w打开文件会清空原内容，指针在开始位置
#     f.write('你好hello world\n哈哈***哈'.encode('utf-8'))
#     print(f.tell())
#     f.write('增加的内容'.encode('utf-8'))
#     f.seek(-15, 1)
#     print(f.read().decode('utf-8'))

# with open('../Day12/b.txt', mode='自己版本.py+b') as f:
#     # a打开文件，指针会停在末尾
#     # print(f.tell())
#     # print(f.read().decode('utf-8'))
#     f.write('\n追加的内容1'.encode('utf-8'))
#     f.seek(-16, 1)
#     print(f.read().decode('utf-8'))
#     f.seek(-17, 1)
#     f.write('\n追加的内容2'.encode('utf-8'))
#     f.seek(0, 0)
#     print(f.read().decode('utf-8'))

# 3、tail -f access.log程序实现
# 循环读取日志的最后一行
with open('../Day12/b.txt', mode='r+b') as f:
    last_line_len = len(f.readlines()[-1])
    f.seek(last_line_len*-1, 2)
    print(f.read().decode('utf-8'))

# 4、周末作业参考在老师讲解完毕后（下午17：30开始讲解），练习熟练，明早日考就靠他俩
# 4.1：编写用户登录接口
# 4.2：编写程序实现用户注册后（注册到文件中），可以登录（登录信息来自于文件）
