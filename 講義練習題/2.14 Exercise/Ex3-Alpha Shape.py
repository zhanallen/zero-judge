# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:09:43 2023

@author: allen
"""

import math

def up(y):
    return (chr(y + 64))
    
def low(y):
    return (chr(y + 96))

tx = int(input())
x = tx % 26    # 輸入值
n = math.ceil(x / 2)    # 設定n為x的1/2無條件進位值
lx = list(str(i) for i in range(1,x+1))
ln = list(str(i) for i in range(1,x+1,2))

i = 1    # 橫向輸出
while (i <= x):
    print(f"{low(i)}", end = "")
    i += 1
print("  ", end = "")
i = x
while (i > 0):
    print(f"{low(i)}", end = "")
    i -= 1
i = 1
while (i <= x):
    print(f"{low(i)}", end = "")
    i += 1
print("  ", end = "")
i = x
while (i > 0):
    print(f"{low(i)}", end = "")
    i -= 1
print("\n")

    
i = 1    # 直向輸出
while (i <= x):
    print(f"{i}  {x-i+1}")
    i += 1
print()

i = 1    # 八種直角三角形
while (i <= x):
    print(f"{i}" * i, " " * (x-i), sep = "", end = "")
    print("  ", f"{x-i+1}" * i, " " * (x-i), sep = "", end = "")
    print("  ", " " * (x-i), f"{i}" * i, sep = "", end = "")
    print("  ", " " * (x-i), f"{x-i+1}" * i, sep = "", end = "")
    print("  ", f"{i}" * (x-i+1), " " * (i-1), sep = "", end = "")
    print("  ", f"{x-i+1}" * (x-i+1), " " * (i-1), sep = "", end = "")
    print("  ", " " * (i-1), f"{i}" * (x-i+1), sep = "", end = "")
    print("  ", " " * (i-1), f"{x-i+1}" * (x-i+1), sep = "", end = "")
    print()
    i += 1
print()

i = 1    # 八種等腰三角形 (底為x)
while (i <= (x+(x%2)-1)):
    if (((i*2)-1) <= x):    # 上半部
        print(" " * (n-i), f"{2*i-1}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 1號
        print(" " * 2, " " * (n-i), f"{2*(n-i)+1}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 1號
        print(" " * 2, " " * (i-1), f"{(2*n-1)-(2*(i-1))}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 2號
        print(" " * 2, " " * (i-1), f"{2*i-1}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 2號
        print(" " * 2, *ln[-1:(-i-1):-1], " " * (n-i), sep = "", end = "")    # 5號
        print(" " * 2, *ln[:i], " " * (n-i), sep = "", end = "")    # 6號
        print(" " * 2, " " * (n-i), *ln[(n-i):n], sep = "", end = "")    # 7號
        print(" " * 2, " " * (n-i), *ln[i-1::-1], sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (n*2-1), end = "")    # 1號
        print(" " * (n*2+1), end = "")    # 2號
        print(" " * (n*2+1), end = "")    # 3號
        print(" " * (n*2+1), end = "")    # 4號
        print(" " * 2, *ln[-1:(i-n-1):-1], " " * (i-n), sep = "", end = "")    # 5號
        print(" " * 2, *ln[:(2*n-i)], " " * (i-n), sep = "", end = "")    # 6號
        print(" " * 2, " " * (i-n), *ln[i-n:n], sep = "", end = "")    # 7號
        print(" " * 2, " " * (i-n), *ln[n-i-1::-1], sep = "", end = "")    # 8號
    print()
    i += 1
print()

i = 1    # 八種等腰三角形 (底為2x-1)
while (i < (2*x)):
    if (i <= x):    # 上半部
        print(" " * (x-i), f"{i}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 1號
        print(" " * 2, " " * (x-i), f"{x-i+1}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 2號
        print(" " * 2, " " * (i-1), f"{i}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 3號
        print(" " * 2, " " * (i-1), f"{x-i+1}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 4號
        print(" " * 2, *lx[:i], " " * (x-i), sep = "", end = "")    # 5號
        print(" " * 2, *lx[-1:(-i-1):-1], " " * (x-i), sep = "", end = "")    # 6號
        print(" " * 2, " " * (x-i), *lx[i-1::-1], sep = "", end = "")    # 7號
        print(" " * 2, " " * (x-i), *lx[(x-i):x], sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (2*x), end = "")    # 1號
        print(" " * (2*x), end = "")    # 2號
        print(" " * 2,end = "")
        print(" " * (2*x), end = "")    # 3號
        print(" " * (2*x), end = "")    # 4號
        print(" " * 2, *lx[:(2*x-i)], " " * (i-x), sep = "", end = "")    # 5號
        print(" " * 2, *lx[-1:(i-x-1):-1], " " * (i-x), sep = "", end = "")    # 6號
        print(" " * 2, " " * (i-x), *lx[x-i-1::-1], sep = "", end = "")    # 7號
        print(" " * 2, " " * (i-x), *lx[i-x:x], sep = "", end = "")    # 8號
    print()
    i += 1
print()

i = 1    # 八種等腰三角形 (底為2x-1)(內有空白)
while (i < (2*x)):
    if (i <= x):    # 上半部
        print(" " * (x-i), f"{i} " * i, " " * (x-i), sep = "", end = "")    # 1號
        print("  ", " " * (x-i), f"{x-i+1} " * i, " " * (x-i), sep = "", end = "")    # 2號
        print(" " * (i), f"{i} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 3號
        print(" " * (i), f"{x-i+1} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 4號
        if (i % 2):
            print(" ".join(lx[-1:-i-1:-2]), "  ", " " * (x-i), sep = "", end = "")    # 5號
            print(" ".join(lx[0:i:2]), " ", " " * (x-i), sep = "", end = "")    # 6號
            print(" " * (x-i), " ", " ".join(lx[-i::2]), sep = "", end = "")    # 7號
            print(" " * (x-i), "  ", " ".join(lx[i-1::-2]), sep = "", end = "")    # 8號
        else:
            print(" ", " ".join(lx[-2:-i-1:-2]), " " * (x-i+1), sep = "", end = "")    # 5號
            print("  ", " ".join(lx[1:i:2]), " " * (x-i+1), sep = "", end = "")    # 6號
            print(" " * (x-i+1), " ".join(lx[-i::2]), "  ", sep = "", end = "")    # 7號
            print(" " * (x-i+1), " ".join(lx[i-1::-2]), " ", sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (2*x), sep = "", end = "")    # 1號
        print("  ", " " * (2*x), sep = "", end = "")    # 2號
        print(" " * 2, " " * (2*x), sep = "", end = "")    # 3號
        print(" " * 2, " " * (2*x), sep = "", end = "")    # 4號
        if (i % 2):
            print(" ".join(lx[-1:-(2*x-i+1):-2]), "  ", " " * (i-x), sep = "", end = "")    # 5號
            print(" ".join(lx[:2*x-i:2]), " ", " " * (i-x), sep = "", end = "")    # 6號
            print(" " * (i-x), " ", " ".join(lx[i-x::2]), sep = "", end = "")    # 7號
            print(" " * (i-x), "  ", " ".join(lx[x-i-1::-2]), sep = "", end = "")    # 8號
        else:
            print(" ", " ".join(lx[-2:i-x-1:-2]), " " * (i-x+1), sep = "", end = "")    # 5號
            print("  ", " ".join(lx[1:2*x-i:2]), " " * (i-x+1), sep = "", end = "")    # 6號
            print(" " * (i-x+1), " ".join(lx[i-x::2]), "  ", sep = "", end = "")    # 7號
            print(" " * (i-x+1), " ".join(lx[x-i-1::-2]), " ", sep = "", end = "")    # 8號
    print()
    i += 1
print()

i = 1    # 八種矩形缺口
while (i < 2*x):
    if (i < x):    # 1號
        print(f"{i}" * i, " " * (2*(x-i)-1), f"{i}" * i, sep = "", end = "")
    else:
        print(f"{x}" * (2*x-1), sep = "", end = "")
    if (i < x):    # 2號
        print("  ", f"{x-i+1}" * i, " " * (2*(x-i)-1), f"{x-i+1}" * i, sep = "", end = "")
    else:
        print("  ", "1" * (2*x-1), sep = "", end = "")
    if (i <= x):    # 3號
        print("  ", f"{x}" * (2*x-1), sep = "", end = "")
    else:
        print("  ", f"{2*x-i}" * (2*x-i), " " * (2*(i-x)-1), f"{2*x-i}" * (2*x-i), sep = "", end = "")
    if (i <= x):    # 4號
        print("  ", "1" * (2*x-1), sep = "", end = "")
    else:
        print("  ", f"{i-x+1}" * (2*x-i), " " * (2*(i-x)-1), f"{i-x+1}" * (2*x-i), sep = "", end = "")
    if (i <= x):    # 上半部
        print("  ", " " * (i-1), *lx[i-1:], f"{x}" * (x-1), sep = "", end = "")    # 5號
        print("  ", " " * (i-1), *lx[x-i::-1], "1" * (x-1), sep = "", end = "")    # 6號
        print("  ", f"{x}" * (x-1), *lx[-1:-(x-i+2):-1], " " * (i-1), sep = "", end = "")    # 7號
        print("  ", "1" * (x-1), *lx[:x-i+1], " " * (i-1), sep = "", end = "")    # 8號
    else:    # 下半部
        print("  ", " " * (2*x-i-1), *lx[2*x-i-1:], f"{x}" * (x-1), sep = "", end = "")    # 5號
        print("  ", " " * (2*x-i-1), *lx[i-x::-1], "1" * (x-1), sep = "", end = "")    # 6號
        print("  ", f"{x}" * (x-1), *lx[-1:-(i-x+2):-1], " " * (2*x-i-1), sep = "", end = "")    # 7號
        print("  ", "1" * (x-1), *lx[:i-x+1], " " * (2*x-i-1), sep = "", end = "")    # 8號
    print()
    i += 1
print()

i = 1    # 八種矩形尖角
while (i < 2*x):
    if (i < x):    # 1號
        print(" " * (x-i), f"{i}" * ((2*i)-1), " " * (x-i), sep = "", end = "")
    else:
        print(f"{x}" * (2*x-1), sep = "", end = "")
    if (i < x):    # 2號
        print("  ", " " * (x-i), f"{x-i+1}" * ((2*i)-1), " " * (x-i), sep = "", end = "")
    else:
        print("  ", "1" * (2*x-1), sep = "", end = "")
    if (i <= x):    # 3號
        print("  ", f"{x}" * (2*x-1), sep = "", end = "")
    else:
        print("  ", " " * (i-x), f"{2*x-i}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")
    if (i <= x):    # 4號
        print("  ", "1" * (2*x-1), sep = "", end = "")
    else:
        print("  ", " " * (i-x), f"{i-x+1}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")
    if (i <= x):    # 上半部
        print("  ", f"{x}" * (x-1), *lx[-1:-i-1:-1], " " * (x-i), sep = "", end = "")    # 5號
        print("  ", "1" * (x-1), *lx[:i], " " * (x-i), sep = "", end = "")    # 6號
        print("  ", " " * (x-i), *lx[x-i:], f"{x}" * (x-1), sep = "", end = "")    # 7號
        print("  ", " " * (x-i), *lx[-(x-i+1)::-1], "1" * (x-1), sep = "", end = "")    # 8號
    else:    # 下半部
        print("  ", f"{x}" * (x-1), *lx[-1:-(2*x-i+1):-1], " " * (i-x), sep = "", end = "")    # 5號
        print("  ", "1" * (x-1), *lx[:2*x-i], " " * (i-x), sep = "", end = "")    # 6號
        print("  ", " " * (i-x), *lx[i-x:], f"{x}" * (x-1), sep = "", end = "")    # 7號
        print("  ", " " * (i-x), *lx[x-i-1::-1], "1" * (x-1), sep = "", end = "")    # 8號
    print()
    i += 1
print()