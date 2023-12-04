# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:51:16 2023

@author: allen
"""

i = 1
while (1):
    x = int(input())
    if (x == 0):
        break
    l = list(map(int,input().split()))
    S = sum(l) // x
    n = 0
    for j in l:
        if (j > S):
            n += (j - S)
    print(f"Set #{i}")
    print(f"The minimum number of moves is {n}.\n")
    i += 1