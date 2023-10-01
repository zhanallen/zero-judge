# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:58:52 2023

@author: allen
"""

x = input().replace("」", "").replace("「", "").split("、")
if (len(x[1]) < 2):
    x[1] = "0"+x[1]
if (len(x[2]) < 2):
    x[2] = "0"+x[2]
a = ".".join(x)
print(a)