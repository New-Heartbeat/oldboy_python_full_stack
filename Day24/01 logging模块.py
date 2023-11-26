# 参考链接：https://www.cnblogs.com/linhaifeng/articles/6384466.html#_label12
import logging

# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

logging.basicConfig(
    # 日志输出位置
    # filename='access.log',  # 不指定，默认打印到终端
    # 日志格式
    format='[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s',
    # 时间
    datefmt='%Y-%m-%d %X',
    # 级别
    level=10,
)


# logging.debug('调试debug')
# logging.info('消息info')
# logging.warning('警告warn')
# logging.error('egon提现失败')
# logging.critical('严重critical')





