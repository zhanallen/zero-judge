# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 02:21:14 2023

@author: allen

請將海龍公式撰寫成Python程式碼，
並用其計算出三邊常分別為3, 4, 5之三角形的面積後輸出。

"""

a, b, c = 3, 4, 5
s = (a + b + c) / 2
d = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print(d)