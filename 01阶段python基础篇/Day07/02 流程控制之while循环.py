# 1、循环的语法与基本使用
count = 0
sum = 0
while count < 5:
    sum += count
    count += 1
print(sum)

# 2、死循环与效率问题
# 纯计算无io的死循环会导致致命的效率问题
# while True:
#     1 + 1

# 3、循环的应用
# 4、循环的结束
# 4.1 while + break
# 4.2 改变条件结束循环
# 5、循环嵌套
# 6、while + continue：结束本次循环，直接进入下一次
count = 0
while count < 6:
    count += 1
    if count == 4:
        continue
    print(count)

# 7、while + else：else包含的代码会在while循环结束后，
# 并且while循环是在没有被break打断循环的情况下结束后，运行
# else是针对break的
while True:
    break
else:
    print('while + else')

count = 0
while count < 3:
    print(count)
    count += 1
    if count > 5:
        break
else:
    print('3次循环后 仍未达到目标结果')

