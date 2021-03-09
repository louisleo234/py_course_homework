"""
Python基础课第三天作业1:    正则表达式匹配练习
日期:                     20210309
学员:                     李明
"""
import re

show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
result = re.match('(\w+)\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s+\w+\s+\
(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+),\s+\w+\s+(\d:\d+:\d+),\
\s+\w+\s+(\d+),\s+\w+\s+(\w+)',show_conn).groups()
# 打印变量result了解参数位置 print(result) #('TCP', '172.16.1.101:443', '172.16.66.1:53710', '0:01:09', '27575949', 'UIO')

time = list(result[3])
time.insert(1, '小时')
time.insert(5, '分钟')
time.insert(9, '秒')

# 转time列表后，删除time列表中不要的：内容
del time[2]
del time[5]


# 打印并格式化输出匹配出的内容
print('{0:<20}:{1:>4}'.format('protocol', result[0]))
print('{0:<20}:{1:>17}'.format('server', result[1]))
print('{0:<20}:{1:>18}'.format('localserver', result[2]))
print('{0:<20}:{1:>11}'.format('idle', "".join(time)))
print('{0:<20}:{1:>9}'.format('bytes', result[4]))
print('{0:<20}:{1:>4}'.format('flags', result[5]))
