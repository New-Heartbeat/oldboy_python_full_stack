
import m1

# ImportError: cannot import name 'x' from partially initialized module 'm1' (most likely due to a circular import) (D:\老男孩python全栈\Day21\m1.py)

# 屎上雕花
# 解决方法：把导入语句定义到函数中去
m1.f1()
