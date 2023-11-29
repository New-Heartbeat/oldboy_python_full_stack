# 2.5 命名关键字参数（了解）
# 在定义函数时，*后定义的参数，称为命名关键字参数
# 特点：命名关键字实参必须按照key=value的形式为其传值
# def func(x, y, *, 自己版本.py, b):
#     print(x, y)
#     print(自己版本.py, b)
# func(1, 2)
# func(1, 2, b=111, 自己版本.py=222,)

# def func(x, y, *, 自己版本.py=111, b):
#     print(x, y)
#     print(自己版本.py, b)
# func(1, 2, b=5)

# def func(x, y=111, *args, z, **kwargs): # 位置在 * 与 ** 形参之间
#     return
