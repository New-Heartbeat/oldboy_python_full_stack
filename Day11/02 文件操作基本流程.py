# 1、打开文件
f = open(r'a.txt', mode='rt', encoding='utf-8')  # f的值是一种变量，占用的是应用程序的内存空间
print(f)

# 2、操作文件
res = f.read()
print(res)

# 3、关闭文件
f.close()   # 回收操作系统资源
print(f)
f.read()    # 变量f存在，但是不能再读了

# del f       # 回收应用程序资源
