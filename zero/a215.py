# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:39:50 2023

@author: allen
"""

while (1):
    try:
        x, y = map(int, input().split())
        Sum = 0
        s = 0
        while (1):
            Sum += x
            print(x,Sum)
            s += 1
            x += 1
            if(Sum > y):
                break
        print(s)
    except:
        break   