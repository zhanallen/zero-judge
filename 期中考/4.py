# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:52:42 2023

@author: allen
"""

while (1):
    try:
        x = int(input())
        if (x > 0):
            for i in range(1, x + 1):
                print(f"{i} " * i)
        if (x < 0):
            for i in range(abs(x), 0, -1):
                print(f"{i} " * i)
    except:
        break
    