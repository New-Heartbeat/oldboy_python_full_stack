
import time
# 一、time
# 时间分为三种格式
# 1、时间戳：从1970年到现在经过的秒数
#   作用：用于时间间隔的计算
# print(time.time())

# 2、按照某种格式显示的时间 #2023-11-12 19:50:06
#   作用：用于展示时间
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X'))

# 3、结构化的时间
#   作用：用于单独获取时间的某一部分
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_yday)

# 二、datetime
import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=-3))
# print(datetime.datetime.now() + datetime.timedelta(weeks=1))
# print(datetime.datetime.now() + datetime.timedelta(days=3*365))

"""时间模块需要掌握的操作"""
# 1、时间格式的转换
# struct_time -> 时间戳
# s_time = time.localtime()
# print(time.mktime(s_time))

# 时间戳 -> struct_time
# tp_time = time.time()
# print(time.localtime(tp_time))

# 世界标准时间和本地标准时间补充
# print(time.localtime())
# print(time.gmtime())    # 世界标准时间

# struct_time -> 格式化的字符串形式的时间
# s_time = time.localtime()
# print(time.strftime('%Y-%m-%d %X', s_time))

# 格式化的字符串形式的时间 -> struct_time
# print(time.strptime('2023-11-12 20:03:19', '%Y-%m-%d %X'))

# 真正需要掌握的是 format string<--------->timestamp
# '2023-11-12 20:03:19' + 7days

# struct_time = time.strptime('2023-11-12 20:03:19', '%Y-%m-%d %X')
# timestamp = time.mktime(struct_time) + 7*86400
# print(timestamp)

# time.sleep(2)
# print(time.asctime())   # Sun Nov 12 20:10:55 2023

# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
# print(datetime.datetime.fromtimestamp(333333))
