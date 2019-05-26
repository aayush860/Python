#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:40:28 2019

@author: aayushbhargava
"""
import pandas as pd
initial_price = 21.40
profit=0
loss=0
stoploss=0
stock_vol=0
stoploss=0
def buy():
    print 'buy '+str(current_price)
def sell():
    print 'sell '+str(current_price)
    
x = pd.read_csv('/Users/aayushbhargava/Documents/project_chester/stocks_7feb.txt',sep='\t')
for i in range(0,len(x)):
    current_price = float(x.data[i])
    print str(current_price)+' init: '+str(initial_price)
    if current_price > initial_price:
        if stock_vol==100:
            sell()
            profit+=3.33
            stock_vol=0
            stoploss=0
            initial_price = current_price
        else:
            initial_price = current_price
            
    elif current_price < initial_price:
        if stock_vol==0:
            initial_price = current_price
            buy()
            stock_vol=100
        elif stock_vol==100:
            stoploss+=1
            print 'sl inc==========='
            if stoploss>2:
                initial_price = current_price
                sell()
                stock_vol=0
                stoploss=0
                print 'loss----------'
                loss+=6.66
    elif current_price == initial_price:
        initial_price = current_price
        print 'nothing'
print '-------------------------------------------'
print '\nprofit: '+str(profit)
print 'loss:    '+str(loss)
print 'Total profit: '+str(profit-loss)
print len(x)