# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:52:42 2023

@author: allen
"""

x = input()
if ("@" in x):
    l = x.split("@")
    print(l[0] + "@" + "【跳1行】")
    print("1" + l[1])
elif("$" in x):
    l = x.split("$")
    print(l[0] + "$" + "【跳2行】")
    print("1\n2", end = "")
    print(l[1])
elif("#" in x):
    l = x.split("#")
    print(l[0] + "#" + "【跳3行】")
    print("1\n2\n3", end = "")
    print(l[1])
elif("!" in x):
    l = x.split("!")
    print(l[0] + "!" + "【跳4行】")
    print("1\n2\n3\n4", end = "")
    print(l[1])
elif("%" in x):
    l = x.split("%")
    print(l[0] + "%" + "【跳5行】")
    print("1\n2\n3\n4\n5", end = "")
    print(l[1])
else:
    print(x)