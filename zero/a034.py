# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:53:48 2023

@author: allen
"""

while (1):
    try:
        x = int(input())
        print(bin(x).replace("0b", ""))
    except:
        break