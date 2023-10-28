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

def uplist(ly):
    lr = list(up(int(i)) for i in ly)
    return (lr)

def lowlist(ly):
    lr = list(low(int(i)) for i in ly)
    return (lr)

def ULlist(ly):
    lr = list()
    i = 1
    while (i <= len(ly)):
        if (i % 2):
            lr.append(low(int(ly[i - 1])))
        else:
            lr.append(up(int(ly[i - 1])))
        i += 1
    return (lr)

def reULlist(ly):
    lr = list()
    i = 1
    while (i <= len(ly)):
        if (i % 2):
            lr.append(up(int(ly[i - 1])))
        else:
            lr.append(low(int(ly[i - 1])))
        i += 1
    return (lr)


tx = int(input())
x = tx % 26    # 輸入值
if (x == 0):
    x = 26
n = math.ceil(x / 2)    # 設定n為x的1/2無條件進位值
lx = list(str(i) for i in range(1,x+1))
ln = list(str(i) for i in range(1,x+1,2))


i = 1    # 橫向輸出
while (i <= x):    # 1號
    print(f"{low(i)}", end = "")
    i += 1
print("  ", end = "")
i = x
while (i > 0):  # 2號
    print(f"{low(i)}", end = "")
    i -= 1
print("  ", end = "")
i = 1
while (i <= x):    # 3號
    if (i % 2):
        print(f"{low(i)}", end = "")
    else:
        print(f"{up(i)}", end = "")
    i += 1
print("  ", end = "")
i = x
while (i > 0):    # 4號
    if (i % 2):
        print(f"{low(i)}", end = "")
    else:
        print(f"{up(i)}", end = "")
    i -= 1
print("\n")

    
i = 1    # 直向輸出
while (i <= x):
    print(f"{low(i)}  {low(x-i+1)}", end = "")
    if (i % 2):
        print(f"  {low(i)}  {low(x-i+1)}")
    else:
        print(f"  {up(i)}  {up(x-i+1)}")
    i += 1
print()


