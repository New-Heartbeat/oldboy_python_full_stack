# 1、编写文件修改功能，调用函数时，传入三个参数（修改的文件路径，要修改的内容，修改后的内容）既可完成文件的修改
# def file_revise(src_file, old_str, new_str):
#     """
#     件修改功能：修改目标文件内容
#     :param src_file: 目标文件路径
#     :param old_str: 要修改的内容
#     :param new_str: 修改后的内容
#     :return: None
#     """
#     with open(src_file, mode='rt') as f:
#         res = f.read().replace(old_str, new_str)
#
#     with open(src_file, mode='wt') as f:
#         f.write(res)
#
#
# file_revise('../Day13/自己版本.py.txt', 'egon', 'alex')

# 2、编写tail工具
# 3、编写登录功能
# 4、编写注册功能
# 5、编写用户认证功能

# 选做题：编写ATM程序实现下述功能，数据来源于文件db.txt
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额

# 选做题中的选做题：登录功能
# 用户登录成功后，内存中记录下该状态，上述功能以当前登录状态为准，必须先登录才能操作
