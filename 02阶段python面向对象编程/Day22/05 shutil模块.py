import shutil

# 1、copy()：复制文件
# res = shutil.copy('day22作业.py', r'D:\老男孩python全栈')
# print(res)

# res = shutil.copy2('day22作业.py', r'D:\老男孩python全栈')
# print(res)

# 2、copyfileobj()
# 描述：将一个文件的内容拷贝到另一个文件中，如果目标文件本身就有内容，
# 来源文件的内容会把目标文件的内容覆盖掉。如果文件不存在它会自动创建一个。
# 语法：shutil.copyfileobj(fsrc, fdst[, length=16*1024])
# with open(r'./06 打印进度条.py', mode='r', encoding='utf-8') as f1, \
#         open(r'../day22作业.py', mode='w+', encoding='utf-8') as f2:
#     shutil.copyfileobj(f1, f2)

# 3、copytree()
# 描述：复制整个目录文件，不需要的文件类型可以不复制
# import os
# path1 = os.path.join(os.getcwd(), "shutile")
# path2 = os.path.join(os.getcwd(), "bbb", "ccc")
# shutil.copytree(path1, path2, ignore=shutil.ignore_patterns("abc.txt", "bcd.txt"))

# 4、move()
# 描述：移动文件或文件夹
# 语法：shutil.move(src, dst)

# 5、disk_usage()
# 描述：查看磁盘使用信息，计算磁盘总存储，已用存储，剩余存储信息。
# res = shutil.disk_usage('D:')
# print(res)

# 6、make_archive()
# 描述：压缩打包
# 语法：make_archive(base_name, format, root_dir=None, base_dir=None)
# base_name： 压缩包的文件名，也可以是压缩包的路径。
# format： 压缩或者打包格式 "zip", "tar", "bztar"or "gztar"
# root_dir : 将哪个目录或者文件打包（也就是源文件）,默认将当前路径文件夹打包

# 将Day21文件夹打包到 Day22/archive文件夹下，压缩文件名为Day21.gz.tar
# shutil.make_archive('./archive/Day21', 'gztar', r'../Day21')

# 7、unpack_archive解压缩
# 语法：unpack_archive(filename, extract_dir=None, format=None)

# 将上面获得的压缩文件解压缩到unpack文件夹下（文件夹不存在时会自动创建）
# shutil.unpack_archive(r'./archive/Day21.tar.gz', r'./unpack')


