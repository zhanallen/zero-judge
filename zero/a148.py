# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 02:34:52 2023

@author: allen
"""

while (1):
    try:
        x = list(map(int,input().split()))
        a = sum(x) - x[0]
        a /= x[0]
        if(a <= 59):
            print("yes")
        else:
            print("no")
    except:
        break