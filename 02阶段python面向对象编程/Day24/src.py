
# 拿到日志的产生者
# 第一个：kkk
# 第二个：

import settings
import logging
from logging import config, getLogger

config.dictConfig(settings.LOGGING_DIC)
# logger1 = getLogger('kkk')
# logger1.info('这是一条info日志')

logger2 = getLogger('专门的采集')
logger2.info('专门的采集的一条日志')

# 补充两个重要额外知识
# 1、日志名的命名
#       日志命名是区别日志业务归属的一种非常重要的标识
# 2、日志轮转
#       日志记录着程序运行过程中的关键信息


