# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:49:11 2023

@author: allen
"""

n = int(input())
for _ in range(n):
    l = list(map(int,input().split()))
    x = l[0]
    y = l[1]
    a = x + y
    c = a // 2
    if (y > x or (a % 2)):
        print("impossible")
    else:
        print(c, x - c)