# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:06:25 2023

@author: allen
"""
while(1):
    try:
        a,b=map(int,input().split())
        x=list()
        for i in range(a):
            x.extend(input().split())
        for i in range(b):
            for j in range(a):
                print(x[0+i+b*j],end=" ")
            print()
    except:
        break