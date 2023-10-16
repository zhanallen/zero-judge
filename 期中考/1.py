# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:50:38 2023

@author: allen
"""

x = list(map(int, input().split()))
y = list(map(str, input().split()))
n = str(x[0])
for i in range(len(x) - 1):
    n = n + y[i % len(y)] + f"{x[i + 1]}"
print(eval(n))