# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:01:51 2023

@author: allen
"""

while (1):
    try:
        a, b = map(int,input().split())
        print(abs(a - b))
    except:
        break