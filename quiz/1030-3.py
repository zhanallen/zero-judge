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

y = int(input())
x = input()
l = x.split()
for i in range(y):
    print(*l[i::])
    
    