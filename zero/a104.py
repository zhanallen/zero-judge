# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 04:16:16 2023

@author: allen
"""
while (1):
    try:
        x = int(input())
        a = list(map(int, input().split()))
        a.sort()
        print(*a)
    except:
        break