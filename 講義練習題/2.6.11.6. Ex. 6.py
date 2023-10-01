# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 01:26:28 2023

@author: allen

網路傳輸速度為1M = 128kB/s，而檔案大小為1MB = 1024kB，
在理想狀態下，以速度100M傳輸256MB的檔案需要花多少秒？
(請撰寫一程式計算該結果並加以輸出)

"""

M, MB = map(int,input().split())
M *= 128
MB *= 1024
print(MB / M)