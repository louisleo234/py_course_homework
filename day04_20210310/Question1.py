# -*- coding=utf-8 -*-
"""
Python基础课第四天作业:    正则表达式匹配练习
日期:                    20210310
学员:                    李明
"""
import re
import os
import subprocess
# ifconfig_result = os.popen('ifconfig' + 'ens160').read() 条件不允许，使用习题ifconfig内容

ifconfig_result = 'ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n \
        \tinet 172.16.66.166  netmask 255.255.255.0  broadcast 172.16.66.255\n \
        \tinet6 fe80::250:56ff:feab:59bd  prefixlen 64  scopeid 0x20<link>\n \
        \tether 00:50:56:ab:59:bd  txqueuelen 1000  (Ethernet)\n \
        \tRX packets 174598769  bytes 1795658527217 (1.6 TiB)\n \
        \tRX errors 1  dropped 24662  overruns 0  frame 0\n \
        \tTX packets 51706604  bytes 41788673420 (38.9 GiB)\n \
        \tTX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'
# print(ifconfig_result) 确认ifconfig内容与题目一致

# 正则表达式匹配IP,掩码,广播和MAC地址
ifconfig_filter = re.match('\w+:\s+\w+\S+\s+\w+\s+\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\
(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+::\d+:\w+:\w+:\w+\
\s+\w+\s\d+\s+\w+\s\S+\s+\w+\s(\S+)\s+\S+\s+\S+\s+\S+\s+.*\s+\s+.*\s+\s+.*\s+\s+.*', ifconfig_result).groups()
ip_addr = ifconfig_filter[0]
netmask = ifconfig_filter[1]
boardcast = ifconfig_filter[2]
MAC = ifconfig_filter[3]

# 格式化打印
print('{0:<10}:{1:<14}'.format('ipv4_add', ip_addr))
print('{0:<10}:{1:<14}'.format('netmask', netmask))
print('{0:<10}:{1:<14}'.format('broadcast', boardcast))
print('{0:<10}:{1:<14}'.format('mac_addr', MAC))

# 判断假设网段是否满足与主机IP是同/24网段
ipv4_gw_temp = []
gw_prefix = (input('请输入正确网关的网段信息'))
while gw_prefix != ip_addr[0:4] + ip_addr[4:7] + ip_addr[7:9]:
    print('网段不正确，请重新输入')
    gw_prefix = str(input('重输'))
    if gw_prefix == ip_addr[0:4] + ip_addr[4:7] + ip_addr[7:9]:
        x = gw_prefix + '.254'
    ipv4_gw_temp.append(x)
ipv4_gw = ''.join(ipv4_gw_temp)
print(ipv4_gw)

# 打印网关IP
print('\n我们假设网关IP为最后一位254, 因此网关IP是:' + ipv4_gw + '\n')

# ping网关
ping_result_temp = os.popen('ping ' + ipv4_gw).read()
print(ping_result_temp)
# ping_result_temp = 'PING 172.20.128.65 (172.20.128.65) 56(84) bytes of data.\
# 64 bytes from 172.20.128.65: icmp_seq=1 ttl=64 time=0.047 ms\
# \
# --- 172.20.128.65 ping statistics ---\
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms\
# rtt min/avg/max/mdev = 0.047/0.047/0.047/0.000 ms\
# '

#ping_result = subprocess.call(ping_result_temp, stdout=subprocess.PIPE,shell=True) 使用subprocess方式
re_ping_result = re.match('.*\s+.*(ttl=64)\s.*\s+\.*\S+.*\s+.*\s+.*', ping_result_temp).groups()[0]
if  'ttl' in ping_result_temp:
    print('网关可达')
elif '超时' or 'timeout' or '0 reveived' in ping_result_temp:
    print('网关不可达')
else:
    print('其他错误')
