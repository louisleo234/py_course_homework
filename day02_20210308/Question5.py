import re

str1 = 'Port-channel1.189       192.168.189.254     YES     CONFIG  up  up'

result = re.match('(\w+-\w+\d+\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(YES)\s+(CONFIG)\s+(\w+)\s+(\w+)', str1).groups()
print(result)
print('-'*64)
print('{0:<8}:{1:>18}'.format('接口', result[0]))
print('{0:<8}:{1:>16}'.format('IP地址', result[1]))
print('{0:<8}:{1:>3}'.format('状态', result[4]))