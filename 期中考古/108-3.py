# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:24:45 2023

@author: allen

自從上次學會外星人的第一款計數器後,
過了幾天,又在夢中遇見那位全身發光的外星人想要教我更新的記數方法,
一樣地,他們的世界裡是使用類似象形的文字來處理,但是規則顯然精進許多,例如,
0::.
  ..
1:.:
  ..
2:..
  .:
3:.:
  .:
4:..
  :.
5:.:
  :.
6:..
  ::
7:.:
  ::
其標記是以順時針方式查看,如下數字表示順序,每個數字以上下兩個符號組成。
01
42
所以,標記.表示無值,標記:表示有值,例如,
:.
..表示0

..
::表示4+2=6

"""

#       0     1     2     3     4     5     6     7
l = [[':.', '.:', '..', '.:', '..', '.:', '..', '.:'],
     ['..', '..', '.:', '.:', ':.', ':.', '::', '::']]

while (1):
    try:
        x = input()
        n = int(x)
        print(" ", end = "")
        print(*x, sep = "  ")
        for i in range(len(x)):
            if (i == len(x)-1):
                print(l[0][int(x[i])], end = "")
                
            else:
                print(l[0][int(x[i])], end = " ")
        print()
        for i in range(len(x)):
            if (i == len(x)-1):
                print(l[1][int(x[i])], end = "")
            else:
                print(l[1][int(x[i])], end = " ")
        print()
    except:
        break