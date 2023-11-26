
# 一、send传值
# 会将send函数的参数赋值给yield表达式左边的变量
# 第一次传值只能是None
# def dog(name):
#     print('道哥%s准备吃东西啦...' % name)
#     while True:
#         x = yield None
#         print('道哥%s吃了%s' % (name, x))
#
# g = dog('alex')
# g.send(None) # 等同于next(g)
#
# g.send('一根骨头')    # 把'一根骨头'赋值给yield表达式左边的x
# g.send('一瓶可乐')
# g.send(['肉包子', 'aaa'])
# g.close()
# g.send('肉包子')   # 关闭之后无法传值

# 二、返回值
# 返回yield后面的值
# def dog(name):
#     print('道哥%s准备吃东西啦...' % name)
#     while True:
#         x = yield 1111
#         print('道哥%s吃了%s' % (name, x))
#
# g = dog('alex')
# res = g.send(None) # 等同于next(g)
# print(res)
#
# res = g.send('一根骨头')
# print(res)
#
# res = g.send('肉包子')
# print(res)

def dog(name):
    food_list = []
    print('道哥%s准备吃东西啦...' % name)
    while True:
        x = yield food_list
        print('道哥%s吃了%s' % (name, x))
        food_list.append(x)

g = dog('alex')
res = g.send(None) # 等同于next(g)
print(res)

res = g.send('一根骨头')
print(res)

res = g.send('肉包子')
print(res)

