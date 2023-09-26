# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 01:34:38 2023

@author: allen
"""

a, b, c = map(int, input().split())
x1 = (-b + ((b ** 2) - 4 * a * c) ** (1 / 2)) / (2 * a)
x2 = (-b - ((b ** 2) - 4 * a * c) ** (1 / 2)) / (2 * a)
if (type(x1) == complex or type(x2) == complex):
    print("No real root")
elif (x1 == x2):
    print("Two same roots x=", int(x1), sep = "")
else:
    print("Two different roots x1=", int(x1), " , x2=", int(x2), sep = "")