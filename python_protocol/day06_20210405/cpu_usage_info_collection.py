# -*- coding=utf-8 -*-
"""
Python第二十二天练习:    matplotlib搜集show process cpu配置, 线形图展示
日期:                 20210405
"""
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文
plt.rcParams['font.family'] = 'sans-serif'
import paramiko
import re
import datetime
import time


def mat_line(cpu_usage_list):
	# 调节图形大小, 宽, 高
	fig = plt.figure(figsize=(6,6))
	# 一共一行, 每行一图, 第一图
	ax = fig.add_subplot(111)

	# 处理X轴时间格式
	import matplotlib.dates as mdate
	#ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
	# 设置时间标签显示格式
	ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M')) # 设置时间标签显示格式

	# 处理Y轴百分比格式
	import matplotlib.ticker as mtick
	ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

	# 把cpu_usage_list数据，拆分成X轴的时间和Y轴的利用率
	x = []
	y = []

	for time, cpu in cpu_usage_list:
		x.append(time)
		y.append(cpu)

	# 添加主题和注释
	plt.title('路由器CPU利用率')
	plt.xlabel('采集时间')
	plt.ylabel('CPU利用率')

	fig.autofmt_xdate() # X轴拥挤时可以自适应

	# 实线红色
	ax.plot(x,y,linestyle='solid', color='r', label='R1')
	# 虚线黑色
	#ax.plot(x,y,linestyle='dashed', color='b', label='R1')

	# 如果有多套数据，可以在一幅图里绘制双线
	# ax.plot(x2,y2,linestyle='dashed', color='b',label='R2')

	# 设置说明的位置
	ax.legend(loc='upper left')

	# 保存到图片
	plt.savefig('result1.png')
	# 绘制图形
	plt.show()


def ssh_singlecmd(ip, username, password, cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip, port=22, username=username,password=password,timeout=5, compress=True)
		stdin, stdout, stderr = ssh.exec_command(cmd)
		x = stdout.read().decode()
		ssh.close()
		return x
	except Exception as e:
		print('%stErrorn %s' %(ip, e))

def get_cpu_usage():
	show_result = ssh_singlecmd('172.16.240.20','cisco','123456', 'show process cpu')
	cpu_usage_list = {}
	for line in show_result.strip().split('\n'):
		show_cpu_result = re.match(r'^CPU utilization for five seconds: (\d+)\%\/\d+\%; one minute: \d+\%; five minutes: \d+\%', line)
		if show_cpu_result:
			temp_time = time.strftime("%H:%M")
			cpu_usage_list = {time.strftime("%H:%M"): show_cpu_result.groups()[0]}
			return cpu_usage_list
	# 		app_bytes_list.append(app_bytes.groups()[2])
	# mat_bing(app_bytes_list, app_name_list)

if __name__ == '__main__':
	counters = [30, 53, 12, 45]
	protocols = ['http协议', 'ftp协议', 'rdp协议', 'qq协议']
	from datetime import datetime, timedelta
	from random import randrange
	now = datetime.now()
	time_cpu_usage = []
	for x in range(-12, 13):
		time_cpu_usage.append([(now + timedelta(hours=x)), randrange(101)])
	mat_line(time_cpu_usage)
