# 1、算数运算符
print("10/3的结果是：", 10 / 3)
print("10//3的结果是：", 10 // 3)
print("10%3的结果是：", 10 % 3)
print("10**3的结果是：", 10 ** 3)

# 2、比较运算符

# 3、赋值运算符
# 3.1 =：变量的赋值
# 3.2 增量赋值
age = 18
age += 1

# 3.3 链式赋值
# x = 10
# y = x
# z = y
z = y = x = 10
print(x, y, z)
print(id(x), id(y), id(z))

# 3.4 交互赋值
m = 10
n = 20
print(m, n)
# m = n
# n = m
# print(m, n) # 这里并不会交换m、n的值

# temp = m
# m = n
# n = temp
m, n = n, m
print(m, n)

# 3.5 解压赋值
salary = [111, 222, 333, 444, 555]
# mon0 = salary[0]
# mon1 = salary[1]
# mon2 = salary[2]
# mon3 = salary[3]
# mon4 = salary[4]
mon0, mon1, mon2, mon3, mon4 = salary   # 对应的变量名必须一一对应
print(mon0, mon1, mon2, mon3, mon4)

# * 会将没有对应关系的值存成列表
# * 可以帮助我们取两头的值，无法取中间的值
x, y, z, *_ = salary = [111, 222, 333, 444, 555]
print(x, y, z)
print(_)

*_, x, y, z = salary = [111, 222, 333, 444, 555]
print(x, y, z)
print(_)

x, y, z = dict = {'自己版本.py': 1, 'b': 2, 'c': 3}
print(x, y, z)
