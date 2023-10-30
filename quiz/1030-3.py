# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:55:58 2023

@author: allen

大家都學過程式設計的天下第一招式，Hello, World囉，
讓我們這次到山谷中聽一下回音吧~~~
例如，我對這山谷中喊出小於六個字的字串："Hello, what a nice world!"之後，
山谷中的回音會試出現以下的回音字串喔。

Hello, what a nice world!
what a nice world!
a nice world!
nice world!
world!

現在請您寫出一支小程式來處理這樣的空谷回音吧。

輸入說明
一個小於六的數字。
一個小於六個字的字串，且中間以空白區隔。

輸出說明
依序輸出該字串的後面段文。

範例輸入 #1
5
Hello, what a nice world!
範例輸出 #1
Hello, what a nice world!
what a nice world!
a nice world!
nice world!
world!

"""

y = int(input())    # 輸入切割後的數量
x = input()    # 輸入字串
l = x.split()    # 切割字串並存入l
# 因為split()涵式預設就是用空白切割所以不須另外設的切割字元
for i in range(y):
    print(*l[i::])
    
    
'''
乘號*後面放串列(*list)
就是把串列的值取出加上逗號
舉例 :
    x = ["1", "2", "3", "4", "5"]
    print(*x)----->意思就是print("1", "2", "3", "4", "5") 因為是逗號所以print出來中間就會有空格，如果不想要空格可以用sep來設定
    print(*x[0:3])----->意思就是print("1", "2", "3")
    print(*x[1:4])----->意思就是print("2", "3", "4")
    print(*x[1::])----->意思就是print("2", "3", "4", "5")
    print(*x[2::])----->意思就是print("3", "4", "5")
'''
    
    