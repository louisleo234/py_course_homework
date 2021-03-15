"""
Python基础课第七天作业:    文件操作练习
日期:                    20210315
学员:                    李明
"""
import os

# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1','w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2','w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3','w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# os.mkdir('qytang4')
# os.mkdir(('qytang5'))

#列出当前工作目录和文件
#print(os.listdir(os.getcwd()))

#
key_word = 'qytang'
file_dir = []
files = []

# 判断当前工作目录下有哪些目录，如果是目录就记录到file_dir列表中
for i in os.listdir(os.getcwd()):
    if os.path.isdir(i):
        file_dir.append(i)
#        print(file_dir)

# 判断目录并进入到目录中，再判断哪些是文件，记录到files列表中，最后判断关键字，如果文件中存在则记录到列表files
for x in file_dir:
    os.chdir(x)
    temp_lists = os.listdir()
    for y in temp_lists:
        if os.path.isfile(y):
          if key_word in open(y).read():
            files.append(y)

# 格式化打印
print('文件中包含关键字\'qytang\'的有:')
print('{0:>34}'.format(files[0]))
print('{0:>34}'.format(files[1]))