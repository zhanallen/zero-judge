# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:21:02 2023

@author: allen
"""
x = int(input())
for i in range(x):
    a = input().split()
    if (int(a[1]) - int(a[0]) == (int(a[2]) - int(a[1]))):
        for c in range(len(a)):
            print(a[c], end = " ")
        print(int(a[3]) + (int(a[1]) - int(a[0])))
    else:
        for c in range(len(a)):
            print(a[c], end = " ")
        print(int(int(a[3]) * (int(a[1]) / int(a[0]))))