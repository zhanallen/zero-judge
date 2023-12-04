# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:50:42 2023

@author: allen
"""

count = 1
while (1):
    try:
        x = int(input())
        l = list()
        for _ in range(x):
            l.append(tuple(map(int,input().split())))
        l.sort()
        n = 0
        for _ in range(len(l)):
            if (n == len(l)):break
            for i,j in l:
                if (i == l[n][0] and j == l[n][1]):
                    continue
                elif (i >= l[n][0] and j >= l[n][1]):
                    l.remove(l[n])
                    n -= 1
                    break
            n += 1
        print(f"Case {count}:")
        print(f"Dominate Point: {len(l)}")
        for i, j in l:
            print(f"({i},{j})")
        count += 1  
    except:
        break