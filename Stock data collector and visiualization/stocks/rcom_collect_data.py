#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:54:57 2019

@author: aayushbhargava
"""

import requests
import time,os
from datetime import datetime
start_time = time.time()

filename='/Users/aayushbhargava/Documents/project_chester/stocks_19feb_rcom_bse.txt'
filex = open(filename, "a")
live_stock_price = 'https://newtrade.sharekhan.com/wcs.sk?e=141&mid=5&ex=BSE&s=RCOM'    #BSE
#live_stock_price = 'https://newtrade.sharekhan.com/wcs.sk?e=141&mid=5&ex=NSE&s=RCOM'    #NSE
prev=0
nextt=1

while True:
    try:
        r = requests.get(live_stock_price)
        #print r.text
        try:
            s = r.text.split('ltp":"')[1].split('","token"')[0]
            prev = float(str(s))
        except:
            s = r.text.split('ltp":"')[1].split('","ltq"')[0]
            prev = float(str(s))
        
        time.sleep(0.1)
        
        if prev!=nextt:
            timee=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            print str(timee)+'\t'+str(prev)+'\n'
            filex.write(str(timee)+'\t'+str(prev)+'\n')
            filex.flush()
            os.fsync(filex)
            nextt=prev

    #except:
     #   print 'erefrecfe'
           
    except:
        r = requests.get(live_stock_price)
        try:
            s = r.text.split('ltp":"')[1].split('","token"')[0]
            prev = float(str(s))
        except:
            print 'eerroorr'
            s = r.text.split('ltp":"')[1].split('","ltq"')[0]
            prev = float(str(s))
        prev = float(str(s))
        time.sleep(0.1)
        if prev!=nextt:
            timee=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            print str(timee)+'\t'+str(prev)+'\n'
            filex.write(str(timee)+'\t'+str(prev)+'\n')
            filex.flush()
            os.fsync(filex)
            nextt=prev
    

end_time = time.time()
print "Total Time:"+str(end_time-start_time)