#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:55:42 2019

@author: aayushbhargava
"""

import requests
import time,os
from datetime import datetime
start_time = time.time()
'''
live_stock_price = 'https://newtrade.sharekhan.com/wcs.sk?e=141&mid=5&ex=NSE&s=RELIANCE'
while True:
    r = requests.get(live_stock_price)
    print r.text.split('ltp":"')[1].split('","ltq"')[0].split('","token"')[0]
   # time.sleep(.3)
'''

filename='/Users/aayushbhargava/Documents/project_chester/stocks_13feb.txt'
filex = open(filename, "a")
live_stock_price = 'https://newtrade.sharekhan.com/wcs.sk?e=103&category=all&key=hfcl'
prev=0
nextt=1

while True:
    try:
        r = requests.get(live_stock_price)
        s = r.text.split('ltp":"')[1].split('","exchange"')[0].split('","perc"')[0]
        prev = float(str(s))
        time.sleep(0.1)
        if prev!=nextt:
            timee=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print str(timee)+'\t'+str(prev)+'\n'
            filex.write(str(timee)+'\t'+str(prev)+'\n')
            filex.flush()
            os.fsync(filex)
            nextt=prev
        
    except:
        r = requests.get(live_stock_price)
        s = r.text.split('ltp":"')[1].split('","exchange"')[0].split('","perc"')[0]
        prev = float(str(s))
        time.sleep(0.1)
        if prev!=nextt:
            timee=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print str(timee)+'\t'+str(prev)+'\n'
            filex.write(str(timee)+'\t'+str(prev)+'\n')
            filex.flush()
            os.fsync(filex)
            nextt=prev

end_time = time.time()
print "Total Time:"+str(end_time-start_time)