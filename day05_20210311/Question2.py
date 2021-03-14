"""
Python基础课第五天作业:    列表练习
日期:                    20210311
学员:                    李明
"""

l1 = [4,5,7,1,3,9,0]
l2 = l1.copy()

for i in zip(l1, sorted(l2)):
    print(i)