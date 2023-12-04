# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:53:35 2023

@author: allen

浮點數計算有誤
"""

while (1):
    try:
        a, b, n = map(int, input().split())
        s = f"%.{n+1}f" %(a/b)
        print(s[:-1])
    except:
        break