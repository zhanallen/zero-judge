# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:38:47 2023

@author: allen
"""

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if (a == 1):
        print(b + c)
    elif (a == 2):
        print(b - c)
    elif (a == 3):
        print(b * c)
    else:
        print(b // c)