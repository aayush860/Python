#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:57:44 2018
@author: aayushbhargava
"""

import os 
PATH_ADDRESS = "/Users/aayushbhargava/Documents/evive/daily_prod_feb/"
test = os.listdir(PATH_ADDRESS)
for files in test:
    PATH = PATH_ADDRESS+files+"/"
    try:
        subdir = os.listdir(PATH)
        for subfiles in subdir:
            print subfiles
            os.unlink(PATH+subfiles)
            
        print ("----------------------------------------------")
    except:
        pass
    


#/Users/aayushbhargava/Downloads