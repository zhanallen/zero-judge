# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:51:11 2023

@author: allen

有人說物理的極致是宗教,數學的極致是哲學,是有一定道理的。
難怪有人會如此醉心於數學,每年的3/14是國際數學日,請看有趣的算式。
1 x 9 + 2 = 11
12 x 9 + 3 = 111
123 x 9 + 4 = 1111
1234 x 9 + 5 = 11111
12345 x 9 + 6 = 111111
123456 x 9 + 7 = 1111111
1234567 x 9 + 8 = 11111111
12345678 x 9 + 9 = 111111111
123456789 x 9 + 10 = 1111111111
請試著寫個程式試試看嚕~~~

輸入說明
輸入一個介於1至9的正整數
輸出說明
輸出該數字與該數字減一與加一後的運算式與結果,但大於9與小於1的數字不會被輸出。(請注意格式化。)

範例輸入 #1
1
範例輸出 #1
1         x 9 +  2 = 11
12        x 9 +  3 = 111

範例輸入 #2
4
範例輸出 #2
123       x 9 +  4 = 1111
1234      x 9 +  5 = 11111
12345     x 9 +  6 = 111111

範例輸入 #3
9
範例輸出 #3
12345678  x 9 +  9 = 111111111
123456789 x 9 + 10 = 1111111111

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