# -*- coding=utf-8 -*-
"""
Python第十九天练习:    udp传输数据服务端
日期:                 20210331
"""
import socket
import sys
import struct
import hashlib
import pickle

address = ("172.16.240.6", 6666)  # 设置udp server
# 创建UDP套接字Socket, AF_INET为IPv4, SOCK_DGRAM为Datagram就是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 套接字绑定到地址,元组(host, port)
s.bind(address)

print('UDP服务器就绪!等待客户数据!')
while True:
	try:
		# 接收UDP套接字的数据,2048为接收的最大数据量,多的直接丢弃!
		# 不推荐使用UDP传大量数据
		recv_source_data = s.recvfrom(2048)
		rdata, addr = recv_source_data
		header = rdata[:12]  # 获取udp头部信息
		uppack_header = struct.unpack('>HHLL', header) # 解包 udp头部
		version = uppack_header[0]  # 解包 udp头部,得到version
		pkt_type = uppack_header[1] # 解包 udp头部, 得到数据包类型
		seq_id = uppack_header[2] # 解包 udp头部,得到发送序列
		length = uppack_header[3] # 解包 udp头部,得到数据包长度

		rdata = rdata[12:]
		data = rdata[:length]
		md5_recv = rdata[length:]

		m = hashlib.md5()
		m.update(header + data)
		md5_value = m.digest()
		# 如果客户发来空数据,就退出循环
		if md5_recv == md5_value:
			print('=' * 80)
			print("{0:<30}:{1:<30}".format("数据源自于", str(addr)))
			print("{0:<30}:{1:<30}".format("数据序列号", seq_id))
			print("{0:<30}:{1:<30}".format("数据长度", length))
			print("{0:<30}:{1:<30}".format("数据内容", str(pickle.loads(data))))

		# 如果客户发来的数据不为空,就显示数据,与源信息
	except KeyboardInterrupt:
		sys.exit()

s.close()

