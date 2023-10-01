# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:04:48 2023

@author: allen
"""

x = input()
for i in range(len(x)):
    if(ord(x[i]) > 64 and ord(x[i]) <91):
        print(chr(ord(x[i]) + 32), end = "")
    else:
        print(x[i], end = "")
        