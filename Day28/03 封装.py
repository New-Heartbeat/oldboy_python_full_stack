# 隐藏属性
# 一、如何隐藏属性
# Python的Class机制采用双下划线开头的方式将属性隐藏起来（设置成私有的）
# 但其实这仅仅只是一种变形操作，类中所有双下滑线开头的属性都会在
# 类定义阶段、检测语法时自动变成“_类名__属性名”的形式
class Foo:
    __N = 0

    def __init__(self) -> None:
        self.__N = 10


# print(Foo.__N)   # AttributeError: type object 'Foo' has no attribute '__N'
obj = Foo()
# print(obj.__N)  # AttributeError: 'Foo' object has no attribute '__N'
print(obj.__dict__)  # {'_Foo__N': 10}

# 1.在类外部无法直接访问双下滑线开头的属性，但知道了类名和属性名就可以拼出名字
# _类名__属性，然后就可以访问了
# 所以说这种操作并没有严格意义上地限制外部访问，仅仅只是一种语法意义上的变形。
print(obj._Foo__N)

# 2.在类内部是可以直接访问双下滑线开头的属性的
# 比如self.__N=10，因为在类定义阶段类内部双下滑线开头的属性统一发生了变形。

# 3.变形操作只在类定义阶段发生一次,在类定义之后的赋值操作，不会变形。
obj.__M = 100
print(obj.__dict__)
print(obj.__M)


# 二、为什么隐藏属性
# 1.开放数据接口
# 将数据隐藏起来就限制了类外部对数据的直接操作，然后类内应该提供相应的接口来允许类外部间接地操作数据
# 接口之上可以附加额外的逻辑来对数据的操作进行严格地控制
class People:
    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        print(self.__name)

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            print("姓名必须是字符串格式！")
            return
        self.__name = new_name


peo1 = People("egon")
peo1.get_name()
# peo1.set_name(12312)
peo1.set_name("EGON")
peo1.get_name()


# 2.开放函数接口
# 目的的是为了隔离复杂度，例如ATM程序的取款功能
# 该功能有很多其他功能组成，比如插卡、身份认证、输入金额、打印小票、取钱等
# 而对使用者来说,只需要开发取款这个功能接口即可,其余功能我们都可以隐藏起来
class ATM:
    def __card(self):  # 插卡
        print("插卡")

    def __auth(self):  # 身份认证
        print("用户认证")

    def __input(self):  # 输入金额
        print("输入取款金额")

    def __print_bill(self):  # 打印小票
        print("打印账单")

    def __take_money(self):  # 取钱
        print("取款")

    def withdraw(self):  # 取款功能
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


atm_obj = ATM()
atm_obj.withdraw()
