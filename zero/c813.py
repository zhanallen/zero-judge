# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:32:08 2023

@author: allen
"""

def f(n: int):
    sum = 0
    c = str(n)
    for i in c:
        sum += int(i)
    return(sum)

def g(n: int):
    if (n // 10):
        return g(f(n))
    else:
        return(n)

while (1):
    x = int(input())
    if(x == 0):
        break
    print(g(x))
