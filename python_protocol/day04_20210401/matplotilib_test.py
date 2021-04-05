# -*- coding=utf-8 -*-
"""
Python第二十天练习:    解决matplotlib模块乱码问题, 饼状图
日期:                 20210401
"""

from matplotlib import pyplot as plt
import matplotlib
print(matplotlib.matplotlib_fname())
plt.rcParams['font.sans-serif'] = ['SimHei', 'Bitstream vera Sans', 'Lucida Grande',
								   'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica',
								   'Avant Garde', 'sans-serif', 'axes.unicode_minus'] # 设置中文
plt.rcParams['font.family'] = 'sans-serif'


def mat_bing(size_list, name_list):
	# 调节图形大小，宽，高
	plt.figure(figsize=(6,6))

	#将某部分爆炸出来，使用括号， 将第一块分割出来， 数值的大小是分割出来的与其它两款的间隙
	# explode = (0.01, 0.01, 0.01, 0.01)

	patches, label_text, percent_text = plt.pie(size_list,
												# explode=explode,
												labels=name_list,
												labeldistance=1.1,
												autopct='%3.1f%%',
												shadow=False,
												startangle=90,
												pctdistance=0.6)
	# labeldistance. 文本的位置离原点有多远， 1.1指1.1倍半径的位置
	# autopct, 圆里面的文本格式, %3.1f%%表示小数有三位，整数有移位的浮点数
	# shadow, 饼是否有阴影
	# startangle, 起始角度, 0, 表示从0开始逆时针转, 为第一块。 一般选择90度开始
	# pctdistance, 百分比的text离圆心的距离
	# patches, 1_texts, p_texts, 为了得到饼图的返回值, p_texts饼图是内部文本的, 1_texts外部饼图文本的

	# 改变文本的大小
	# 方法是把每一个text遍历。 调用set_size方法设备它的属性
	for l in label_text:
		l.set_size = 30
	for p in percent_text:
		p.set_size = 20
	# 设置x, y轴刻度一直，这样饼图才是圆的
	plt.axis('equal')
	plt.legend()
	plt.show()


if __name__ == '__main__':
	conters = [30, 53, 12, 45]
	protocols = ['http协议', 'ftp协议', 'rds协议', 'qq协议']
	mat_bing(conters, protocols)