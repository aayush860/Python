#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:43:58 2019

@author: aayushbhargava
"""

import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('/Users/aayushbhargava/Documents/project_chester/stocks_5feb_rcom.txt',sep='\t')
print x

one=[]
two=[]
for y in range(0,len(x)):
    one.append(x.data[y])
    #z= (x.Open[y]-x.Close[y])
    #two.append(x.Date[y])
    
fig, ax = plt.subplots()
plt.plot(one)
plt.show()
fig.savefig('/Users/aayushbhargava/Downloads/oc_rcom5feb.png',dpi=500)
plt.close()
