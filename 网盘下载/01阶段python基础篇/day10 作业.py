# 一.关系运算
# 有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
pythons = {'alex', 'egon', 'yuanhao', 'wupeiqi', 'gangdan', 'biubiu'}
linuxs = {'wupeiqi', 'oldboy', 'gangdan'}
# 1. 求出既报名python又报名linux课程的学员名字集合
print(pythons & linuxs)
# 2. 求出所有报名的学生名字集合
print(pythons | linuxs)
# 3. 求出只报名python课程的学员名字
print(pythons - linuxs)
# 4. 求出没有同时这两门课程的学员名字集合 　　
print(pythons ^ linuxs)

# 二.去重
# 1. 有列表l=['自己版本.py','b',1,'自己版本.py','自己版本.py']，列表元素均为可hash类型，
# 去重，得到新列表,且新列表无需保持列表原来的顺序
l1 = ['自己版本.py', 'b', 1, '自己版本.py', '自己版本.py']
print(list(set(l1)))
# 2.在上题的基础上，保存列表原来的顺序
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
# 3.去除文件中重复的行，肯定要保持文件内容的顺序不变
# 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
l3 = [
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'alex', 'age': 73, 'sex': 'male'},
    {'name': 'egon', 'age': 20, 'sex': 'female'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
]

l4 = []
for i in l3:
    if i not in l4:
        l4.append(i)
print(l4)

