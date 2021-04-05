# -*- coding=utf-8 -*-
"""
Python第十九天练习:    udp传输数据客户端
日期:                 20210331
"""
import socket
import pickle
import struct
import hashlib

def udp_send_data(ip, port, data_list):
	address = (ip, port)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 使用ipv4(af_inet,和udp协议 sock_dgram)
	version = 1
	pkt_type = 1
	seq_id = 1
	for x in data_list:
		# ---header设计--
		# 2字节 版本1
		# 2字节 类型1为请求，2是响应
		# 4字节 ID号
		# 4字节 长度

		# 变长数据部分
		# pickle转换数据

		# hash校验
		# 16字节 MD5
		send_data = pickle.dumps(x)
		header = struct.pack('>HHLL', version, pkt_type, seq_id, len(send_data))
		m = hashlib.md5()
		m.update(header + send_data)
		md5_value = m.digest()  # digest是二进制的hash值
		s.sendto(header + send_data + md5_value, address)
		seq_id += 1
	s.close()

if __name__ == "__main__":
	user_data = ['乾颐堂', [1, 'qytang', 3], {'qytang':1, 'test':3}]
	udp_send_data('172.16.240.6', 6666, user_data)