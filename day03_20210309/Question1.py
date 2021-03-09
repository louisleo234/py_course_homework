"""
Python基础课第三天作业1:    正则表达式匹配练习
日期:                     20210309
学员:                     李明
"""
import re

MAC = '16654a2.74f7.0326 DYNAMIC Gi1/0/11'

# 正则匹配并取VLAN ID,同时转列表赋值给变量方便后续使用
VLAN_ID = list(re.match('(\d{1,3}).*', MAC).groups())

# 正则匹配并取MAC地址信息,同时转列表赋值给变量方便后续使用
MAC_add = list(re.match('\d{1,3}(\w+\.\w+\.\w+)\s+\w+\s+\w+/\d/\d+', MAC).groups())

# 正则匹配并取接口类型信息,同时转列表赋值给变量方便后续使用
Type = list(re.match('\d{1,3}\w+\.\w+\.\w+\s+(\w+)\s+\w+/\d/\d+', MAC).groups())

# 正则匹配并取接口号信息,同时转列表赋值给变量方便后续使用
Interface = re.match('\d{1,3}\w+\.\w+\.\w+\s+\w+\s+(\w+/\d/\d+)', MAC).groups()

# 打印并格式化输出匹配出的内容
print('{0:<12}:{1:>4}'.format('VLAN ID',(VLAN_ID)[0]))
print('{0:<12}:{1:>15}'.format('MAC', (MAC_add)[0]))
print('{0:<12}:{1:>8}'.format('Type', (Type)[0]))
print('{0:<12}:{1:>9}'.format('Interface', (Interface)[0]))
