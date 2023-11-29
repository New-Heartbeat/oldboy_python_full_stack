# 1、有列表['alex',49,[1900,3,18]]
# 分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
# l1 = ['alex',49,[1900,3,18]]
# name = l1[0]
# age = l1[1]
# born_date = l1[2]

# 2、用列表的insert与pop方法模拟队列
# l = []
# # 入队
# l.append(1)
# l.append(22)
# l.append(333)
# print(l)

# 出队
# l.pop(0)
# print(l)
# l.pop(0)
# print(l)

# 3. 用列表的insert与pop方法模拟堆栈
# l = []
# # 入队
# l.append(1)
# l.append(22)
# l.append(333)
# print(l)

# 出队
# l.pop()
# print(l)
# l.pop()
# print(l)

# 4、简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，
# 则将商品名，价格，购买个数以三元组形式加入购物列表，
# 如果输入为空或其他非法输入则要求用户重新输入　　
msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}

# buy_car = []
# while True:
#     item = input('请输入商品名')
#     if item in msg_dic.keys():
#         break
#     else:
#         print('输入非法或商品不存在')
# while True:
#     number = input('请输入商品个数')
#     if number.isdigit():
#         break
#     else:
#         print('输入非法')
# buy_car.append([item, msg_dic[item], int(number)])
# print(buy_car)

# 5、有如下值集合 [11,22,33,44,55,66,77,88,99,90]，
# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# big = []
# small = []
# d = {}.fromkeys(['k1', 'k2'], None)
# for x in l:
#     if x > 66:
#         big.append(x)
#     else:
#         small.append(x)
# d['k1'] = big
# d['k2'] = small
# print(d)

# 6、统计s='hello alex alex say hello sb sb'中每个单词的个数
s = 'hello alex alex say hello sb sb'
res = s.split(' ')
d = {}
for i in res:
    d[i] = res.count(i)
print(d)
