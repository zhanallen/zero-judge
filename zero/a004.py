# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:56:04 2023

@author: allen
"""
try:
    while(1):
        x=int(input())
        if((x%4==0 and x%100!=0) or x%400==0):
            print("閏年")
        else:
            print("平年")
except:
    print("",end="\n")
    