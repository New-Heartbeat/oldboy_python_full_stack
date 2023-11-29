# 作业：
# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
#     egon male 18 3000
#     alex male 38 30000
#     wupeiqi female 28 20000
#     yuanhao female 28 10000

# 要求:
# 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
keys = ['name', 'sex', 'age', 'salary']
# l1 = []
with open(r'../Day20/day20homework.txt', mode='rt') as f:
    # for line in f:
    #     info = line.strip('\n').split(' ')
    #     d = dict(zip(keys, info))
    #     l1.append(d)
    l1 = [dict(zip(keys, line.strip('\n').split(' '))) for line in f]
print(l1)

# 2 根据1得到的列表,取出薪资最高的人的信息
# res = max(l1, key=lambda x: x['salary'])
# print(res)

# 3 根据1得到的列表,取出最年轻的人的信息
# res = min(l1, key=lambda x: x['age'])
# print(res)

# 4、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
# names = ['egon', 'alex_sb', 'wupeiqi', 'yuanhao']
# new_names = [name.upper() for name in names]
# print(new_names)

# 5、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
# names = ['egon', 'alex_sb', 'wupeiqi', 'yuanhao']
# name = [name for name in names if not name.endswith('sb')]
# l = [len(name) for name in names if not name.endswith('sb')]
# new_names = dict(zip(name, l))
# print(new_names)

# 6、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
# with open(r'../Day20/day20homework.txt', mode='rt') as f:
#     res = max(len(line) for line in f)
#     print(res)

# 7、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
# with open(r'../Day20/day20homework.txt', mode='rt') as f:
    # g = (len(line) for line in f)
    # print(g)
    # print(sum(g))
    # res1 = sum(len(line) for line in f)
    # res2 = sum(len(line) for line in f)
    # print(res1)
    # print(res2)
# print(g)
# print(sum(g))

# 8、思考题
# with open('a.txt') as f:
#     g=(len(line) for line in f)
# print(sum(g)) #为何报错？
# 报错：ValueError: I/O operation on closed file.
# 生成器g本身没有值，在文件关闭后，想调里面的值但是文件已经关闭

# 9、文件shopping.txt内容如下

# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# 求总共花了多少钱？

# 打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]

# 求单价大于10000的商品信息,格式同上
# l2 = [info for info in l1 if int(info['salary']) > 10000]
# print(l2)

# 10、思考：判断下述说法是否正确
#     题目1：
#     1、应该将程序所有功能都扔到一个模块中，然后通过导入模块的方式引用它们
#     2、应该只将程序各部分组件共享的那一部分功能扔到一个模块中，然后通过导入模块的方式引用它们

# 题目2：
# 运行python文件与导入python文件的区别是什么？
# 运行的python文件产生的名称空间何时回收，为什么？
# 导入的python文件产生的名称空间何时回收，为什么？
