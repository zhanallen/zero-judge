# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:56:04 2023

@author: allen
"""

while (1):                # 使用while製作一個無窮迴圈
    try:                  # 如果try裡面的程式沒有錯誤則會一直執行，否則將會執行except
        x = int(input())
        if((x % 4 == 0 and x % 100 != 0) or x % 400 == 0):
            print("閏年")
        else:
            print("平年")
    except:               # 進入except後執行break終止while迴圈
        break
    