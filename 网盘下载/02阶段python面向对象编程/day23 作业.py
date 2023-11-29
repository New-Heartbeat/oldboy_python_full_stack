# 作业：
#     1、把登录与注册的密码都换成密文形式
import hashlib

# def register():
#     username = input('username===>').strip()
#     password = input('password===>').strip()
#     m1 = hashlib.md5(password.encode('utf-8'))
#     encrypt_pwd = m1.hexdigest()
#     with open(r'../Day23/user.txt', mode='at') as f:
#         f.write(f'{username}:{encrypt_pwd}\n')
# register()

# def login():
#     print('登录：')
#     username = input('username===>').strip()
#     password = input('password===>').strip()
#     m1 = hashlib.md5(password.encode('utf-8'))
#     encrypt_pwd = m1.hexdigest()
#     with open(r'../Day23/user.txt', mode='rt') as f:
#         for line in f:
#             user_info = line.strip('\n').split(':')
#             if user_info[0] == username and user_info[1] == encrypt_pwd:
#                 print('登录成功')
#                 break
#         else:
#             print('用户名或密码不正确')
# login()
#     2、文件完整性校验（考虑大文件）

# with open(r'../Day23/user.txt', mode='rb') as f:
#     res1 = f.read(10)
#     m1 = hashlib.md5(res1)
#     f.seek(-10, 2)
#     res2 = f.read()
#     m1.update(res2)
#     check = m1.hexdigest()
#     print(res1)
#     print(res2)
#     print(check)


#     3、注册功能改用json实现
import json
"""
注册：
第一种方式：
1、先读json文件，反序列化为字典
2、字典添加新的用户信息键值对，再序列化为json格式
3、将json格式内容写入到json文件中
第二种方式：√√√√
1、注册用户信息之间多个换行，这样可以用追加写模式，节省内存
2、同时读取的时候，用for linf in f读取每一行的json格式
3、再将json格式反序列化为字典
"""
# def register():
#     username = input('username===>').strip()
#     password = input('password===>').strip()
#     m1 = hashlib.md5(password.encode('utf-8'))
#     encrypt_pwd = m1.hexdigest()
#     d = {username: encrypt_pwd}
#     with open(r'../Day23/user.json', mode='at') as f:
#         # f.write(f'{username}:{encrypt_pwd}\n')
#         json.dump(d, f)
#         f.write('\n')
# register()


# def login():
#     print('登录：')
#     username = input('username===>').strip()
#     password = input('password===>').strip()
#     m1 = hashlib.md5(password.encode('utf-8'))
#     encrypt_pwd = m1.hexdigest()
#     with open(r'../Day23/user.json', mode='rt') as f:
#         for line in f:
#             res = json.loads(line)
#             if username in res and res[username] == encrypt_pwd:
#                 print('登录成功')
#                 break
#         else:
#             print('用户名或密码不正确')
# login()

#     4、项目的配置文件采用configparser进行解析




