# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:54:12 2023

@author: allen
"""

x = int(input())
c = list()
n = list()
for i in range(x):
   a = list(map(str, input().split()))
   c.append(a[0])
   if (a[0] not in n):
       n.append(a[0])
n.sort()
for i in n:
    print(i,c.count(i))