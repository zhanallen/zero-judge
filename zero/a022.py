# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:31:23 2023

@author: allen
"""

import math

x = input()
l = math.ceil(len(x) / 2)    # 使用字串長度除2並無條件進位找出中間值
a = x[0:l:1]
b = x[-1:(-l - 1):-1]
if (a == b):
    print("yes")
else:
    print("no")