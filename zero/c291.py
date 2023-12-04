# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:53:36 2023

@author: allen

map(int,input().split())
"""


x = int(input())
l1 = list([1]*x)
l2 = list(range(x))
fin = 0
for i in range(x):
    if (l1[i]):
        n = i
        l1[n] = 0
        fin += 1
        while (l1[l2[n]]):
            l1[l2[n]] = 0
            n = l2[n]
print(fin)