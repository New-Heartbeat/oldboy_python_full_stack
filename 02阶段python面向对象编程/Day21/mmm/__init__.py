
print('运行了')
x = 111
y = 222

def say():
    pass

print('==========>这是在被导入的__init__.py的文件路径')
import sys
print(sys.path)

# 绝对导入，以包的文件夹作为起始来进行导入
# from mmm.m1 import f1
# from mmm.m2 import f2
# from mmm.m3 import f3

# 相对导入：仅限于包内使用，不能跨出包
# 包内模块之间的导入，推荐使用相对导入
# .：代表当前文件夹
# ..：代表上一层文件夹
from .m1 import f1
from .m2 import f2
from .m3 import f3

# 相对导入不能跨出包，仅限于包内模块彼此之间的引用
# 绝对导入没有任何限制的，所以绝对导入是一种通用的导入
