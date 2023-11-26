
print('模块foo==>')

x = 5

def get():
    print(x)

def change():
    global x
    x = 0

def say():
    print('我还活在内存中呢')

__all__ = ['x', 'get']  # 可以用来控制 * 的使用

# print(__name__)
# 1、当foo.py被运行时，其值为'__main__'
# 2、当foo.py被当作模块导入时，其值为'foo'
if __name__ == '__main__':
    get()
    change()

