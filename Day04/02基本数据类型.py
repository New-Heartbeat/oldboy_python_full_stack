"""
基本数据类型
"""
# 1、数字类型
# 1.1 整型int
# 作用：记录整数值，如年龄、个数等
age = 18

# 1.2 浮点型float
# 作用：记录薪资等
salary = 3.3

# 1.3 数字类型的其他用途
# 计算用途(int 和 float 可以相加)
print(3 + 7.5)
# 比较用途
print(19 > 18)

# 2、字符串类型
# 作用：用于记录描述
# 定义：用引号('', "", """""")括起来
name = 'egon'
describe = """按表格撒娇给"""
# 字符串只能和字符串相加,但可以和 int 相乘
# print('egon' + 18) # 报错
print('egon' + '18')
print('*' * 10)

# 3、列表：索引对应值，索引从0开始，0代表第一个
# 作用：记录多个值，并且可以按照索引取指定位置的值
# 定义：在[]内用逗号分隔开多个任意类型的值，一个值称之为一个元素
l = [10, 3.1, 'aaa', ['bbb', 'ccc'], 'ddd']
print(l[-1])
# 列表嵌套
print(l[3][1])

# 4、字典：key对应值，其中key通常为字符串类型，所以key对值可以有描述功能
# 作用：用来存多个值，每个值都有唯一一个key与其对应，key对值有描述性功能
# 定义：在{}内用逗号分开多个 key:value
info = {
    'name': 'egon',
    'age': 18,
    salary: 3.3
}
print(info['age'])

# 字典嵌套
students_info = [
    {'name': '张三', 'age': 18, 'score': 60},
    {'name': '李四', 'age': 17, 'score': 80},
    {'name': '王五', 'age': 20, 'score': 90},
]
print(students_info[-1]['name'])

# 5、布尔bool
# 作用：用来记录真假这两种状态
# 定义：
is_ok = True
print(type(is_ok))
# 其他使用：通常用来当作判断的条件，将在if判断中用到
