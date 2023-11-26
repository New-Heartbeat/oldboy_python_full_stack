# 1、作用

# 2、定义
# d = {'k1': 111, (1, 2): 'abc'}
# print(d[(1, 2)])
#
# d = {}
# print(d, type(d))
#
# d = dict(x=1, y=2, z=3)
# print(d, type(d))

# 3、类型转换
# info = [
#     ['name', 'egon'],
#     ('age', 18),
#     ['gender', 'male']
# ]
# d = dict(info)
# print(d)

# 快速初始化一个字典
# keys = ['name', 'age', 'gender']
# d = {}.fromkeys(keys, None)
# d = {}.fromkeys(keys, ['egon', '18', 'male'])
# print(d)

# 4、使用
# 优先掌握的操作
# 4.1 按key存取：可存可取
# d = {'k1': 111}
# # 针对赋值操作，key存在，则修改；key不存在，则创建新的键值对
# d['k1'] = 11111
# d['k2'] = 222
# print(d)

# 4.2 长度 len
# d = {'k1': 111, 'k2': 222, 'k1': 333}
# print(d)
# print(len(d))

# 4.3 成员运算：根据key
# 4.4 删除
# d = dict(x=1, y=2, z=3)
# 通用删除 del
# del d['x']
# print(d)

# pop删除：根据key删除元素,返回删除key对应的那个value值
# res = d.pop('y')
# print(d, res)

# popitem删除：随机删除，返回元组（删除的key，删除的value）
# res = d.popitem('y')    # 报错
# res = d.popitem()
# print(d, res)

# 4.5 取键、值、键值对
# keys()、values()、items() => 在python3中得到的是老母鸡
# d = dict(x=1, y=2, z=3)
# print(d.keys())
# print(d.values())
# print(d.items())
# print(list(d.keys()))   # 想要得到“蛋” 可用list转换

# 需要掌握的内置方法
# d = dict(x=1, y=2, z=3)
# d.clear()

# d.update()
# d.update(dict(k1=1, k=2, z=33))
# print(d)

# d.get()：根据key取值，容错性好，key不存在也不报错，返回None
# d = dict(x=1, y=2, z=3)
# print(d['k1'])   # 不存在则报错
# print(d.get('k1'))
# res = d.get('k1', '取不到则返回第二个参数')
# print(res)

# d.setdefault()：key有则不添加，返回value
# info = {'name': 'egon', 'age': 16}
# res = info.setdefault('gender', 'male')
# print(info, res)
# res = info.setdefault('name', 'alex')
# print(info, res)
