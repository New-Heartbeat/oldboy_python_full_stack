# 作业（必做题）：
# 1. 使用while循环输出1 2 3 4 5 6     8 9 10
# 2. 求1-100的所有数的和
# 3. 输出 1-100 内的所有奇数
# 4. 输出 1-100 内的所有偶数
# 5. 求1-2+3-4+5 ... 99的所有数的和
# 6. 用户登陆（三次机会重试）
# 7：猜年龄游戏
"""
要求：
    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
"""
# 8：猜年龄游戏升级版（选做题）
"""
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如果猜对了，就直接退出
"""

# 1. 使用while循环输出1 2 3 4 5 6     8 9 10
# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)

# 2. 求1-100的所有数的和
# sum = 0
# count = 0
# while count < 100:
#     count += 1
#     sum += count
# print(sum)

# 3. 输出 1-100 内的所有奇数
# sum = 0
# count = 0
# while count < 100:
#     count += 1
#     if count % 2:
#         sum += count
# print(sum)

# 5. 求1-2+3-4+5 ... 99的所有数的和
# sum = 0
# count = 0
# while count < 99:
#     count += 1
#     if count % 2:
#         x = 1
#     else:
#         x = -1
#     sum += count*x
# print(sum)

# 6. 用户登陆（三次机会重试）
# count = 0
# while count < 3:
#     # 用户名：burningJ
#     # 密码：123456
#     count += 1
#     user_name = input('请输入用户名')
#     pwd = input('请输入密码')
#     if user_name == 'burningJ' and pwd == '123456':
#         print("登录成功")
#         break
#     elif user_name != 'burningJ':
#         print(f'用户名不正确, 还有{3-count}次机会')
#     else:
#         print(f'密码不正确, 还有{3-count}次机会')
# else:
#     print("对不起，由于多次输错，账号已锁定")

# 8：猜年龄游戏升级版（选做题）
"""
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如果猜对了，就直接退出
"""
try_cnt = 0
age = 18
while True:
    try_cnt += 1

    # 每猜三次询问一次是否要继续
    if try_cnt % 3 == 1 and try_cnt > 3:
        # 确保回答在下面列表内
        answer_list = ['y', 'Y', 'n', 'N']
        while True:
            answer = input("是否还想继续玩, 请回答y/n")
            if answer not in answer_list:
                print("请输入正确的格式：['y', 'Y', 'n', 'N']")
            else:
                break
        if answer == 'n' or answer == 'N':
            break

    # 确保猜的年龄为 int 类型
    while True:
        guess_age = input("请猜年龄")
        if guess_age.isdigit():
            guess_age = int(guess_age)
            break
        else:
            print('请输入整数猜年龄')

    if guess_age == age:
        print(f"恭喜猜对了！您总共猜了{try_cnt}次")
        break
    else:
        print(f'真遗憾，猜错了!您总共猜了{try_cnt}次')
