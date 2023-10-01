# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:22:10 2023

@author: allen

請修正下列程式碼，使其能正確執行：

bornYear = input("請輸入你的出生年份：")
nowYear = input("請輸入今年的年份：")
age = nowYear - bornYear
print("你今年%d歲" % age)

"""


bornYear = int(input("請輸入你的出生年份："))    # 輸入的值轉成int即可
nowYear = int(input("請輸入今年的年份："))
age = nowYear - bornYear
print("你今年%d歲" % age)