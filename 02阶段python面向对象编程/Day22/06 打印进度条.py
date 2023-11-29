
# 进度条打印
# print('[%-50s]' % '#')
# print('[%-50s]' % '##')
# print('[%-50s]' % '###')
import time

# res = ''
# for i in range(50):
#     res += '#'
#     time.sleep(0.2)
#     print('\r[%-50s]' % res, end='')

recv_size = 0
total_size = 33333

while recv_size < total_size:
    time.sleep(0.2)
    recv_size += 1024
    # print(recv_size)
    percent = recv_size/total_size
    if percent > 1:
        percent = 1
    res = '#'*int(50 * percent)
    print('\r[%-50s] %d%%' % (res, int(100*percent)), end='')

