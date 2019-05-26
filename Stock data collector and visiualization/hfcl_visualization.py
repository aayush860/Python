#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:29:24 2019

@author: aayushbhargava
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

x = pd.read_csv('/Users/aayushbhargava/Downloads/HFCL.BO (1).csv')
#print str((x.Open-x.Close).tail(1000))
one=[]
two=[]
for y in range(3900,len(x)):
    z= (x.Open[y]-x.Close[y])
    two.append(x.Date[y])
    one.append(z)
#print one
fig, ax = plt.subplots()
plt.plot(one)
plt.show()
fig.savefig('/Users/aayushbhargava/Downloads/oc.png',dpi=500)
plt.close()

n = x.shape[0]
p = x.shape[1]


x=x.values
train_start = 0
train_end = int(np.floor(0.8*n))
test_start = train_end
test_end = n

data_train = x[np.arange(train_start, train_end), :]
data_test = x[np.arange(test_start, test_end), :]

print data_test


#print str(x.High-x.Open)+'  '+str(x.High-x.Open)cd
