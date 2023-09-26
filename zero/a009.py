# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 01:54:12 2023

@author: allen
"""
x = input()
for i in range(len(x)):
    a = ord(x[i])
    print(chr(a - 7), end = "")