# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:25:14 2023

@author: allen

請修正下列程式碼，使其能正確執行：

gift = input("請輸入禮物份數：")
children = input("請輸入小朋友個數：")
oneGet = gift // children
print(gift + "個禮物分給" + children +"個小朋友，每個小朋友可以分到" + oneGet + "個禮物")

"""

gift = int(input("請輸入禮物份數："))    # 輸入的值轉成int
children = int(input("請輸入小朋友個數："))
oneGet = gift // children
print(gift, "個禮物分給", children, "個小朋友，每個小朋友可以分到", oneGet, "個禮物", sep = "")
# 加號不能用在非字串的地方所以要改逗號