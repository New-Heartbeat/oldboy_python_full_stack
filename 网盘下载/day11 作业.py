# 一：今日作业：
# 1、编写文件copy工具
# old_file = input('请输入原文件的绝对路径：')
# new_file = input('请输入要复制到的绝对路径：')
# with open(old_file, mode='rt') as f1, open(new_file, mode='wt') as f2:
#     for line in f1:
#         f2.write(line)
#     res = f1.read()
#     f2.write(res)


# 2、编写登录程序，账号密码来自于文件
# input_username = input('请输入用户名')
# input_password = input('请输入密码')
#
# with open(r'D:\老男孩python全栈\Day11\user_info.txt', mode='rt') as f:
#     for line in f:
#         username, password = line.strip('\n').split(':')
#         if input_username == username and input_password == password:
#             print('login successful')
#             break
#     else:
#         print('login error')

# 3、编写注册程序，账号密码来存入文件
def signup():
    input_username = input('请输入用户名')
    input_password = input('请输入密码')
    with open(r'D:\老男孩python全栈\Day11\user_info.txt', mode='at') as f:
        info = input_username + ':' + input_password + '\n'
        f.write(info)
        print('注册成功')
    return


# 二：周末综合作业：
# 2.1：编写用户登录接口
# 1、输入账号密码完成验证，验证通过后输出"登录成功"
# 2、可以登录不同的用户
# 3、同一账号输错三次锁定，（提示：锁定的用户存入文件中，这样才能保证程序关闭后，该用户仍然被锁定）

def login():
    # 读取出用户信息
    user_info = {}
    with open(r'D:\老男孩python全栈\Day11\user_info.txt', mode='rt') as f:
        for line in f:
            username, password = line.strip('\n').split(':')
            user_info[username] = password
    print(user_info)

    i = 0
    banned_user = []
    while True:
        input_username = input('请输入用户名')
        with open(r'D:\老男孩python全栈\Day11\user_ban.txt', mode='rt') as f:
            for line in f:
                banned_user.append(line.strip('\n'))
        if input_username in banned_user:
            print('该用户已被锁定，请用其他用户名登录')
            i += 1
            continue
        if input_username in user_info:
            for j in range(3):
                input_password = input('请输入密码')
                i += 1
                if input_password == user_info[input_username]:
                    print('登录成功')
                    i = 100
                    break
                else:
                    if j == 2:
                        print('输错密码三次，账号已被锁定')
                        with open(r'D:\老男孩python全栈\Day11\user_ban.txt', mode='at') as f:
                            f.write(input_username + '\n')
                    else:
                        print('密码不正确，请重新输入')
        else:
            print('用户名不存在')
            i += 1
        if i == 100:
            break
        elif i >= 10:
            print('已输错10次，系统退出')
            break
    return


# 2.2：编写程序实现用户注册后（注册到文件中），可以登录（登录信息来自于文件）
# 提示：
while True:
    msg = """
    0 退出
    1 登录
    2 注册
    """
    print(msg)
    cmd = input('请输入命令编号>>: ').strip()
    if not cmd.isdigit():
        print('必须输入命令编号的数字，傻叉')
        continue

    if cmd == '0':
        break
    elif cmd == '1':
        # 登录功能代码（附加：可以把之前的循环嵌套，三次输错退出引入过来）
        login()
        break
    elif cmd == '2':
        # 注册功能代码
        signup()
    else:
        print('输入的命令不存在')

# 思考：上述这个if分支的功能否使用其他更为优美地方式实现
