# -*- coding=utf-8 -*-
"""
Python基础课第五天作业:    函数练习
日期:                    20210319
学员:                    李明
"""
import paramiko
import re
from hashlib import md5
import hashlib
import time

# 定义ssh连接交换机并查看交换机接口
def ssh_conn(ip,username,password,port=22):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    stdin,stdout,stderr = ssh_client.exec_command('show run')
    interface_info = stdout.read().decode()
    global cut_int_info
    cut_int_info = interface_info[316:]

    return cut_int_info

def liming_check_diff(ip,username,password,port=22):
    ssh_conn(ip,username,password,port=22)
    original_conf_md5 = hashlib.md5(cut_int_info.encode()).hexdigest()
    while True:
        if hashlib.md5(cut_int_info.encode()).hexdigest() == original_conf_md5:
            print(hashlib.md5(cut_int_info.encode()).hexdigest())
            time.sleep(5)
            ssh_conn(ip, username, password, port=22)

        else:
            print(hashlib.md5(cut_int_info.encode()).hexdigest())
            print('MD5 value changed')
            break
liming_check_diff('192.168.228.135','cisco','123456')

