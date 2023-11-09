# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:30:21 2023

@author: allen

改寫一句子,規則為句子中
遇到@(小老鼠),則跳1行,並在@後註明【跳1行】,且每跳一行都要註明跳第幾行的數目。
遇到$(錢字號),則跳2行,並在$後註明【跳2行】,且每跳一行都要註明跳第幾行的數目。
遇到#(井字號),則跳3行,並在#後註明【跳3行】,且每跳一行都要註明跳第幾行的數目。
遇到!(驚嘆號),則跳4行,並在!後註明【跳4行】,且每跳一行都要註明跳第幾行的數目。
遇到%(百分比),則跳5行,並在%後註明【跳5行】,且每跳一行都要註明跳第幾行的數目。

輸入說明
請記得處理複雜(也就是重複出現特殊字元等)的狀況。
輸出說明
請記得要加上【跳N行】的說明,還有每跳一行要記得數數字喔~~~

範例輸入 #1
The % character is a percent sign.
範例輸出 #1
The %【跳5行】
1
2
3
4
5 character is a percent sign.

"""

x = input()
if ("@" in x):    # 判斷@是否在x裡面
    l = x.split("@")
    print(l[0] + "@" + "【跳1行】")
    print("1" + l[1])
elif("$" in x):    # 判斷$是否在x裡面
    l = x.split("$")
    print(l[0] + "$" + "【跳2行】")
    print("1\n2", end = "")
    print(l[1])
elif("#" in x):    # 判斷#是否在x裡面
    l = x.split("#")
    print(l[0] + "#" + "【跳3行】")
    print("1\n2\n3", end = "")
    print(l[1])
elif("!" in x):    # 判斷!是否在x裡面
    l = x.split("!")
    print(l[0] + "!" + "【跳4行】")
    print("1\n2\n3\n4", end = "")
    print(l[1])
elif("%" in x):    # 判斷%是否在x裡面
    l = x.split("%")
    print(l[0] + "%" + "【跳5行】")
    print("1\n2\n3\n4\n5", end = "")
    print(l[1])
else:
    print(x)