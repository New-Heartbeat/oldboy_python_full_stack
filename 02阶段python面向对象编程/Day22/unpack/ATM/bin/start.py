
import sys
import os

# from ..core import src
# src.run()
# 报错：ImportError: attempted relative import with no known parent package
# 相对导入不能跳出父文件夹

# print(__file__)   # 当前文件的绝对路径
# print(sys.path)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()



