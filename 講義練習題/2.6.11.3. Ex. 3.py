# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:47:01 2023

@author: allen
"""

x = int(input("輸入存款金額 :"))
y = int(input("輸入存入時間(年) :"))
for _ in range(y * 2):
    x *= 1.005
print(int(x))