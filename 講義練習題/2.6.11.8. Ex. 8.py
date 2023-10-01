# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 02:09:04 2023

@author: allen

請將海龍公式撰寫成Python程式碼，
讓使用者可利用系統參數的方式代入三角形的三邊長，
並輸出三角形面積。

"""

a, b, c = map(int,input().split())
s = (a + b + c) / 2
d = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print(d)