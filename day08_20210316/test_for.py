"""
Python基础课第七天作业:    while循环练习
日期:                    20210316
学员:                    李明
"""
list1 = ['aaa', 111, (4,5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4,5)]
empty_list = []
#
# for x in list1:
#     for y in list2:
#         if x == y:
#             empty_list.append(x)
# print(empty_list)

def find_same(l1,l2):
    for x in l1:
        for y in l2:
            if x == y:
                empty_list.append(x)

find_same(list1, list2)
print(empty_list)
