# 1、接收用户的输入

# 在python3中，input会将用户输入的所有内容都存成字符串类型
# username = input("请输入您的账号")
# print(username, type(username))

# age = int(input("请输入您的年龄"))
# int只能将纯整数的字符串转成整型
# print(age)

# 在python2中：
# raw_input():用法与python3的input一样
# input():要求用户必须输入一个明确的数据类型，输入的是什么类型，就会存成什么类型。方便开发者但不方便使用者


# 2、格式化输出
# 知乎链接：https://zhuanlan.zhihu.com/p/110406030

# 2.1 %
# 值按照位置与%s一一对应，少一个多一个都不行
res1 = "name: %s  age:%s" % ('egon', '18')
res2 = "name: %s  age:%s" % (18, 'egon')
res3 = "name: %(name)s  age:%(age)s" % {'name': 'egon', 'age': 18}
print(res1)
print(res2)
print(res3)

# %d只能接收int
# %s可以接收任意类型，包括列表、字典

# 2.2 str, format：兼容性好
res = '我的名字是 {0}{0}{0} 我的年龄是 {1}{1}'.format('egon', 18)
print(res)

# 打破位置的限制
res = '我的名字是{name}我的年龄是{age}'.format(age=18, name='egon')
print(res)

# 四舍五入
print('{salary:.3f}'.format(salary=123.12351))  # 精确到小数点后三位

# 2.3 f：python3.5以后才推出
# x = input('your name')
# y = input('your age')
# res = f'我的名字是{x} 我的年龄是{y}'
# res = f'我的名字是{{{x}}} 我的年龄是{y}
# print(res)

# f的新用法：{}内的字符串可以被当作表达式运行
print(f'{10+3}')
# f'{print(”aa“)}'
