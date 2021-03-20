# -*- coding=utf-8 -*-
"""
Python基础课第五天作业:    paramiko练习
日期:                    20210318
学员:                    李明
"""
import paramiko
import re

# 定义ssh连接交换机并查看交换机接口
def ssh_conn(ip,username,password,port=22):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    stdin,stdout,stderr = ssh_client.exec_command('show ip interface brief')
    interface_info = stdout.read().decode()
    dict_int = {}
    for line in interface_info.strip().splitlines():
        int_ip = re.findall('(GigabitEthernet\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s\w+\s+\w+\s+\w+.*',line)
        if int_ip:
            dict_int['192.168.1.1'] = int_ip[0]
            print(dict_int)

ssh_conn('172.16.240.20','cisco','123456')
