# -*- coding=utf-8 -*-
import sqlite3
import re
import hashlib
import paramiko

def liming_ssh(ip, username, password, port=22, cmd='ls'):
	ssh = paramiko.SSHClient() # 加载调用ssh client的实例
	ssh.load_system_host_keys() #读取系统ssh key
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #主机没有ssh key使用
	#连接主机
	ssh.connect(ip,port=port,username=username,password=password,timeout=5, compress=True)
	#罗列目录
	stdin, stdout, stderr = ssh.exec_command(cmd)
	#读取标准输出
	x = stdout.read().decode()
	return x

def get_config_md5(ip, username='cisco', password='123456'):
	try:
		device_config_raw = liming_ssh(ip, username, password, cmd='show run')
		split_result = re.split(r'\r\nhostname \S+\r\n', device_config_raw)
		device_config = device_config_raw.replace(split_result[0],'').strip()
		m = hashlib.md5()
		m.update(device_config.encode())
		md5_value = m.hexdigest()
		return device_config, md5_value
	except Exception:
		return

device_list = ['172.16.240.20']
username = 'cisco'
password = '123456'

def write_config_md5_to_db():
	conn = sqlite3.connect('qytangconfig.sqlite')
	cursor = conn.cursor()
	for device in device_list:
		config_and_md5 = get_config_md5(device, username='cisco', password='123456')
		cursor.execute('select * from config_md5 where ip=?', (device,))
		md5_result = cursor.fetchall()
		if not md5_result:
			cursor.execute("insert into config_md5(ip, config, md5) values (?, ?, ?)", (device,
																						config_and_md5[0],
																						config_and_md5[1]))
			conn.commit()
		else:
			if config_and_md5[1] != md5_result[0][2]:
				cursor.execute("update config_md5 set config=?, md5=? where ip=?", (config_and_md5[0],
																					config_and_md5[1],
																					device))
				conn.commit()
			else:
				continue
	cursor.execute('select * from config_md5')
	all_result = cursor.fetchall()
	for x in all_result:
		print(x[0],x[2])
	conn.close()


if __name__ == '__main__':
	import os
	if os.path.exists('qytangconfig.sqlite'):
		os.remove('qytangconfig.sqlite')
	conn = sqlite3.connect('qytangconfig.sqlite')
	cursor = conn.cursor()

	# 执行创建表任务
	cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5 varchar(1000))")
	conn.commit()
	conn.close()
	write_config_md5_to_db()