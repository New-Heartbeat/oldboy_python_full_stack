
# 函数内一旦存在yield关键字，调用函数并不会马上运行函数体
# 会返回一个生成器对象，生成器即自定义生成器
def func():
    print('第一次')
    yield 1
    print('第二次')
    yield 2
    print('第三次')
    yield 3
    print('第四次')

g = func()
# print(g)
# 生成器就是迭代器
# g.__iter__()
# g.__next__()

# 会触发函数体代码的运行，然后遇到yield停下来
# 将yield后的值当作本次调用的结果返回
res1 = g.__next__()
print(res1)

res2 = g.__next__()
print(res2)

res3 = g.__next__()
print(res3)

res4 = g.__next__()
print(res4)

