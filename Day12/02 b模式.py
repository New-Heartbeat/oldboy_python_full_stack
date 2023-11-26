"""
控制文件读写内容的模式：
t：
    1、读写都是以字符串（unicode）为单位
    2、只能针对文本文件
    3、必须指定字符编码

b：binary模式
    1、读写都是以bytes为单位
    2、可以针对所有文件
    3、一定不能指定encoding

总结：
1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要转换
2、针对非文本文件（如图片、视频、音频等）只能使用b模式
"""
# with open(r'桌面.mp4', mode='rt') as f:
#     res = f.read()
#     print(res)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe1 in position 48: invalid continuation byte

# with open(r'桌面.mp4', mode='rb') as f:
#     res = f.read()  # 硬盘的二进制读入内存->b模式下，不做任何转换，直接读入内存
#     print(res, type(res))

# with open(r'自己版本.py.txt', mode='rb') as f:
#     res = f.read()
#     print(res, type(res))
#     print(res.decode('utf-8'))
#
# with open(r'自己版本.py.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read()  # utf-8的二进制 -> unicode
#     print(res, type(res))

# with open('b.txt', mode='wb') as f:
#     # f.write('hello world')  # TypeError: 自己版本.py bytes-like object is required, not 'str'
#     f.write('你好hello world'.encode('gbk'))

# 文件拷贝工具：适用所有类型文件
src_file = input('源文件路径===>').strip()
dst_file = input('目标文件路径===>').strip()

# 循环读取文件（推荐适用，节省内存空间）
# 方式一：按行循环，适用于一行的长度较短的情况
# with open(src_file, mode='rb') as f1, open(dst_file, mode='wb') as f2:
#     for line in f1:
#         f2.write(line)

# 方式二：控制每次读取的长度，
with open(src_file, mode='rb') as f1, open(dst_file, mode='wb') as f2:
    while True:
        res = f1.read(1024)
        if len(res) == 0:
            break
        f2.write(res)
