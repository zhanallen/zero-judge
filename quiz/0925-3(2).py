# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:05:01 2023

@author: allen
0925-3(2)

根據輸入內容，輸出特定的運算結果。

輸入說明
輸入某二個數字

輸出說明
輸出一個運算結果

範例輸入 #1
7 5
範例輸出 #1
7 / 5 的商數及餘數分別是 1 2
範例輸入 #2
10 3
範例輸出 #2
10 / 3 的商數及餘數分別是 3 1

"""

x, y = input().split()
x = int(x)
y = int(y)
print(x, " / ", y, " 的商數及餘數分別是 ", (x // y), " ", (x % y), sep = "")