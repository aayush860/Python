#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 18:56:21 2018

@author: aayushbhargava
"""

from skimage.measure import compare_ssim
from scipy.ndimage import imread
import numpy as np
a = imread('/Users/aayushbhargava/Desktop/img4.png', flatten=True).astype(np.uint8)
b = imread('/Users/aayushbhargava/Desktop/img9.png', flatten=True).astype(np.uint8)
sim, diff = compare_ssim(a, b, full=True)

print sim
print diff