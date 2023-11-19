# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:25:55 2023

@author: allen

輸入一個整數，若是正整數，會畫出正的直角三角形；若是負整數，會畫出反的直角三角形。

輸入說明
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

a = int(input())
b = int(input())
b = -b

for i in range(1,a+1):
    print(f"{i}" * i)
print()
for i in range(b,0,-1):
    print(f"{i}" * i)