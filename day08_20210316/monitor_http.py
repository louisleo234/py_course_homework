"""
Python基础课第七天作业:    while循环练习
日期:                    20210316
学员:                    李明
"""
import os
import re
import time

port_collection = os.popen('netstat -tulnp').read()
#print(port_collection)

for x in port_collection.split('\n'):
    if re.match('tcp.+(0.0.0.0:80)|(0.0.0.0:8000).+LISTEN.+', x):
        print('http(TCP/80)端口已经打开')
        break
    else:
        print('等待一秒重新开始监控')
        time.sleep(1)


