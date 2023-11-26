
# 1、什么是序列化
#   序列化指的是把内存的数据类型转换成一个特定的格式的内容
#   该格式的内容可用于存储或者传输给其他平台使用

#   内存中的数据类型--->序列化--->特定的格式
#   内存中的数据类型<---序列化<---特定的格式

#   土办法：
#   {'aaa':111} ---> str({'aaa':111}) ---> "{'aaa':111}"
#   {'aaa':111} <--- eval("{'aaa':111}") <--- "{'aaa':111}"

# 2、为何要序列化
#   序列化得到结果==>特定的格式的内容有两种用途
#   01、可用于存储==>用于存档
#   02、传输给其他平台使用==>跨平台数据交互

#   针对用途01的特定格式：可是一种专用的格式=>pickle只有python可以识别
#   针对用途02的特定格式：应该是一种通用、能够被所有语言识别的格式=>json

#   json强调：字符串是双引号

# 3、如何序列化和反序列化
import json

# 序列化
# l = [1, 'aaa', True, False]
# res = json.dumps(l)
# print(res, type(res))

# with open('test.json', mode='wt') as f:
#     json.dump(res, f)

# 反序列化
# l = json.loads(res)
# print(l, type(l))

# with open('test.json', mode='rt') as f:
#     l = json.load(f)
#     print(l, type(l))
#
# l2 = json.loads(l)
# print(l2, type(l2))

# 了解：byte类型也可以直接反解
# l = json.loads(b'[1, "aaa", true, false]')
# print(l, type(l))


# 猴子补丁：在入口处打补丁
# import json
# import ujson
#
# def monkey_patch_json():
#     json.__name__ = 'ujson'
#     json.dumps = ujson.dumps
#     json.loads = ujson.loads
#
# monkey_patch_json() # 在入口文件处运行


# import ujson as json  # 不行


# pickle模块
# import pickle
#
# res = pickle.dumps({1,2,3,4,5})
# print(res, type(res))
#
# s = pickle.loads(res)
# print(s, type(s))

