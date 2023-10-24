# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:37:20 2023

@author: allen
"""

x = int(input())
if (x == 1):
    print(0)
else:
    l = [0, 1]
    i = 2
    while (i < x):
        l.append(l[i-1] + l[i-2])
        i += 1
    print(*l)