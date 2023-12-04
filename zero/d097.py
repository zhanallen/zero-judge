# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:07:27 2023

@author: allen
"""

while (1):
    try:
        x = list(map(int,input().split()))
        l = x[1:]
        n = x[0]
        ls = list(abs(l[i]-l[i+1]) for i in range(n-1))
        ls.sort()
        ln = list(i for i in range(1, n))
        if (ls == ln):
            print("Jolly")
        else:
            print("Not jolly")
    except:
        break