# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:25:59 2023

@author: allen
"""

x = int(input())
a = 0; b = 0; c = 0
for i in range(x):    # 執行x次的迴圈
    n = int(input())
    if (n % 3 == 0):
        a += 1
    elif (n % 3 == 1):
        b += 1
    else:
        c += 1
print(a, b, c)