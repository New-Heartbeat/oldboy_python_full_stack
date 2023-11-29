# 作业：
# 1、编写课上讲解的有参装饰器准备明天默写
# 2：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，
# 在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
# dict = {}
#
# def addtodict(func):
#     def wrapper(*args, **kwargs):
#         number = len(dict)
#         if func not in dict.items():
#             dict[str(number+1)] = func
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @addtodict
# def f1():
#     print('注册')
#
# @addtodict
# def f2():
#     print('登录')
#
# f1()
# f2()
# print(dict)

# 3、 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，
# 日志文件路径可以指定
# 注意：时间格式的获取
# import time
# print(time.strftime('%Y-%m-%d %X'))
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         with open(r'../Day18/homework.log', mode='at') as f:
#             content = time.strftime('%Y-%m-%d %X') + ' 函数' + func.__name__ + ' run'
#             f.write(content + '\n')
#         return res
#     return wrapper
#
# @log
# def home(name):
#     print(f'welcome to homepage, {name}!')
#
# home('egon')


# 4、基于迭代器的方式，用while循环迭代取值字符串、列表、元组、字典、集合、文件对象
# 这里只有文件既是可迭代对象又是迭代器对象
# 其他对象都只是可迭代对象，通过调用iter方法转换成迭代器
# 自己版本.py = 'hello world'
# g1 = 自己版本.py.__iter__()
# while True:
#     try:
#         print(next(g1))
#     except StopIteration:
#         break
#
# with open(r'../Day18/homework.log', mode='rt') as f:
#     while True:
#         try:
#             print(next(f), end='')
#         except StopIteration:
#             break


# 5、自定义迭代器实现range功能
# def func(n):
#     count = 0
#     while count < n:
#         yield count
#         count += 1
#
# g = func(5)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

"""本周 作业"""
# ====================本周选做作业如下====================
# 编写小说阅读程序实现下属功能
# 一：程序运行开始时显示
#     0 账号注册
#     1 充值功能
#     2 阅读小说



# 二： 针对文件db.txt，内容格式为："用户名:密码:金额",完成下述功能
# 2.1、账号注册
def register():
    username = input('username====>')
    password = input('password====>')
    with open(r'../Day18/db.txt', mode='at', encoding='utf-t') as f:
        f.write(f'{username}:{password}:0')
    print(f'用户{username}注册成功')

# 2.2、充值功能
def recharge():
    account = input('请输入充值金额')
    with open(r'../Day18/db.txt', mode='rt', encoding='utf-t') as f:
        pass

# 三：文件story_class.txt存放类别与小说文件路径，如下,读出来后可用eval反解出字典
# {"0":{"0":["倚天屠狗记.txt",3],"1":["沙雕英雄转.txt",10]},"1":{"0":["令人羞耻的爱.txt",6],"1":["二狗的妻子与大草原的故事.txt",5]},}

# 3.1、用户登录成功后显示如下内容，根据用户选择，显示对应品类的小说编号、小说名字、以及小说的价格
"""
0 玄幻武侠
1 都市爱情
2 高效养猪36技
"""

# 3.2、用户输入具体的小说编号，提示是否付费，用户输入y确定后，扣费并显示小说内容，如果余额不足则提示余额不足

# 四：为功能2.2、3.1、3.2编写认证功能装饰器，要求必须登录后才能执行操作

# 五：为功能2.2、3.2编写记录日志的装饰器，日志格式为："时间 用户名 操作(充值or消费) 金额"



# 附加：
# 可以拓展作者模块，作者可以上传自己的作品



