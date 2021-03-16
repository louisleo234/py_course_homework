# -*- coding=utf-8 -*-
"""
Python基础课第七天作业:    函数练习
日期:                    20210316
学员:                    李明
"""
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

# kamene方法
# def qytang_ping(host):
#     ping_pkt = IP(dst=host)/ICMP()
#     ping_result = sr1(ping_pkt, timeout=2,verbose=False)
#     if ping_result == 0:
#         print('IP可达')
#         return ping_result
#     else:
#         print('IP不可达，5秒后重试')

# os ping函数方法
import os
def os_ping():
    ping_test1 = os.system('ping 127.0.0.1 -c 4')
    if ping_test1 == 0:
        print('IP可达')
    else:
        print('IP不可达')
    return ping_test1

os_ping()