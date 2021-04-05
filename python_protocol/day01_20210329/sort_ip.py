# -*- coding=utf-8 -*-
"""
Python第十七天练习:    ip过滤脚本
日期:                 20210329
"""

from socket import inet_aton
import struct
import ipaddress

ip_list = ['172.16.12.123',
		   '192.16.12.3',
		   '172.16.12.234',
		   '10.16.12.12',
		   '172.16.12.23',
		   ]

def sort_ip(ips):
	# inet_aton(ip) 转换IP到直接字符串
	# >>> inet_aton("172.16.1.1")
	# b'\xac\x10\x01\x01'
	# 了解struct https://docs.python.org/2/library/struct.html,Python提供struct模块来解决bytes和其他二进制数据类型的转换
	# struct.unpack("!L", inet_aton("172.16.1.1"))
	# (2886729985)
	# 根据整数排序, 然后返回排序后的ips列表
	# return sorted(ips, key=lambda ip: struct.unpack("!L", inet=aton(ip))[0])
	return sorted(ips, key=lambda ip: ipaddress.ip_address(ip))

if __name__ == '__main__':
	print(sort_ip(ip_list))
