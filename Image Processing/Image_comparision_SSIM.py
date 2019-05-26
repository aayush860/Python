#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:05:28 2018

@author: aayushbhargava


This script takes the mean square of both images pixels and subtract them form other and tell us the difference...That difference is how different image is from other one.
"""



import numpy as np
import cv2


x1=cv2.imread('/Users/aayushbhargava/Desktop/Screen Shot 2018-07-18 at 3.36.53 PM.png').resize(400,400)
x2=cv2.imread('/Users/aayushbhargava/Desktop/Screen Shot 2018-07-17 at 2.12.21 PM.png').resize(400,400)


err = np.sum((x1.astype("float") - x2.astype("float")) ** 2)
err /= float(x1.shape[0] * x2.shape[1])

print err
