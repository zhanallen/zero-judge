# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 02:56:50 2023

@author: allen
"""

while (1):
    try:
        x = int(input())
        if (x <= 10):
            print(x * 6)
        elif (x >= 11 and x <= 20):
            print(60 + (x - 10) * 2)
        elif (x >= 21 and x <= 40):
            print(80 + (x - 20))
        else:
            print(100)
    except:
        break