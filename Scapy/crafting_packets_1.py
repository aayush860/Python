#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:54:02 2018
,src=RandIP()
@author: aayushbhargava
"""
import threading
from multiprocessing import Process

import time
from scapy.all import *

def pack1(hh):
    tcp = TCP(flags='S',sport=hh,dport=443,window=65535,dataofs=11,options=[('MSS', 1460), ('NOP', None), ('WScale', 5), ('NOP', None), ('NOP', None), ('Timestamp', (int(time.time()), 0)), ('SAckOK', ''), ('EOL', None)])
    ip = IP(len=64,ihl=5,flags='DF',dst='192.237.154.216',src='10.14.5.91',id=0)
    global a
    a = (Ether()/ip/tcp)
    #ax=sr1(a)
    sendp(a)


li=[]
def cc():
    hh=random.randint(49152,65535)
    for x in range(0,2):
        hh=hh+1
        print hh
      #  UDP(sport=hh)
        li.append(hh)
        pack1(hh)
        for x in a:
            print x.show2()
        hexdump(a)
#for x in range(0,1):
#    cc()
#print li
cc()
def pack2():
    for z in li:
        tcp = TCP(flags='A',sport=z,dport=443,dataofs=8,window=4104,ack=1,seq=1,options=[('NOP', None), ('NOP', None), ('Timestamp', (int(time.time()), int(time.time())))])
        ip = IP(len=52,ihl=5,flags='DF',dst='192.237.154.216',id=0,frag=0L)
        global a
        a = Ether()/ip/tcp
        sendp(a)
        for x in a:
            print x.show2()
        hexdump(a)

time.sleep(1)
#pack2()
    

