# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:33:53 2023

@author: allen
"""

t = int(input())
for _ in range(t):
    a = input()
    x = 1
    for i in range(len(a)):
        x *= int(a[i])
    print(x)