# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:04:48 2023

@author: allen

請查詢附錄X的表格，將以下句子全部輸出成小寫，
"PLEASE CONVERT THIS SENTENCE TO LOWER CASE."

"""

x = input()
for i in range(len(x)):
    if(ord(x[i]) > 64 and ord(x[i]) <91):
        print(chr(ord(x[i]) + 32), end = "")
    else:
        print(x[i], end = "")



"""
或是用內建涵式

x = input()
print(x.lower())

"""