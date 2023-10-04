# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:25:41 2023

@author: allen

我解不出來

"""

import math

while (1):
    try:
        x = input()
        x = x.lower()
        l = math.ceil(len(x) / 2)
        a = x[0:l:1]
        b = x[-1:(-l - 1):-1]
        if (a == b):
            print("yes !")
        else:
            print("no...")
    except:
        break