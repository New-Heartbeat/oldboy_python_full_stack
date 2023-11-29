import time

with open(r'access.log', mode='rb') as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(0.3)
        else:
            print(line.decode('utf-8'), end='')

