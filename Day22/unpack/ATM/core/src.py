
from lib.common import logger

def register():
    print('注册')
    logger('egon刚刚注册了')

def login():
    print('登录')
    logger('egon刚刚登录了')

def withdraw():
    print('提现')
    logger('egon刚刚提现了3毛钱')

def query():
    print('查询余额')
    logger('egon刚刚给alex转了3亿冥币')

func_dict = {
    '0': ['退出', exit],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['提现', withdraw],
    '4': ['查询余额', query]
}

def run():
    while True:
        for k in func_dict:
            print(k, func_dict[k][0])
        code = input('请输入指令').strip()
        if code in func_dict.keys():
            func_dict[code][1]()
        else:
            print('请输入相应指令，傻叉')



