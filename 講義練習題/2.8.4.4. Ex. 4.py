# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:07:00 2023

@author: allen
"""

x = input()
s = 16 - len(x)    # 16減x長度
print("0" * (s) + x)    # 輸出s個0再輸出x
