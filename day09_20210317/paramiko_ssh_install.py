# -*- coding=utf-8 -*-
# 自定义ssh连接函数，用于linux，最终版
import paramiko
import re

def liming_ssh(ip, username, password, port=22, cmd='ls'):
	import paramiko
	ssh = paramiko.SSHClient() # 加载调用ssh client的实例
	ssh.load_system_host_keys() #读取系统ssh key
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #主机没有ssh key使用
#连接主机
	ssh.connect(ip,port=22,username=username,password=password,timeout=5, compress=True)
#罗列目录
	stdin, stdout, stderr = ssh.exec_command(cmd)
#读取标准输出
	return stdout.read().decode()

def ssh_get_route(ip, username, password, port=22):
	route_result = liming_ssh(ip, username, password, cmd='route -n')
	for route in route_result.split('\n')[2:-1]:
		re_route = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
							r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
							r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
							r'(\w+)\s+\d+\s+\d+\s+\d+ \w+',
							route.strip())
		if re_route:
			if re_route.groups()[1] == 'UG':
				return re_route.groups()[0]

if __name__ == '__main__':
	#print(liming_ssh('172.16.240.8','root','123456',cmd='pwd'))
	print('网关为:')
	print(ssh_get_route('172.16.240.8','root','123456'))
