# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:21:28 2023

@author: allen
"""

def get(n):
    ls = list()
    for i in range(1,n):
        if ((n % i) == 0):
            ls.append(i)
    return(ls)

l = list()
i = 1
while (i <= 500):
    l = get(i)
    Sum = sum(l)
    if(Sum == i):
        print(i)
    i += 1