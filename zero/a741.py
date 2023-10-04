# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:38:01 2023

@author: allen
"""

t = 1

def bn(n):
    if (len(n) > 5 and int(n[-7:-5])):
        print(" ", int(n[-7:-5]), " lakh", sep = "", end = "")
    if (len(n) > 3 and int(n[-5:-3])):
        print(" ", int(n[-5:-3]), " hajar", sep = "", end = "")
    if (len(n) > 2 and int(n[-3])):
        print(" ", n[-3], " shata", sep = "", end = "")
    if (len(n) > 0 and int(n[-2:])):
        print(" ", int(n[-2:]), sep = "", end = "")

while (1):
    try:
        a = input()
        l = len(a)
        s = l % 7
        k = 0
        print(f"{t}.", end = "")
        t += 1
        if (a == "0"):
            print(" 0", end = "")
        if (s != 0):
            bn(a[0:s])
            k += 1
        for i in range(l // 7):
            if (k):
                print(" kuti", end = "")
            bn(a[(s+(i*7)):(s+(i*7)+7):])
            k += 1
        print()
    except:
        break