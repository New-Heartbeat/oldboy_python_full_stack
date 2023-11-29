import configparser

config = configparser.ConfigParser()
config.read('test.ini')

# 获取sections
# print(config.sections())

# 获取某一section下所有的option
# print(config.options('section1'))

# 获取items
# print(config.items('section1'))

# res = config.get('section1', 'age')
# print(res, type(res))

# res = config.getint('section1', 'age')
# print(res, type(res))
