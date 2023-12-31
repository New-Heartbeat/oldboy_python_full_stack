# 垃圾回收机制（了解）
# 知乎链接：https://zhuanlan.zhihu.com/p/108683483

# 0、堆区栈区
# 栈区：存放的是变量名与内存地址的对应关系，所以可以简单理解为：变量名存内存地址
# 堆区：存放的是变量值

# 强调：只站在变量名的角度去谈一件事情
#   变量名的赋值(x=y)，还有变量名的传参(print(x))，传递的都是栈区的数据
#   而且栈的数据是变量名与内存地址的对应关系，或者说是对值的引用
#   python是引用传递

l = [111, 222, 333]
l2 = l
l[0] = 'balabala'
print(l)
print(l2)

l2[1] = 444
print(l2)
print(l)

# 1、引用计数
# 直接引用和间接引用都会增加引用计数
# 值的引用计数一旦为0，其占用的内存地址就会被解释器的垃圾回收机制清除掉
x = 10  # 直接引用
print(id(x))

l = ['自己版本.py', x]  # 间接引用,这里列表存放的是'自己版本.py'的内存地址、10的内存地址
print(id(l[1]))

d = {'mmm': x}  # 间接引用
print(id(d['mmm']))

x = 123
print(l[1])

# 2、标记清除
l1 = [111, ]
l2 = [222, ]

# 循环引用
l1.append(l2)   # l1=[值111的内存地址，l2列表的内存地址]
l2.append(l1)   # l2=[值222的内存地址，l1列表的内存地址]

print(id(l1[1]))
print(id(l2))

print(l1)
print(l2)

# del l1
# del l2
# 此时111、222引用计数不为0，但已经取不到这两个值了=>内存泄露
# 标记清除会在内存不够的时候扫描栈区解决循环应用的问题

# 3、分代回收
# 背景：基于引用计数的回收机制，每次回收内存，都需要把所有对象的引用计数都遍历一遍，这是非常消耗时间的
# 于是引入了分代回收来提高回收效率，分代回收采用的是用“空间换时间”的策略。

# 分代回收的核心思想是：在历经多次扫描的情况下，都没有被回收的变量，
# gc机制就会认为，该变量是常用变量，gc对其扫描的频率会降低



