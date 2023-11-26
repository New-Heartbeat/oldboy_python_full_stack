# -*- coding: utf-8 -*-

import subprocess

obj = subprocess.Popen('dir D:', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       )
# print(obj)
res = obj.stdout.read()
print(res.decode('gbk'))

# err_res = obj.srderr.read()
# print(err_res.decode('utf-8'))
