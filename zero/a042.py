# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:30:51 2023

@author: allen

"""

while (1):
    try:
        x = int(input())
        print(int(2 * (((x * (x - 1)) / 2) + 1)))    #算出公式直接套用
    except:
        break