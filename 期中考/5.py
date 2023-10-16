# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:52:55 2023

@author: allen

根據輸入的正整數,輸出一個中空的正三角形。

輸入說明
一正整數。

輸出說明
一個中空的三角形,底邊的星星數目與三角形的高度(行數)就是輸入的正整數數目。

範例輸入#1
3
5

範例輸出 #1
  .
 . .
.....
    .
   . .
  .   .
 .     .
.........

"""

while (1):
    try:
        x = int(input())
        for i in range(1,x + 1):
            if (i == 1 or i == x):
                print(" " * (x - i), end = "")
                print("." * (2 * i - 1))
            else:
                print(" " * (x - i) + "." + " " * (2 * i -3) + ".")
    except:
        break