# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:04:58 2023

@author: allen
"""

def sd(s, r):
    r += 1
    if (s == 1):
        return (s, r)
    elif (s % 2 ==1):
        s = 3 * s + 1
    else:
        s //= 2
    return(sd(s, r))

while (1):
    try:
        n = list(map(int, input().split()))
        print(n[0], n[1], end = " ")
        ma = 0
        n.sort()
        for i in range(n[0],n[1] + 1):
            l = sd(i, 0)
            ma = max(ma, l[1])
        print(ma)
    except:
        break