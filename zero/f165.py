# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:43:55 2023

@author: allen
"""

while (1):
    try:
        a, b = map(int,input().split())
        if(b == 0 or a == 0):
            print("OK!")
        elif (a % b):
            print(a%b)
        else:
            print("OK!")
    except:
        break