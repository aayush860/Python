#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:07:45 2018

@author: aayushbhargava
"""

from scapy.all import *
a=rdpcap("/Users/aayushbhargava/Documents/visit_dump.pcap")
#print a
#for x in range(1,1000):
#    sendp(a)
print "-------------------------------------------"
count = 0
for x in a:
    print x.show()
    count = count+1
    if count==10:
        break