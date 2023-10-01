# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:47:01 2023

@author: allen

在精靈銀行存錢每半年複利1次，半年利息是0.5%。
假設帕森現在開了一個新帳戶並存入1000元，則十年後帳戶裡應有多少錢？
(請撰寫一程式計算該結果並加以輸出)

"""

x = int(input("輸入存款金額 :"))
y = int(input("輸入存入時間(年) :"))
for _ in range(y * 2):
    x *= 1.005
print(int(x))