i = 1    # 八種直角三角形
while (i <= x):
    print(f"{low(i)}" * i, " " * (x-i), sep = "", end = "")    # 1號
    print("  ", f"{low(x-i+1)}" * i, " " * (x-i), sep = "", end = "")    # 2號
    print("  ", " " * (x-i), f"{low(i)}" * i, sep = "", end = "")    # 3號
    print("  ", " " * (x-i), f"{low(x-i+1)}" * i, sep = "", end = "")    # 4號
    print("  ", f"{low(i)}" * (x-i+1), " " * (i-1), sep = "", end = "")    # 5號
    print("  ", f"{low(x-i+1)}" * (x-i+1), " " * (i-1), sep = "", end = "")    # 6號
    print("  ", " " * (i-1), f"{low(i)}" * (x-i+1), sep = "", end = "")    # 7號
    print("  ", " " * (i-1), f"{low(x-i+1)}" * (x-i+1), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種直角三角形(有大小寫)
while (i <= x):
    if (i % 2):
        print(f"{low(i)}" * i, " " * (x-i), sep = "", end = "")    # 1號
        print("  ", f"{low(x-i+1)}" * i, " " * (x-i), sep = "", end = "")    # 2號
        print("  ", " " * (x-i), f"{low(i)}" * i, sep = "", end = "")    # 3號
        print("  ", " " * (x-i), f"{low(x-i+1)}" * i, sep = "", end = "")    # 4號
        print("  ", f"{low(i)}" * (x-i+1), " " * (i-1), sep = "", end = "")    # 5號
        print("  ", f"{low(x-i+1)}" * (x-i+1), " " * (i-1), sep = "", end = "")    # 6號
        print("  ", " " * (i-1), f"{low(i)}" * (x-i+1), sep = "", end = "")    # 7號
        print("  ", " " * (i-1), f"{low(x-i+1)}" * (x-i+1), sep = "", end = "")    # 8號
    else:
        print(f"{up(i)}" * i, " " * (x-i), sep = "", end = "")
        print("  ", f"{up(x-i+1)}" * i, " " * (x-i), sep = "", end = "")
        print("  ", " " * (x-i), f"{up(i)}" * i, sep = "", end = "")
        print("  ", " " * (x-i), f"{up(x-i+1)}" * i, sep = "", end = "")
        print("  ", f"{up(i)}" * (x-i+1), " " * (i-1), sep = "", end = "")
        print("  ", f"{up(x-i+1)}" * (x-i+1), " " * (i-1), sep = "", end = "")
        print("  ", " " * (i-1), f"{up(i)}" * (x-i+1), sep = "", end = "")
        print("  ", " " * (i-1), f"{up(x-i+1)}" * (x-i+1), sep = "", end = "")        
    print()
    i += 1
print()


i = 1    # 八種等腰三角形 (底為x)
while (i <= (x+(x%2)-1)):
    if (((i*2)-1) <= x):    # 上半部
        print(" " * (n-i), f"{low(2*i-1)}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 1號
        print(" " * 2, " " * (n-i), f"{low(2*(n-i)+1)}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 2號
        print(" " * 2, " " * (i-1), f"{low((2*n-1)-(2*(i-1)))}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 3號
        print(" " * 2, " " * (i-1), f"{low(2*i-1)}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 4號
        print(" " * 2, *lowlist(ln[:i]), " " * (n-i), sep = "", end = "")    # 5號
        print(" " * 2, *lowlist(ln[-1:(-i-1):-1]), " " * (n-i), sep = "", end = "")    # 6號
        
        print(" " * 2, " " * (n-i), *lowlist(ln[(n-i):n]), sep = "", end = "")    # 7號
        print(" " * 2, " " * (n-i), *lowlist(ln[i-1::-1]), sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (n*2-1), end = "")    # 1號
        print(" " * (n*2+1), end = "")    # 2號
        print(" " * (n*2+1), end = "")    # 3號
        print(" " * (n*2+1), end = "")    # 4號
        print(" " * 2, *lowlist(ln[:(2*n-i)]), " " * (i-n), sep = "", end = "")    # 5號
        print(" " * 2, *lowlist(ln[-1:(i-n-1):-1]), " " * (i-n), sep = "", end = "")    # 6號
        print(" " * 2, " " * (i-n), *lowlist(ln[i-n:n]), sep = "", end = "")    # 7號
        print(" " * 2, " " * (i-n), *lowlist(ln[n-i-1::-1]), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種等腰三角形 (底為x)(有大小寫)
while (i <= (x+(x%2)-1)):
    if (((i*2)-1) <= x):    # 上半部
        if (i % 2):
            print(" " * (n-i), f"{low(2*i-1)}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 1號
            print(" " * 2, " " * (n-i), f"{low(2*(n-i)+1)}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 2號
            print(" " * 2, " " * (i-1), f"{low((2*n-1)-(2*(i-1)))}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 3號
            print(" " * 2, " " * (i-1), f"{low(2*i-1)}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 4號
        else:
            print(" " * (n-i), f"{up(2*i-1)}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 1號
            print(" " * 2, " " * (n-i), f"{up(2*(n-i)+1)}" * ((i*2)-1), " " * (n-i), sep = "", end = "")    # 2號
            print(" " * 2, " " * (i-1), f"{up((2*n-1)-(2*(i-1)))}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 3號
            print(" " * 2, " " * (i-1), f"{up(2*i-1)}" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")    # 4號
        print(" " * 2, *ULlist(ln[:i]), " " * (n-i), sep = "", end = "")    # 5號
        print(" " * 2, *ULlist(ln[-1:(-i-1):-1]), " " * (n-i), sep = "", end = "")    # 6號
        if (i % 2):
            print(" " * 2, " " * (n-i), *ULlist(ln[(n-i):n]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (n-i), *ULlist(ln[i-1::-1]), sep = "", end = "")    # 8號
        else:
            print(" " * 2, " " * (n-i), *reULlist(ln[(n-i):n]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (n-i), *reULlist(ln[i-1::-1]), sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (n*2-1), end = "")    # 1號
        print(" " * (n*2+1), end = "")    # 2號
        print(" " * (n*2+1), end = "")    # 3號
        print(" " * (n*2+1), end = "")    # 4號
        print(" " * 2, *ULlist(ln[:(2*n-i)]), " " * (i-n), sep = "", end = "")    # 5號
        print(" " * 2, *ULlist(ln[-1:(i-n-1):-1]), " " * (i-n), sep = "", end = "")    # 6號
        if (i % 2):
            print(" " * 2, " " * (i-n), *ULlist(ln[i-n:n]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (i-n), *ULlist(ln[n-i-1::-1]), sep = "", end = "")    # 8號
        else:
            print(" " * 2, " " * (i-n), *reULlist(ln[i-n:n]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (i-n), *reULlist(ln[n-i-1::-1]), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種等腰三角形 (底為2x-1)
while (i < (2*x)):
    if (i <= x):    # 上半部
        print(" " * (x-i), f"{low(i)}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 1號
        print(" " * 2, " " * (x-i), f"{low(x-i+1)}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 2號
        print(" " * 2, " " * (i-1), f"{low(i)}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 3號
        print(" " * 2, " " * (i-1), f"{low(x-i+1)}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 4號
        print(" " * 2, *lowlist(lx[:i]), " " * (x-i), sep = "", end = "")    # 5號
        print(" " * 2, *lowlist(lx[-1:(-i-1):-1]), " " * (x-i), sep = "", end = "")    # 6號
        print(" " * 2, " " * (x-i), *lowlist(lx[i-1::-1]), sep = "", end = "")    # 7號
        print(" " * 2, " " * (x-i), *lowlist(lx[(x-i):x]), sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (2*x), end = "")    # 1號
        print(" " * (2*x), end = "")    # 2號
        print(" " * 2,end = "")
        print(" " * (2*x), end = "")    # 3號
        print(" " * (2*x), end = "")    # 4號
        print(" " * 2, *lowlist(lx[:(2*x-i)]), " " * (i-x), sep = "", end = "")    # 5號
        print(" " * 2, *lowlist(lx[-1:(i-x-1):-1]), " " * (i-x), sep = "", end = "")    # 6號
        print(" " * 2, " " * (i-x), *lowlist(lx[x-i-1::-1]), sep = "", end = "")    # 7號
        print(" " * 2, " " * (i-x), *lowlist(lx[i-x:x]), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種等腰三角形 (底為2x-1)(有大小寫)
while (i < (2*x)):
    if (i <= x):    # 上半部
        if (i % 2):
            print(" " * (x-i), f"{low(i)}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 1號
            print(" " * 2, " " * (x-i), f"{low(x-i+1)}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 2號
            print(" " * 2, " " * (i-1), f"{low(i)}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 3號
            print(" " * 2, " " * (i-1), f"{low(x-i+1)}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 4號
        else:
            print(" " * (x-i), f"{up(i)}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 1號
            print(" " * 2, " " * (x-i), f"{up(x-i+1)}" * (2*i-1), " " * (x-i), sep = "", end = "")    # 2號
            print(" " * 2, " " * (i-1), f"{up(i)}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 3號
            print(" " * 2, " " * (i-1), f"{up(x-i+1)}" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")    # 4號
        print(" " * 2, *ULlist(lx[:i]), " " * (x-i), sep = "", end = "")    # 5號
        print(" " * 2, *ULlist(lx[-1:(-i-1):-1]), " " * (x-i), sep = "", end = "")    # 6號
        if (i % 2):
            print(" " * 2, " " * (x-i), *ULlist(lx[i-1::-1]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (x-i), *ULlist(lx[(x-i):x]), sep = "", end = "")    # 8號
        else:
            print(" " * 2, " " * (x-i), *reULlist(lx[i-1::-1]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (x-i), *reULlist(lx[(x-i):x]), sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (2*x), end = "")    # 1號
        print(" " * (2*x), end = "")    # 2號
        print(" " * 2,end = "")
        print(" " * (2*x), end = "")    # 3號
        print(" " * (2*x), end = "")    # 4號
        print(" " * 2, *ULlist(lx[:(2*x-i)]), " " * (i-x), sep = "", end = "")    # 5號
        print(" " * 2, *ULlist(lx[-1:(i-x-1):-1]), " " * (i-x), sep = "", end = "")    # 6號
        if (i % 2):
            print(" " * 2, " " * (i-x), *ULlist(lx[x-i-1::-1]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (i-x), *ULlist(lx[i-x:x]), sep = "", end = "")    # 8號
        else:
            print(" " * 2, " " * (i-x), *reULlist(lx[x-i-1::-1]), sep = "", end = "")    # 7號
            print(" " * 2, " " * (i-x), *reULlist(lx[i-x:x]), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種等腰三角形 (底為2x-1)(內有空白)
while (i < (2*x)):
    if (i <= x):    # 上半部
        print(" " * (x-i), f"{low(i)} " * i, " " * (x-i), sep = "", end = "")    # 1號
        print("  ", " " * (x-i), f"{low(x-i+1)} " * i, " " * (x-i), sep = "", end = "")    # 2號
        print(" " * (i), f"{low(i)} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 3號
        print(" " * (i), f"{low(x-i+1)} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 4號
        if (i % 2):
            print(" ".join(lowlist(lx[-1:-i-1:-2])), "  ", " " * (x-i), sep = "", end = "")    # 5號
            print(" ".join(lowlist(lx[0:i:2])), " ", " " * (x-i), sep = "", end = "")    # 6號
            print(" " * (x-i), " ", " ".join(lowlist(lx[-i::2])), sep = "", end = "")    # 7號
            print(" " * (x-i), "  ", " ".join(lowlist(lx[i-1::-2])), sep = "", end = "")    # 8號
        else:
            print(" ", " ".join(lowlist(lx[-2:-i-1:-2])), " " * (x-i+1), sep = "", end = "")    # 5號
            print("  ", " ".join(lowlist(lx[1:i:2])), " " * (x-i+1), sep = "", end = "")    # 6號
            print(" " * (x-i+1), " ".join(lowlist(lx[-i::2])), "  ", sep = "", end = "")    # 7號
            print(" " * (x-i+1), " ".join(lowlist(lx[i-1::-2])), " ", sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (2*x), sep = "", end = "")    # 1號
        print("  ", " " * (2*x), sep = "", end = "")    # 2號
        print(" " * 2, " " * (2*x), sep = "", end = "")    # 3號
        print(" " * 2, " " * (2*x), sep = "", end = "")    # 4號
        if (i % 2):
            print(" ".join(lowlist(lx[-1:-(2*x-i+1):-2])), "  ", " " * (i-x), sep = "", end = "")    # 5號
            print(" ".join(lowlist(lx[:2*x-i:2])), " ", " " * (i-x), sep = "", end = "")    # 6號
            print(" " * (i-x), " ", " ".join(lowlist(lx[i-x::2])), sep = "", end = "")    # 7號
            print(" " * (i-x), "  ", " ".join(lowlist(lx[x-i-1::-2])), sep = "", end = "")    # 8號
        else:
            print(" ", " ".join(lowlist(lx[-2:i-x-1:-2])), " " * (i-x+1), sep = "", end = "")    # 5號
            print("  ", " ".join(lowlist(lx[1:2*x-i:2])), " " * (i-x+1), sep = "", end = "")    # 6號
            print(" " * (i-x+1), " ".join(lowlist(lx[i-x::2])), "  ", sep = "", end = "")    # 7號
            print(" " * (i-x+1), " ".join(lowlist(lx[x-i-1::-2])), " ", sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種等腰三角形 (底為2x-1)(內有空白)(有大小寫)
while (i < (2*x)):
    if (i <= x):    # 上半部
        if (i % 2):
            print(" " * (x-i), f"{low(i)} " * i, " " * (x-i), sep = "", end = "")    # 1號
            print("  ", " " * (x-i), f"{low(x-i+1)} " * i, " " * (x-i), sep = "", end = "")    # 2號
            print(" " * (i), f"{low(i)} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 3號
            print(" " * (i), f"{low(x-i+1)} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 4號
            print(" ".join(lowlist(lx[-1:-i-1:-2])), "  ", " " * (x-i), sep = "", end = "")    # 5號
            print(" ".join(lowlist(lx[0:i:2])), " ", " " * (x-i), sep = "", end = "")    # 6號
            print(" " * (x-i), " ", " ".join(lowlist(lx[-i::2])), sep = "", end = "")    # 7號
            print(" " * (x-i), "  ", " ".join(lowlist(lx[i-1::-2])), sep = "", end = "")    # 8號
        else:
            print(" " * (x-i), f"{up(i)} " * i, " " * (x-i), sep = "", end = "")    # 1號
            print("  ", " " * (x-i), f"{up(x-i+1)} " * i, " " * (x-i), sep = "", end = "")    # 2號
            print(" " * (i), f"{up(i)} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 3號
            print(" " * (i), f"{up(x-i+1)} " * ((x-i)+1), " " * (i), sep = "", end = "")    # 4號
            print(" ", " ".join(uplist(lx[-2:-i-1:-2])), " " * (x-i+1), sep = "", end = "")    # 5號
            print("  ", " ".join(uplist(lx[1:i:2])), " " * (x-i+1), sep = "", end = "")    # 6號
            print(" " * (x-i+1), " ".join(uplist(lx[-i::2])), "  ", sep = "", end = "")    # 7號
            print(" " * (x-i+1), " ".join(uplist(lx[i-1::-2])), " ", sep = "", end = "")    # 8號
    else:    # 下半部
        print(" " * (2*x), sep = "", end = "")    # 1號
        print("  ", " " * (2*x), sep = "", end = "")    # 2號
        print(" " * 2, " " * (2*x), sep = "", end = "")    # 3號
        print(" " * 2, " " * (2*x), sep = "", end = "")    # 4號
        if (i % 2):
            print(" ".join(lowlist(lx[-1:-(2*x-i+1):-2])), "  ", " " * (i-x), sep = "", end = "")    # 5號
            print(" ".join(lowlist(lx[:2*x-i:2])), " ", " " * (i-x), sep = "", end = "")    # 6號
            print(" " * (i-x), " ", " ".join(lowlist(lx[i-x::2])), sep = "", end = "")    # 7號
            print(" " * (i-x), "  ", " ".join(lowlist(lx[x-i-1::-2])), sep = "", end = "")    # 8號
        else:
            print(" ", " ".join(lowlist(lx[-2:i-x-1:-2])), " " * (i-x+1), sep = "", end = "")    # 5號
            print("  ", " ".join(lowlist(lx[1:2*x-i:2])), " " * (i-x+1), sep = "", end = "")    # 6號
            print(" " * (i-x+1), " ".join(uplist(lx[i-x::2])), "  ", sep = "", end = "")    # 7號
            print(" " * (i-x+1), " ".join(uplist(lx[x-i-1::-2])), " ", sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種矩形缺口
while (i < 2*x):
    if (i < x):    # 上半部
        print(f"{low(i)}" * i, " " * (2*(x-i)-1), f"{low(i)}" * i, sep = "", end = "")    # 1號
        print("  ", f"{low(x-i+1)}" * i, " " * (2*(x-i)-1), f"{low(x-i+1)}" * i, sep = "", end = "")    # 2號
    else:    # 下半部
        print(f"{low(x)}" * (2*x-1), sep = "", end = "")    # 1號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 2號
    if (i <= x):    # 上半部
        print("  ", f"{low(x)}" * (2*x-1), sep = "", end = "")    # 3號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 4號
        print("  ", " " * (i-1), *lowlist(lx[i-1:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 5號
        print("  ", " " * (i-1), *lowlist(lx[x-i::-1]), "a" * (x-1), sep = "", end = "")    # 6號
        print("  ", f"{low(x)}" * (x-1), *lowlist(lx[-1:-(x-i+2):-1]), " " * (i-1), sep = "", end = "")    # 7號
        print("  ", "a" * (x-1), *lowlist(lx[:x-i+1]), " " * (i-1), sep = "", end = "")    # 8號
    else:    # 下半部
        print("  ", f"{low(2*x-i)}" * (2*x-i), " " * (2*(i-x)-1), f"{low(2*x-i)}" * (2*x-i), sep = "", end = "")    # 3號
        print("  ", f"{low(i-x+1)}" * (2*x-i), " " * (2*(i-x)-1), f"{low(i-x+1)}" * (2*x-i), sep = "", end = "")    # 4號
        print("  ", " " * (2*x-i-1), *lowlist(lx[2*x-i-1:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 5號
        print("  ", " " * (2*x-i-1), *lowlist(lx[i-x::-1]), "a" * (x-1), sep = "", end = "")    # 6號
        print("  ", f"{low(x)}" * (x-1), *lowlist(lx[-1:-(i-x+2):-1]), " " * (2*x-i-1), sep = "", end = "")    # 7號
        print("  ", "a" * (x-1), *lowlist(lx[:i-x+1]), " " * (2*x-i-1), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種矩形缺口 (有大小寫)
while (i < 2*x):
    if (i < x):    # 上半部
        if ( i % 2):
            print(f"{low(i)}" * i, " " * (2*(x-i)-1), f"{low(i)}" * i, sep = "", end = "")    # 1號
            print("  ", f"{low(x-i+1)}" * i, " " * (2*(x-i)-1), f"{low(x-i+1)}" * i, sep = "", end = "")    # 2號
        else:
            print(f"{up(i)}" * i, " " * (2*(x-i)-1), f"{up(i)}" * i, sep = "", end = "")    # 1號
            print("  ", f"{up(x-i+1)}" * i, " " * (2*(x-i)-1), f"{up(x-i+1)}" * i, sep = "", end = "")    # 2號
    else:    # 下半部
        print(f"{low(x)}" * (2*x-1), sep = "", end = "")
        print("  ", "a" * (2*x-1), sep = "", end = "")
    if (i <= x):    # 上半部
        print("  ", f"{low(x)}" * (2*x-1), sep = "", end = "")    # 3號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 4號
        if (i % 2):
            print("  ", " " * (i-1), *ULlist(lx[i-1:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 5號
            print("  ", " " * (i-1), *ULlist(lx[x-i::-1]), "a" * (x-1), sep = "", end = "")    # 6號
        else:
            print("  ", " " * (i-1), *reULlist(lx[i-1:]), f"{up(x)}" * (x-1), sep = "", end = "")    # 5號
            print("  ", " " * (i-1), *reULlist(lx[x-i::-1]), "a" * (x-1), sep = "", end = "")    # 6號
        print("  ", f"{low(x)}" * (x-1), *ULlist(lx[-1:-(x-i+2):-1]), " " * (i-1), sep = "", end = "")    # 7號
        print("  ", "a" * (x-1), *ULlist(lx[:x-i+1]), " " * (i-1), sep = "", end = "")    # 8號
    else:    # 下半部
        if (i % 2):
            print("  ", f"{low(2*x-i)}" * (2*x-i), " " * (2*(i-x)-1), f"{low(2*x-i)}" * (2*x-i), sep = "", end = "")    # 3號
            print("  ", f"{low(i-x+1)}" * (2*x-i), " " * (2*(i-x)-1), f"{low(i-x+1)}" * (2*x-i), sep = "", end = "")    # 4號
            print("  ", " " * (2*x-i-1), *ULlist(lx[2*x-i-1:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 5號
            print("  ", " " * (2*x-i-1), *ULlist(lx[i-x::-1]), "a" * (x-1), sep = "", end = "")    # 6號
        else:
            print("  ", f"{up(2*x-i)}" * (2*x-i), " " * (2*(i-x)-1), f"{up(2*x-i)}" * (2*x-i), sep = "", end = "")    # 3號
            print("  ", f"{up(i-x+1)}" * (2*x-i), " " * (2*(i-x)-1), f"{up(i-x+1)}" * (2*x-i), sep = "", end = "")    # 4號
            print("  ", " " * (2*x-i-1), *reULlist(lx[2*x-i-1:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 5號
            print("  ", " " * (2*x-i-1), *reULlist(lx[i-x::-1]), "a" * (x-1), sep = "", end = "")    # 6號
        print("  ", f"{low(x)}" * (x-1), *ULlist(lx[-1:-(i-x+2):-1]), " " * (2*x-i-1), sep = "", end = "")    # 7號
        print("  ", "a" * (x-1), *ULlist(lx[:i-x+1]), " " * (2*x-i-1), sep = "", end = "")    # 8號
    print()
    i += 1
print()


i = 1    # 八種矩形尖角
while (i < 2*x):
    if (i < x):    # 上半部
        print(" " * (x-i), f"{low(i)}" * ((2*i)-1), " " * (x-i), sep = "", end = "")    # 1號
        print("  ", " " * (x-i), f"{low(x-i+1)}" * ((2*i)-1), " " * (x-i), sep = "", end = "")    # 2號
    else:    # 下半部
        print(f"{low(x)}" * (2*x-1), sep = "", end = "")    # 1號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 2號
    if (i <= x):    # 上半部
        print("  ", f"{low(x)}" * (2*x-1), sep = "", end = "")    # 3號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 4號
        print("  ", f"{low(x)}" * (x-1), *lowlist(lx[-1:-i-1:-1]), " " * (x-i), sep = "", end = "")    # 5號
        print("  ", "a" * (x-1), *lowlist(lx[:i]), " " * (x-i), sep = "", end = "")    # 6號
        print("  ", " " * (x-i), *lowlist(lx[x-i:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 7號
        print("  ", " " * (x-i), *lowlist(lx[-(x-i+1)::-1]), "a" * (x-1), sep = "", end = "")    # 8號
    else:    # 下半部
        print("  ", " " * (i-x), f"{low(2*x-i)}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")    # 3號
        print("  ", " " * (i-x), f"{low(i-x+1)}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")    # 4號
        print("  ", f"{low(x)}" * (x-1), *lowlist(lx[-1:-(2*x-i+1):-1]), " " * (i-x), sep = "", end = "")    # 5號
        print("  ", "a" * (x-1), *lowlist(lx[:2*x-i]), " " * (i-x), sep = "", end = "")    # 6號
        print("  ", " " * (i-x), *lowlist(lx[i-x:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 7號
        print("  ", " " * (i-x), *lowlist(lx[x-i-1::-1]), "a" * (x-1), sep = "", end = "")    # 8號
    print()
    i += 1
print()

i = 1    # 八種矩形尖角 (有大小寫)
while (i < 2*x):
    if (i < x):    # 上半部
        if (i % 2):
            print(" " * (x-i), f"{low(i)}" * ((2*i)-1), " " * (x-i), sep = "", end = "")    # 1號
            print("  ", " " * (x-i), f"{low(x-i+1)}" * ((2*i)-1), " " * (x-i), sep = "", end = "")    # 2號
        else:
            print(" " * (x-i), f"{up(i)}" * ((2*i)-1), " " * (x-i), sep = "", end = "")    # 1號
            print("  ", " " * (x-i), f"{up(x-i+1)}" * ((2*i)-1), " " * (x-i), sep = "", end = "")    # 2號
    else:    # 下半部
        print(f"{low(x)}" * (2*x-1), sep = "", end = "")    # 1號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 2號
    if (i <= x):    # 上半部
        print("  ", f"{low(x)}" * (2*x-1), sep = "", end = "")    # 3號
        print("  ", "a" * (2*x-1), sep = "", end = "")    # 4號
        print("  ", f"{low(x)}" * (x-1), *ULlist(lx[-1:-i-1:-1]), " " * (x-i), sep = "", end = "")    # 5號
        print("  ", "a" * (x-1), *ULlist(lx[:i]), " " * (x-i), sep = "", end = "")    # 6號
        if (i % 2):
            print("  ", " " * (x-i), *ULlist(lx[x-i:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 7號
            print("  ", " " * (x-i), *ULlist(lx[-(x-i+1)::-1]), "a" * (x-1), sep = "", end = "")    # 8號
        else:
            print("  ", " " * (x-i), *reULlist(lx[x-i:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 7號
            print("  ", " " * (x-i), *reULlist(lx[-(x-i+1)::-1]), "a" * (x-1), sep = "", end = "")    # 8號
    else:    # 下半部
        if (i % 2):
            print("  ", " " * (i-x), f"{low(2*x-i)}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")    # 3號
            print("  ", " " * (i-x), f"{low(i-x+1)}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")    # 4號
            print("  ", f"{low(x)}" * (x-1), *lowlist(lx[-1:-(2*x-i+1):-1]), " " * (i-x), sep = "", end = "")    # 5號
            print("  ", "a" * (x-1), *lowlist(lx[:2*x-i]), " " * (i-x), sep = "", end = "")    # 6號
            print("  ", " " * (i-x), *lowlist(lx[i-x:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 7號
            print("  ", " " * (i-x), *lowlist(lx[x-i-1::-1]), "a" * (x-1), sep = "", end = "")    # 8號
        else:
            print("  ", " " * (i-x), f"{up(2*x-i)}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")    # 3號
            print("  ", " " * (i-x), f"{up(i-x+1)}" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")    # 4號
            print("  ", f"{low(x)}" * (x-1), *ULlist(lx[-1:-(2*x-i+1):-1]), " " * (i-x), sep = "", end = "")    # 5號
            print("  ", "a" * (x-1), *ULlist(lx[:2*x-i]), " " * (i-x), sep = "", end = "")    # 6號
            print("  ", " " * (i-x), *reULlist(lx[i-x:]), f"{low(x)}" * (x-1), sep = "", end = "")    # 7號
            print("  ", " " * (i-x), *reULlist(lx[x-i-1::-1]), "a" * (x-1), sep = "", end = "")    # 8號
    print()
    i += 1
print()