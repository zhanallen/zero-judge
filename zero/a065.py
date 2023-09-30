# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 03:41:52 2023

@author: allen
"""

x = input()
for i in range(len(x) - 1):
    a = abs(ord(x[i]) - ord(x[i + 1]))
    print(a, end = "")