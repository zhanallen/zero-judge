# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:21:02 2023

@author: allen
"""
x = int(input())    # 先輸入要執行的次數
for i in range(x):
    a = input().split()    # 切割輸入的字串
    if (int(a[1]) - int(a[0]) == (int(a[2]) - int(a[1]))):    # 判斷為等差還是等比數列並輸出
        for c in range(len(a)):
            print(a[c], end = " ")
        print(int(a[3]) + (int(a[1]) - int(a[0])))
    else:
        for c in range(len(a)):
            print(a[c], end = " ")
        print(int(int(a[3]) * (int(a[1]) / int(a[0]))))