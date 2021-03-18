# -*- coding=utf-8 -*-
"""
Python基础课第八天作业:    函数练习
日期:                    20210317
学员:                    李明
"""
import paramiko
import os
import re
from paramiko import *

# 基于ssh定义查找linux网关函数
def ssh_get_route_gw(ip,username,password,port=22,cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    y = stdout.read().decode()
    list1 = []
    for line in y.split('\n'):
        gw = re.findall('(0.0.0.0).+(192.168.228.2).+(UG)', line)
        for i in gw:
            if i != []:
                list1.append(i)
    return print('网关为\n',list1[0][1].strip())


if __name__ == '__main__':
    ssh_get_route_gw('192.168.228.129','root','123456')