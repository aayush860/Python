#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:07:28 2018

@author: aayushbhargava
"""

# Python program to illustrate 
# template matching
import cv2
import numpy as np
 
# Read the main image
img_rgb = cv2.imread('/Users/aayushbhargava/Desktop/Screen Shot 2018-07-18 at 3.36.53 PM.png')
#cv2.imshow('Detected',img_rgb) 
# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
 
# Read the template
template = cv2.imread('/Users/aayushbhargava/Desktop/Screen Shot 2018-07-17 at 2.12.21 PM.png',0)
 
# Store width and heigth of template in w and h
w, h = template.shape[::-1]
 
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF_NORMED)

print(len(res))
#print(res)

# Specify a threshold
threshold = 0.8
 
# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold) 
for x in loc:
    print x
print(len(loc[0]))

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
 
# Show the final image with the matched area.

#cv2.imshow('Detected',img_rgb)
#cv2.waitKey(5000)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.waitKey(1)

