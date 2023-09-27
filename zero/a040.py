# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:14:44 2023

@author: allen
"""

out = 0
x, y = map(int, input().split())
for i in range(x, y + 1):
    s = 0
    for j in range(len(str(i))):
        
        s += int(str(i)[j]) ** len(str(i))
    if (i == s):
        print(i, end = " ")
        out = 1
if (out == 0):
    print("none")