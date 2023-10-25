# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:21:29 2023

@author: allen
"""

import math

x = int(input())    # 輸入值
n = math.ceil(x / 2)    # 設定n為x的1/2無條件進位值

i = 1    # 橫向輸出
while (i <= x):
    print(f"{i}", end = "")
    i += 1
print("  ", end = "")
i = x
while (i > 0):
    print(f"{i}", end = "")
    i -= 1
print("\n")
    
i = 1    # 直向輸出
while (i <= x):
    print(f"{i}  {x-i+1}")
    i += 1
print()

i = 1
while (i <= x):
    print(f"{i}" * i, " " * (x-i), sep = "", end = "")
    print("  ", f"{x-i+1}" * i, " " * (x-i), sep = "", end = "")
    print("  ", " " * (x-i), f"{i}" * i, sep = "", end = "")
    print("  ", " " * (x-i), f"{x-i+1}" * i, sep = "", end = "")
    print("  ", f"{i}" * (x-i+1), " " * (i-1), sep = "", end = "")
    print("  ", f"{x-i+1}" * (x-i+1), " " * (i-1), sep = "", end = "")
    print("  ", " " * (i-1), f"{i}" * (x-i+1), sep = "", end = "")
    print("  ", " " * (i-1), f"{x-i+1}" * (x-i+1), sep = "", end = "")
    print()
    i += 1