# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:51:11 2023

@author: allen
"""

def out(n):
    if (n > 0 and n< 10):
        a = list(range(1, n + 1))
        s = "".join(str(i) for i in a)
        m = int(s)*9+(n+1)
        print("%-9s x 9 +" %s, "%2d =" %(n+1), m)
        
x = int(input())
out(x - 1)
out(x)
out(x + 1)

"""
1         x 9 +  2 = 11
12        x 9 +  3 = 111
123       x 9 +  4 = 1111
1234      x 9 +  5 = 11111
12345     x 9 +  6 = 111111
123456    x 9 +  7 = 1111111
1234567   x 9 +  8 = 11111111
12345678  x 9 +  9 = 111111111
123456789 x 9 + 10 = 1111111111
"""