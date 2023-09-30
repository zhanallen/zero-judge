# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 03:00:44 2023

@author: allen
"""

import math

def sc(a, b):
    r = 0
    for i in range(math.ceil(a ** 0.5),(int(b ** 0.5) + 1)):
        r += i ** 2
    return (r)

x = int(input())
s = 1
for i in range(x):
    a = int(input())
    b = int(input())
    print(f"Case {s}: {sc(a, b)}")
    s += 1