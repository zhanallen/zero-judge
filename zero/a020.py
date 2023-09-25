# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:06:15 2023

@author: allen
"""

x=input()
if(ord(x[0])<73):
    a=ord(x[0])-55
elif(ord(x[0])>73 and ord(x[0])<79):
    a=ord(x[0])-56
elif(ord(x[0])>79 and ord(x[0])<87 or ord(x[0])==90):
    a=ord(x[0])-57
elif(ord(x[0])>87 and ord(x[0])<90):
    a=ord(x[0])-58
elif(ord(x[0])==73):
    a=34
elif(ord(x[0])==79):
    a=35
elif(ord(x[0])==87):
    a=32
A=str(a)
T=int(A[0])+9*int(A[1])
t=0
for i in range(8,0,-1):
    t+=int(x[9-i])*i
t+=int(x[9])
Sum=T+t
if(Sum%10):
    print('fake')
else:
    print('real')