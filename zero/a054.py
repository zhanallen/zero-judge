# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 01:15:12 2023

@author: allen
"""

d = ["BNZ", "AMW", "KLY", "JVX", "HU", "GT", "FS", "ER", "DOQ", "CIP"]
x = input()
c = int(x[8])
s = 0
for i in range(8, 0, -1):
    s += int(x[8 - i]) * i
print(d[(10 - (s + c)) % 10])