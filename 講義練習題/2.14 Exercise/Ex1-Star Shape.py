# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:52:01 2023

@author: allen

# print(" " * 2,sep = "", end = "")
"""

import math

x = int(input())    # 輸入值

i = 0    # 直向輸出
while (i < x):
    print("*")
    i += 1
print()

i = 0    # 橫向輸出
while (i < x):
    print("*", end = "")
    i += 1
print("\n")

i = 1    # 四種直角三角形
while (i <= x):
    print("*" * i, " " * ((x-i)+1), sep = "", end = "")
    print(" " * ((x-i)+1), "*" * i, " ", sep = "", end = "")
    print(" ", "*" * (x-i+1), " " * i, sep = "", end = "")
    print(" " * i, "*" * ((x-i)+1), sep = "", end = "")
    print()
    i += 1
print()

n = math.ceil(x / 2)    # 四種等腰三角形 (底為x)
i = 1
while (i <= (x+(x%2)-1)):
    if (((i*2)-1) <= x):    # 上半部
        print(" " * (n-i), "*" * ((i*2)-1), " " * (n-i), sep = "", end = "")
        print(" " * 2, " " * (i-1), "*" * (((n-i)*2)+1), " " * (i-1), sep = "", end = "")
        print(" " * 2, "*" * i, " " * (n-i), sep = "", end = "")
        print(" " * 2, " " * (n-i), "*" * i, sep = "", end = "")
    else:    # 下半部
        print(" " * (n*2-1), sep = "", end = "")
        print(" " * (n*2+1), sep = "", end = "")
        print(" " * 2, "*" * (2*n-i), " " * (i-n), sep = "", end = "")
        print(" " * 2, " " * (i-n), "*" * (2*n-i), sep = "", end = "")
    print()
    i += 1
print()

n = math.ceil(x / 2)    # 四種等腰三角形 (底為2x-1)
i = 1
while (i < (2*x)):
    if (i <= x):    # 上半部
        print(" " * (x-i), "*" * ((i*2)-1), " " * (x-i), sep = "", end = "")
        print(" " * 2, " " * (i-1), "*" * (2*(x-i)+1), " " * (i-1), sep = "", end = "")
        print(" " * 2, "*" * i, " " * (x-i), sep = "", end = "")
        print(" " * 2, " " * (x-i), "*" * i, sep = "", end = "")
    else:    # 下半部
        print(" " * (2*x), sep = "", end = "")
        print(" " * (2*x), sep = "", end = "")
        print(" " * 2, "*" * (2*x-i), " " * (i-x), sep = "", end = "")
        print(" " * 2, " " * (i-x), "*" * (2*x-i), sep = "", end = "")
    print()
    i += 1
print()

n = math.ceil(x / 2)    # 四種等腰三角形 (底為2x-1)(內有空白)
line = 1
i = 1
while (i < (2*x)):
    if (i <= x):    # 上半部
        print(" " * (x-i), "* " * i, " " * (x-i), sep = "", end = "")
        print(" " * (i), "* " * ((x-i)+1), " " * (i), sep = "", end = "")
        if (line % 2):
            print("* " * math.ceil(i/2), " " * (x-i), sep = "", end = "")
            print(" " * (x-i), " *" * math.ceil(i/2), sep = "", end = "")
        else:
            print(" *" * math.ceil(i/2), " " * (x-i+1), sep = "", end = "")
            print(" " * (x-i+1), "* " * math.ceil(i/2), sep = "", end = "")
    else:    # 下半部
        print(" " * (2*x), sep = "", end = "")
        print(" " * 2, " " * (2*x), sep = "", end = "")
        if (line % 2):
            print("* " * (math.ceil((2*x-i)/2)), " " * (i-x), sep = "", end = "")
            print(" " * (i-x), " *" * (math.ceil((2*x-i)/2)), sep = "", end = "")
        else:
            print(" *" * (math.ceil((2*x-i)/2)), " " * (i-x+1), sep = "", end = "")
            print(" " * (i-x+1), "* " * (math.ceil((2*x-i)/2)), sep = "", end = "")
    print()
    line += 1
    i += 1
print()

i = 1    # 四種矩形缺口
while (i < 2*x):
    if (i < x):    # 1號
        print("*" * i, " " * (2*(x-i)-1), "*" * i, sep = "", end = "")
    else:
        print("*" * (2*x-1), sep = "", end = "")
    if (i <= x):    # 2號
        print("  ", "*" * (2*x-1), sep = "", end = "")
    else:
        print("  ", "*" * (2*x-i), " " * (2*(i-x)-1), "*" * (2*x-i), sep = "", end = "")
    if (i <= x):    # 3跟4號
        print("  ", " " * (i-1), "*" * (2*x-i), sep = "", end = "")
        print("  ", "*" * (2*x-i), " " * (i-1), sep = "", end = "")
    else:
        print("  ", " " * (2*x-i-1), "*" * (i), sep = "", end = "")
        print("  ", "*" * (i), " " * (2*x-i-1), sep = "", end = "")
    print()
    i += 1
print()

i = 1    # 四種矩形缺口
while (i < 2*x):
    if (i < x):    # 1號
        print(" " * (x-i), "*" * ((2*i)-1), " " * (x-i), sep = "", end = "")
    else:
        print("*" * (2*x-1), sep = "", end = "")
    if (i <= x):    # 2號
        print("  ", "*" * (2*x-1), sep = "", end = "")
    else:
        print("  ", " " * (i-x), "*" * (2*(2*x-i)-1), " " * (i-x), sep = "", end = "")
    if (i <= x):    # 3跟4號
        print("  ", "*" * (x+i-1), " " * (x-i), sep = "", end = "")
        print("  ", " " * (x-i), "*" * (x+i-1), sep = "", end = "")
    else:
        print("  ", "*" * (3*x-i-1), " " * (i-x), sep = "", end = "")
        print("  ", " " * (i-x), "*" * (3*x-i-1), sep = "", end = "")
    print()
    i += 1
print()
