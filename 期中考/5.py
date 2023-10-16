# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:52:55 2023

@author: allen
"""

while (1):
    try:
        x = int(input())
        for i in range(1,x + 1):
            if (i == 1 or i == x):
                print(" " * (x - i), end = "")
                print("." * (2 * i - 1))
            else:
                print(" " * (x - i) + "." + " " * (2 * i -3) + ".")
    except:
        break