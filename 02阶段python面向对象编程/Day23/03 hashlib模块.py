
# 1、什么是哈希
#   hash一类算法，该算法接收传入的内容，经过运算得到一串hash值
#   hash值的特点：
# 1.1 只要传入的内容一样，得到的hash值必然一样
# 1.2 不能由hash值反解内容
# 1.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的

# 特点2用于密码密文传输与验证
# 特点1、3用于文件完整性校验

# 2、hash的用途
import hashlib

# m = hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res1 = m.hexdigest()
# print(res1)
#
# m1 = hashlib.md5('he'.encode('utf-8'))
# m1.update('llo'.encode('utf-8'))
# m1.update('wor'.encode('utf-8'))
# m1.update('ld'.encode('utf-8'))
# res2 = m1.hexdigest()
# print(res2)

# 模拟撞库
# m2 = hashlib.md5('alex1314'.encode('utf-8'))
# print(m2.hexdigest())
# cryptograph = '8971146949ef6a8e2db2bb86e00a1791'
# passwords = [
#     'alex3714',
#     'alex1313',
#     'alex94139413',
#     'alex1314'
# ]
#
# dic = {}
# for p in passwords:
#     res = hashlib.md5(p.encode('utf-8'))
#     dic[p] = res.hexdigest()
#
# for k, v in dic.items():
#     if v == cryptograph:
#         print('撞库成功, 明文密码是：%s' % k)
#         break

# 提升撞库的成本==>密码加盐
# 在密码周围以一定的规则加上暗号（”天王盖地虎“）后再加密
# m3 = hashlib.md5()
# m3.update('天王')
# m3.update('alex1314')
# m3.update('盖地虎')
