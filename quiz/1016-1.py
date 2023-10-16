# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:55:09 2023

@author: allen

根據輸入內容，輸出特定的運算結果。

輸入說明
輸入一個字串

輸出說明
輸出一個字串，但每個子字串之間以下標【_】字母作為間隔。
請注意字串的前後可能會有多餘的空白字母存在，必須一併刪除。

範例輸入 #1
This is a book.
範例輸出 #1
This_is_a_book.
範例輸入 #2
   What a   nice   day.    Let's    go hiking.
範例輸出 #2
What_a_nice_day._Let's_go_hiking.

"""

x = input().split()
print("_".join(x))