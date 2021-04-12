# -*- coding=utf-8 -*-
"""
Python第二十四天练习:   snmp练习
日期:                 20210407
"""
import sqlite3
from dateutil import parser
from datetime import datetime,timedelta
from cpu_usage_info_collection import mat_line


def cpu_read_db(dbname, last_min=1):
	conn = sqlite3.connect(dbname)
	cursor = conn.cursor()
	now = datetime.now()
	before_last_min = now - timedelta(minutes=last_min)
	cursor.execute("select time, cpu from routerdb where time > '{0}'".format(before_last_min))
	yourresults = cursor.fetchall()

	return [[parser.parse(i[0]),i[1]] for i in yourresults]

if __name__ == '__main__':
	#print(cpu_read_db('deviceinfo.sqlite', 1))
	mat_line(cpu_read_db('deviceinfo.sqlite', 1))