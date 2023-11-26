
import random

# print(random.random())
# print(random.randint(1, 3))     # [1, 3]
# print(random.randrange(1, 3))   # [1, 3)
# print(random.choice([1, 'aaa', [4, 5]]))
# print(random.sample([1, 'aaa', [4, 5]], 2))
# print(random.uniform(1, 3))
#
# item = [1, 3, 5, 7, 9]
# print(random.shuffle(item))
# print(item)

# 应用：随机验证码
# x1w296

def make_code(n=6):
    res = ''
    for i in range(n):
        s1 = chr(random.randint(65, 90))
        s2 = str(random.randint(0, 9))
        random_str = random.choice([s1, s2])
        res += random_str
    return res
res = make_code()
print(res)
