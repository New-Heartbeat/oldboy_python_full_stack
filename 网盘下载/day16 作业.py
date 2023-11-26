# 今日作业：
# 1、函数对象优化多分支if的代码练熟
def f1():
    # 0、注册功能：用户输入账号名、密码、金额，按照固定的格式存入文件db.txt
    print('注册')
    username = input('请输入用户名')
    password = input('请输入密码')
    account = input('请输入金额')
    with open(r'../Day16/db.txt', mode='at') as f:
        f.write(username+' '+password+' '+account)

def f2():
    # 1、登录功能：用户名不存在，要求必须先注册，用户名存在&输错三次锁定
    # 登录成功后记录下登录状态
    username = input('请输入用户名')
    password = input('请输入密码')
    if 1:
        print('登录')
        global login_status
        login_status = True
    else:
        print('')

def f3():
    print('充值')

def f4():
    print('转账')

def f5():
    print('提现')

def f6():
    print('查询余额')

func_dict = {
    '0': [0, '退出'],
    '1': [f1, '注册'],
    '2': [f2, '登录'],
    '3': [f3, '充值'],
    '4': [f4, '转账'],
    '5': [f5, '提现'],
    '6': [f6, '查询余额'],
}
# print(func_dict)
# login_status = False
# while True:
#     print('欢迎来到系统'.center(50, '*'))
#     for key in func_dict:
#         print(key, ' ', func_dict[key][1])
#
#     operation_code = input('请输入指令')
#     if not operation_code.isdigit():
#         print('请输入数字指令')
#         continue
#
#     if operation_code == '0':
#         break
#
#     for key in func_dict:
#         if key == operation_code:
#             if operation_code not in ['1', '2'] and not login_status:
#                 print('请登录后使用该功能')
#                 break
#             func_dict[key][0]()
#             break


# 2、编写计数器功能，要求调用一次在原有的基础上加一
#         温馨提示：
#             I:需要用到的知识点：闭包函数+nonlocal
#             II:核心功能如下：
#                 def counter():
#                     x+=1
#                     return x
#
#         要求最终效果类似
#             print(couter()) # 1
#             print(couter()) # 2
#             print(couter()) # 3
#             print(couter()) # 4
#             print(couter()) # 5
# def f1():
#     x = 0
#     def counter():
#         nonlocal x
#         x += 1
#         print(x)
#         return x
#     return counter
#
# res = f1()
# res()
# res()
# res()
# res()
# res()


# ====================周末作业====================
# 编写ATM程序实现下述功能，数据来源于文件db.txt
# 0、注册功能：用户输入账号名、密码、金额，按照固定的格式存入文件db.txt
# 1、登录功能：用户名不存在，要求必须先注册，用户名存在&输错三次锁定，登录成功后记录下登录状态（提示：可以使用全局变量来记录）

# 下述操作，要求登录后才能操作
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额





