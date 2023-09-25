# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:28:11 2023

@author: allen
"""

d=dict()
s=list()
n=int(input())
i=2

while(i<=n):
    if((n%i)!=0):
        i+=1
    else:
        if(d.get(i) == None):
            d[i]=1
        else:d[i]=d.get(i)+1
        n/=i

for key, value in d.items():
    if(value>1):
        s.append(f"{key}^{value}")
    else:s.append(str(key))

print(" * ".join(s))