# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 01:55:52 2022

@author: jayyu
"""
n = int(input())
for i in range(n):
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    rule = True
    if a[1] == a[3] or a[1] != a[5] or b[1] == b[3] or b[1] != b[5]:
        print("A",end="")
        rule = False
    if a[6] != 1 or b[6] != 0:
        print("B",end="")
        rule= False
    if a[1] == b[1] or a[3] == b[3] or a[5] == b[5]:
        print("C",end="")
        rule = False
    if rule:
        print("None") 
    else:
        print() 
