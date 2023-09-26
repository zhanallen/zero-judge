# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:02:20 2023

@author: allen
0925-2

據輸入內容，輸出特定的運算結果。

輸入說明
輸入某兩個字串

輸出說明
輸出第一個字串第三個字元之後與第二個字串倒數第三個之前的合併結果

範例輸入 #1
debug
coders
範例輸出 #1
bug code
範例輸入 #2
uncertain
things
範例輸出 #2
certain thin

"""

x = input()
y = input()
print(x[2:], y[:-2])