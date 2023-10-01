# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 01:43:41 2023

@author: allen

請修正以下程式碼的運算子，使其能正確輸出 1^3 + 3^3 = 28。乘法公式:
a^3 + b^3 = (a + b)(a^2 − a ∗ b + b^2)

a = 1
b = 3
Ans = (a + b) * (a^2 - a*b + b^2)
print("1^3 + 3^3 = ", Ans)

"""

a = 1
b = 3
Ans = (a + b) * ((a**2) - (a*b) + (b**2))
print("1^3 + 3^3 =", Ans)