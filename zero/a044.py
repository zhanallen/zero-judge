# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:58:36 2023

@author: allen

感謝陪我熬夜解公式的各位同學
公式解法請參考
https://wenku.baidu.com/view/61e116ecd6bbfd0a79563c1ec5da50e2524dd106?pcf=2&_wkts_=1696010608632&needWelcomeRecommand=1&bfetype=new&bfetype=new

"""

while (1):
    try:
        x = int(input())
        a = int(((x ** 3) + (5 * x) + 6) / 6)
        print(a)
    except:
        break