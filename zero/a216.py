# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:55:52 2023

@author: allen
"""

def f(n):
        return int(((n + 1) * n) / 2)
def g(n):
    return int((n * (n+1) * (n+2)) / 6)

while (1):
    try:
        x = int(input())
        print(f(x), g(x)) 
    except:
        break