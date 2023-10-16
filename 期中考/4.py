# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:52:42 2023

@author: allen

輸入一個整數,若是正整數,會畫出正的直角三角形;若是負整數,會畫出反的直角三角形。

輸人說明
一正整數與另一負整數

輸出說明
一個數字型的正/反直角三角形

範例輸入 #1
4
-5
範例輸出 #1
1
2 2
3 3 3
4 4 4 4

5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1

"""

while (1):
    try:
        x = int(input())
        if (x > 0):
            for i in range(1, x + 1):
                print(f"{i} " * (i - 1), end = "")
                     # 注意^是有一個空白的
                print(i)
        if (x < 0):
            for i in range(abs(x), 0, -1):
                print(f"{i} " * (i - 1), end = "")
                     # 注意^是有一個空白的
                print(i)
    except:
        break
    