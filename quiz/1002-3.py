# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:24:15 2023

@author: allen

根據輸入的數字，輸出特定區段的數字。
例如，輸入數字為5與3，
則輸出5除以3之後的餘數，
也會輸出3除以5之後的餘數。

輸入說明
輸入兩個數字

輸出說明
輸出該兩個數字的餘數

範例輸入 #1
5 3
範例輸出 #1
5/3餘2
3/5餘3

"""

x, y = map(int, input().split())
print(x, "/", y, "餘", x % y, sep = "")
print(y, "/", x, "餘", y % x, sep = "")

# print(f"{x}/{y}餘{x % y}")
# print(f"{y}/{x}餘{y % x}")