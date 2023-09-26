# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:53:37 2023

@author: allen
"""

M, D = map(int, input().split())
S = (M * 2 + D) % 3
if (S == 0):
    print("普通")
elif (S == 1):
    print("吉")
else:
    print("大吉")