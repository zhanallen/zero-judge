# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 22:06:33 2023

@author: allen
"""

while (1):
    l = list(map(int,input().split()))
    if (l == [0, 0, 0, 0]):
        break
    h = abs(l[0] - l[2])
    v = abs(l[1] - l[3])
    if (h == 0 and v == 0):
        print(0)
    elif (h == v or h == 0 or v == 0):
        print(1)
    else:
        print(2)