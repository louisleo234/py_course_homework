"""
Python基础课第五天作业:    正则表达式匹配练习
日期:                    20210311
学员:                    李明
"""
import re
import os

result_route = os.popen('route -n').read() # os模块执行shell命令
print(result_route)

host_gw = re.match('\w+\s.*\s+\w+\s+Gateway\s.*\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s.*\s.*\s.*\s.*\s.*',
                   result_route).groups()[0]
# print(host_gw) # 确认正则抓取到了需要的数据

print('{0:<5}:{1:<12}'.format('主机网关为', host_gw))