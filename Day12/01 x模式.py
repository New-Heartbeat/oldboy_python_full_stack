"""
x模式（控制文件操作的模式） => 了解
    只写模式【不可读；不存在则创建，存在则报错】
"""
with open('a.txt', mode='xt') as f:
    f.write('哈哈哈\n')
