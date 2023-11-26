
"""
t文本（默认的模式）
1、读写都以str（unicode）为单位
2、文本文件
3、必须指定encoding='utf-8'
"""
# 没有指定encoding参数操作系统会使用自己默认的编码
# linux系统默认utf-8
# windows系统默认gbk (以前默认gbk）
with open('a.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()
    print(res, type(res))



