#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:24:26 2018

@author: aayushbhargava
"""
import threading
from multiprocessing import Process

import time
from scapy.all import *

hh=random.randint(49152,65535)
tcp = TCP(flags='S',sport=hh,dport=443,window=65535,dataofs=11,options=[('MSS', 1460), ('NOP', None), ('WScale', 5), ('NOP', None), ('NOP', None), ('Timestamp', (int(time.time()), 0)), ('SAckOK', ''), ('EOL', None)])
ip = IP(len=64,ihl=5,flags='DF',dst='192.237.154.216',src='10.14.5.91',id=0)
#global a
#a = (Ether()/ip/tcp)

synack_packet = sr1(ip/tcp)
my_ack = synack_packet.seq+1
print my_ack

tcp = TCP(flags='A',sport=hh,dport=443,dataofs=8,window=4104,ack=my_ack,seq=1,options=[('NOP', None), ('NOP', None), ('Timestamp', (int(time.time()), int(time.time())))])
ip = IP(len=52,ihl=5,flags='DF',dst='192.237.154.216',src='10.14.5.91',id=0,frag=0L)

send(ip/tcp)
#ax=sr(a)
#sendp(a)
