
# 文件对象又称为文件句柄
with open('a.txt', mode='rt') as f1, \
        open('b.txt') as f2:
    print(f1)
    res1 = f1.read()
    res2 = f2.read()
    print(res1)
    print(res2)


