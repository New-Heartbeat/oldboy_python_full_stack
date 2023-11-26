
def register(name: "必须传入名字傻叉", hobbies: tuple, age: int=18, ) -> int:
    print(name)
    print(hobbies)
    print(age)
    return 111


register(1, 'egon', 'hello world')
register('egon',  ('篮球', '游戏'), 18)
print(register.__annotations__)
