
# 无论是import还是from...import...在导入模块时都涉及到查找问题
# 优先级：
#   1、内存（内置模块）
#   2、从硬盘找：按照sys.path中存放的文件的顺序依次查找要导入的模块

# import sys
# print(sys.path)

# import foo  # 内存中已经有foo了
# foo.say()
#
# import time
# time.sleep(10)  # 10s里删除foo.py文件，下面的import并不会报错，因为已经加载到内存中去了
#
# import foo
# foo.say()

# 了解：sys.modules查看已经加载到内存中的模块
# import sys
# print(sys.modules)

# 导入aa文件夹里的模块
# import sys
# sys.path.append(r'D:\老男孩python全栈\Day21\aa')
# import a
# a.say()


