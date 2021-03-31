# -*- coding=utf-8 -*-
"""
Python基础课第十二天作业:    函数练习
日期:                    20210322
学员:                    李明
"""
import paramiko
import time
import pprint


def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    chan = ssh.invoke_shell(width=300)
    time.sleep(1)
    x = chan.recv(2048).decode() # 获取返回结果
    if enable and '>' in x: # 判断是否有enable密码情况
        chan.send('enable'.encode()) #发送命令
        chan.send(b'\n') # 回车
        chan.send(enable.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
    elif not enable and '>' in x:
        print('需要配置enable密码')
        return
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(65535).decode()
        if verbose:
            print(x)
    chan.close()
    ssh.close()


if __name__ == '__main__':
    qytang_multicmd('172.16.240.20',
                    'cisco',
                    '123456',
                    ['terminal length 0',
                     'show version',
                     'config ter',
                     'router ospf 1',
                     'network 192.168.1.0 0.0.0.255 area 0'],
                    enable='cisco123',
                    wait_time=1,
                    )