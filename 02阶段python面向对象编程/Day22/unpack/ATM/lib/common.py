
import time
from config.setting import LOG_PATH

def logger(msg):
    with open(LOG_PATH, mode='at', encoding='utf-8') as f:
        t = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write('%s %s\n' % (t, msg))
