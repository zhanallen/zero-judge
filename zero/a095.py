# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 03:55:59 2023

@author: allen

這題題目很麻煩可以看一下討論
"""

while (1):
    try:
        a, b = map(int,input().split())
        if (a == b):
            print(b)
        else:
            print(b + 1)
    except:
        break