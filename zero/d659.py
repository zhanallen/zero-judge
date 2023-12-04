# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 22:18:03 2023

@author: allen
"""

n = int(input())
for i in range(1, n+1):
    l = list(map(int,input().split()))
    l.sort()
    print(f"Case {i}: {l[1]}")