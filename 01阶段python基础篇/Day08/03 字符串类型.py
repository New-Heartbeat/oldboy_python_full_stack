# 1、作用
# 2、定义
msg = str('hello')
print(msg)
# 3、类型转换
# str 可以把任意其他类型都转成字符串
res = str({'自己版本.py': 123})
print(res, type(res))

# 4、使用：内置方法
# 4.1 优先掌握
# 4.1.1 按索引取值（正向取+反向取）：只能取
msg = 'hello world'
print(msg[0])
print(msg[-1])

# 只能取
# msg[0] = 'H'

# 4.1.2 切片：索引的拓展应用（顾头不顾尾）
print(msg[:])
print(msg[0:5])
print(msg[0:5:2])  # 2是步长

# 反向步长
print(msg[0:5:-1])  # 结果为空
print(msg[5:0:-1])
print(msg[::-1])

# 4.1.3 长度 len
print(len(msg))

# 4.1.4 成员运算 in 和 not in
# 判断一个字符串是否存在于一个大字符串中

# 4.1.5 移除字符串左右两侧的符号strip
msg = '           egon     '
res = msg.strip()  # 默认去掉的空格
print(msg)  # 不会改变原值
print(res)  # 产生了新值

msg = '*****egon****'
print(msg.strip('*'))

# 了解：strip只去两边，不去中间
msg = '*****eg**on****'
print(msg.strip('*'))

msg = '**/=-***egon***/=-*'
print(msg.strip('*/=-'))

# 4.1.6 切分split：把一个字符串按照某种分隔符进行切分，得到一个列表
# 默认分隔符是空格
info = "egon 18 male"
print(info.split())
info = "egon:18:male"
print(info.split(':'))

# 指定分隔次数（了解）
print(info.split(':', 1))

# 4.1.7 循环
for x in info:
    print(x)

# 4.2、需要掌握
# 4.2.1 strip,lstrip,rstrip

# 4.2.2 lower,upper

# 4.2.3 startswith,endswith
print("alex is sb".startswith("alex"))
print("alex is sb".endswith("sb"))

# 4.2.4 format的三种玩法

# 4.2.5 split rsplit
info = "egon:18:male"
print(info.split(':'))
print(info.rsplit(':'))
print(info.rsplit(':', 1))

# 4.2.6 join：把列表拼接成字符串
res = info.split(':')
print(":".join(res))  # 按照某个分隔符号，把元素全为字符串的列表拼接成一个字符串

# 4.2.7 replace
msg = 'you can you up no can no bb'
print(msg.replace("you", 'YOU'))
print(msg.replace("you", 'YOU', 1))

# 4.2.8 isdigit
# 判断字符串是否由纯数字组成
print('123'.isdigit())
print('12.3'.isdigit())

# 4.3、了解
# 4.3.1 find, rfind, index, rindex, count
msg = 'hello egon hahaha'
# 返回起始索引
print(msg.find('aaa.txt'))
print(msg.find('egon'))
print(msg.index('aaa.txt'))
print(msg.index('egon'))
# 找不到
print(msg.find('xxx'))  # 返回-1，代表找不到
# print(msg.index('xxx')) # 抛出异常

print(msg.count('h'))
print(msg.count('ha'))

# 4.3.2 center, ljust, rjust, zfill
print('egon'.center(50, '*'))
print('egon'.ljust(50, '*'))
print('egon'.rjust(50, '*'))
print('egon'.zfill(50))

# 4.3.3 expandtabs
msg = 'hello\tworld'
print(msg.expandtabs(2))  # 设置制表符代表的空格数为2

# 4.3.4 capitalize, swapcase, title
print('hello WORLD Egon'.capitalize())  # 全小写
print('hello WORLD Egon'.swapcase())  # 翻转大小写
print('hello WORLD Egon'.title())  # 每个单词首字母大写

# 4.3.5 is数字系列
# 4.3.6 is其他
print('abC'.islower())
print('ABC'.isupper())
print('Hello World'.istitle())
print('AB12bsaC'.isalnum())  # 字母或数字组合
print('AB12bsaC'.isalpha())  # 由字母组成
print("*"*50)
num1 = b'4'  # bytes
num2 = u'4'  # unicode,python3中无需加u就是unicode
num3 = '四'  # 中文数字
num4 = 'Ⅳ'  # 罗马数字
# isdigit
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
print(num4.isdigit())

# isnumeric
print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())

# isdecimal
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())
