# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:19:42 2023

@author: allen
"""

def forward(n,x,y):
    if (n%4 == 0):
        y += 1
    elif (n%4 == 1):
        x += 1
    elif (n%4 == 2):
        y -= 1
    else:
        x -= 1
    return(x,y)

def backward(n,x,y):
    if (n%4 == 0):
        y -= 1
    elif (n%4 == 1):
        x -= 1
    elif (n%4 == 2):
        y += 1
    else:
        x += 1
    return(x,y)

d = {"N": 0, "E": 1, "S": 2, "W": 3}
D = {0: "N", 1: "E", 2: "S", 3: "W"}
scent = list()
t = tuple(map(int,input().split()))
while (1):
    try:
        l = input().split()
        x = int(l[0])
        y = int(l[1])
        see = d.get(l[2])
        lost = False
        step = input()
        for i in step:
            if (i == "F"):
                x, y = forward(see,x,y)
                if (x > t[0] or y > t[1] or x < 0 or y < 0):
                    x, y = backward(see,x,y)
                    if([x,y] in scent):
                        pass
                    else:
                        lost = True
                        scent.append([x,y])
                        break
            elif (i == "R"):
                see += 1
            elif (i == "L"):
                see -= 1
        print(x, y, D.get(see%4) ,end = "")
        if (lost):
            print(" LOST")
        else:
            print()
    except:
        break