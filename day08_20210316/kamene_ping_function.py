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
def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2,verbose=False)
    if ping_result:
        return ip, True
    else:
        return ip, False

# os ping函数方法
# import os
# def os_ping():
#     ping_test1 = os.system('ping 127.0.0.1 -c 1')
#     if ping_test1 == 0:
#         print('IP可达')
#     else:
#         print('IP不可达')
#     return ping_test1


if __name__ == '__main__':
    ping_pong = qytang_ping('172.16.240.20')
    if ping_pong[1]:
        print(f'{ping_pong[0]} 可达！')
    else:
        print(f'{ping_pong[0]} 不可达!')