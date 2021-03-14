# """
# Python基础课第六天作业:    接口排序
# 日期:                    20210312
# 学员:                    李明
# """
# import re
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46',
             'eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25',
             'eth 1/101/1/45','eth 1/101/2/8']
# #print(port_list[0].split('/')[0:4])
#
print(sorted(port_list, key=lambda x: (int(x.split('/')[0][4:]),int(x.split('/')[1]),int(x.split('/')[2]),int(x.split('/')[3]))))

