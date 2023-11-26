# 一：编写函数，（函数执行的时间用time.sleep(n)模拟）
import time
# 二：编写装饰器，为函数加上统计时间的功能
# def timmiy(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
#
# @timmiy
# def index(x, y):
#     time.sleep(2)
#     print('index====>', x, y)
# index(1, 2)
# 三：编写装饰器，为函数加上认证的功能

# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式
# login_status = False
# def auth(db_type):
#     def outter(func):
#         def wrapper(*args, **kwargs):
#             global login_status
#             if login_status:
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 username = input('your name=>')
#                 pwd = input('your password=>')
#
#                 if db_type == 'file':
#                     print('从文件验证')
#                     with open(r'../Day17/db.txt', mode='rt') as f:
#                         for line in f:
#                             res = eval(line)
#                             print(res)
#                             if username == res['name'] and pwd == res['password']:
#                                 print('登录成功')
#                                 login_status = True
#                                 res = func(*args, **kwargs)
#                                 return res
#                 elif db_type == 'mysql':
#                     print('从mysql数据库验证')
#                     if 1:
#                         print('登录成功')
#                         login_status = True
#                         res = func(*args, **kwargs)
#                         return res
#                 else:
#                     print('没有该来源')
#                 print('请登录后再使用')
#         return wrapper
#     return outter
#
# @auth('mysql')
# def index(x, y):
#     time.sleep(2)
#     print('index====>', x, y)
#
# @auth('file')
# def home(name):
#     print('welcome to homepage %s!' % name)
#
# @auth('file')
# def endpage(name):
#     print('to the end, welcome back %s' % name)
#
# index(1, 2)
# home('egon')
# endpage('2024年')
# 五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录
# 超过了超时时间，则必须重新登录
login_status = False
tick = time.time()
def auth(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        global login_status, tick
        if not login_status or now - tick > 2:
            print('开始认证'.center(20, '='))
            username = input('username===>')
            pwd = input('password===>')
            with open(r'../Day17/db.txt', mode='rt') as f:
                for line in f:
                    user_info = eval(line)
                    if user_info['name'] == username and user_info['password'] == pwd:
                        print('登录成功'.center(20, '='))
                        login_status = True
                        tick = time.time()
                        res = func(*args, **kwargs)
                        return res
            print('登录失败'.center(20, '='))
        else:
            res = func(*args, **kwargs)
            return res
    return wrapper

@auth
def home(name):
    print('welcome to homepage, %s!' % name)

home('alex')
time.sleep(3)
home('egon')
home('alex')


# 六：选做题
# 思考题（选做），叠加多个装饰器，加载顺序与运行顺序，可以将上述实现的装饰器叠加起来自己验证一下
# @deco1 # index=deco1(deco2.wrapper的内存地址)
# @deco2 # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3 # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass
