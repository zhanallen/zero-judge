# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 01:51:57 2023

@author: allen
"""

f = input().split()
if (len(f) == 2):
    n = int(f[0])
    s = f[1]
else:
    n = int(f[0])
    s = input()
    
x = 1
out = str()
c = s[0]
for i in range(1, n):
    if (s[i] == c):
        x += 1
        continue
    else:
        out += f"{x}{c}"
        x = 1
        c = s[i]
if (c == s[-1]):
    out += f"{x}{c}"
else:
    out += c
if (len(out) >= len(s)):
    print(s)
else:
    print(out)