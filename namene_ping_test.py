#!/usr/bin/python3.6
# -*- coding=utf-8 -*-

# from kamene.all import *
# ping_one_reply = sr1(IP(dst='172.16.240.1')/TCP(), timeout = 1, verbose=False)
# ping_one_reply.show()

# num = range(0,401)
# i = 0
# for i in num:
# 	print('send mail ')if i % 20 == 0 else 555
# 	i += 1
# 	print(i)

import random

section1 = random.randint(1,255)
section2 = random.randint(0,255)
section3 = random.randint(0,255)
section4 = random.randint(0,254)

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
print(random_ip)