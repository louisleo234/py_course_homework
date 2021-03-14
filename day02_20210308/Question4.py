Department1 = 'Security'
Department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456
end = 'The END!'

#字符串表达式 %s %(value)方式
line1 = '%s:%s%s%s%s%s%s' %('Department1 name', Department1, 'Manager:'.rjust(10, ' '), depart1_m, \
                            'COURSE FEES:'.rjust(14, ' '),COURSE_FEES_SEC, end.rjust(12, ' '))
line2 = '%s:%s%s%s%s%s%s' %('Department2 name', Department2, 'Manager:'.rjust(12, ' '), depart2_m, \
                            'COURSE FEES:'.rjust(16, ' '), COURSE_FEES_Python, end.rjust(16, ' '))
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

#字符串格式化方法 '...{}...'format(values)
line3 = '{0:16}:{1:8}{2:>9}:{3:<9}{4:>11}:{5:<15}{6:>10}'.format('Department1 name', Department1, 'Manager', depart1_m,\
                                                     'COURSE FEES', COURSE_FEES_SEC, end)
line4 = '{0:16}:{1:8}{2:>9}:{3:<9}{4:>5}:{5:<14}{6:>11}'.format('Department2 name', Department2, 'Manager', depart2_m,\
                                                     'COURSE FEES', COURSE_FEES_Python, end)
length1 = len(line3)
print('='*length1)
print(line3)
print(line4)
print('='*length1)
