# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:34:53 2023

@author: allen
"""

while (1):
    x = int(input())
    if(x == 0):
        break
    for i in range(1,x):
        if(i % 7 != 0):
            print(i, end = " ")
    print()
