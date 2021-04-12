# -*- coding=utf-8 -*-
"""
Python第二十四天练习:   snmp练习
日期:                 20210407
"""
import os
import sqlite3
from snmpv2_get import snmpv2_get
import datetime
import time

def get_info_writedb(ip, rocommunity, dbname, seconds):
	if os.path.exists(dbname):
		os.remove(dbname)
	conn = sqlite3.connect(dbname)
	cursor = conn.cursor()

	cursor.execute("create table routerdb(id INTEGER PRIMARY KEY AUTOINCREMENT, time timestamp, cpu int)")

	while seconds > 0:
		cpu_info = snmpv2_get(ip, rocommunity, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7")[1]
		time_info = datetime.datetime.now()
		cursor.execute("insert into routerdb (time, cpu) values ('{0}', {1})".format(time_info, int(cpu_info)))
		time.sleep(5)
		seconds -=5
		conn.commit()

if __name__ == '__main__':
	get_info_writedb("172.16.240.20", "tcpipro", "deviceinfo.sqlite", 1000)
