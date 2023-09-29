# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:24:18 2023

@author: allen
"""

while (1):
    try:
        x = eval(input().replace("/", "//"))    # 本題題目要求整除，所以使用者如果輸入/
        print(x)
    except:
        break