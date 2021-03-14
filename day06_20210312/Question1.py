"""
Python基础课第六天作业:    字典使用练习
日期:                    20210312
学员:                    李明
"""
import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n\
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

# 创建空字典用于后面存参数
asa_dict = {}
asa_list = []
for x in asa_conn.split('\n'):
    re_result = re.match('\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s\w+\s\
(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s\w+\s\d{1,2}:\d{1,2}:\d{1,2},\s\w+\s(\d+),\s\w+\s(\w+)', x).groups()
    asa_list.append(x.split(' '))
"""
转列表方便后续使用户
[(0, ['TCP', 'Student', '192.168.189.167:32806', 'Teacher', '137.78.5.128:65247,', 'idle', '0:00:00,', 'bytes', '74,'
, 'flags', 'UIO']), (1, ['TCP', 'Student', '192.168.189.167:80', 'Teacher', '137.78.5.128:65233,', 'idle', '0:00:03,',
 'bytes', '334516,', 'flags', 'UIO'])]
"""
src = 'src'
src_ip = asa_list[0][2][0:15]
src_ip2 = asa_list[1][2][0:15]
src_port = asa_list[0][2][16:21]
src_port2 = asa_list[1][2][16:21]
dst = 'dst'
dst_ip = asa_list[0][4][0:12]
dst_ip2 = asa_list[1][4][0:12]
dst_port = asa_list[0][4][13:18]
dst_port2 = asa_list[1][4][13:18]
bytes = asa_list[0][8][0:2]
bytes1 = asa_list[1][8][0:6]
flags = asa_list[0][10]
flags1 = asa_list[1][10]

# 给字典创建键值
asa_dict={(src_ip, src_port, dst_ip, dst_port): (bytes,flags), (src_ip2, src_port2, dst_ip2, dst_port2): (bytes1, flags1)}
print('打印分析后的字典!')
print(asa_dict)

# 格式化输出
print('\n格式化打印输出\n')
print('{0:^8}:{1:<16}|{2:^10}:{3:^12}|{4:^10}:{5:<16}|{6:^12}:{7:^12}\n{8:^8}:{9:^16}|{10:^10}:{11:^12}'.format('src',
src_ip,'src_port',src_port,'dst',dst_ip, 'dst_port', dst_port, 'bytes',bytes,'flags',flags))
print('='*102)
print('{0:^8}:{1:<16}|{2:^10}:{3:^12}|{4:^10}:{5:<16}|{6:^12}:{7:^12}\n{8:^8}:{9:^16}|{10:^10}:{11:^12}'.format('src',
src_ip2,'src_port',src_port2,'dst',dst_ip2, 'dst_port', dst_port2, 'bytes',bytes1,'flags',flags1))
print('='*102)