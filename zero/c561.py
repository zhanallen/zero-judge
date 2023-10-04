# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:20:09 2023

@author: allen
"""

x = int(input())
n = input().split()
for i in range(0, x, 1):
    c = n[i]
    n[i] = int(c[::-1])
print(max(n))