# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:53:06 2023

@author: allen

英文的 Odd 是「奇怪」的意思，Odd Number 當然就是「奇怪的數字」簡稱「奇數」。
問題是「奇數」倒底是唸成「ㄐㄧ數」或是「ㄑㄧˊ 數」呢？

輸入說明
輸入只有一行，其中含有一個整數 i。

輸出說明
如果 i 是奇數，輸出 Odd；如果 i 是偶數，則輸出 Even。 

範例輸入 #1
1
範例輸出 #1
Odd
範例輸入 #2
4
範例輸出 #2
Even

"""

x = int(input())
if((x % 2) == 1):
    print("Odd")
else:
    print("Even")
    
    
"""
x = int(input())
if(x % 2):
    print("Odd")
else:
    print("Even")
"""