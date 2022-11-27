# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:17:50 2022

@author: Yuin
"""

import sys
a,b,c,d=input().split()

if len(str(a))>8:
        sys.exit("請重新輸入，資料長度超過長度")
elif a.isalpha()==False:
        print(d.find("."))
        if a.find(".")!=-1:
            k=float(a)
            a=round(k,2)
if len(str(b))>8:
        sys.exit("請重新輸入，資料長度超過長度")
elif b.isalpha()==False:
        print(d.find("."))
        if b.find(".")!=-1:
            l=float(b)
            b=round(l,2)
if  len(str(c))>8:
        sys.exit("請重新輸入，資料長度超過長度")
elif c.isalpha()==False:
        print(d.find("."))
        if c.find(".")!=-1:
            m=float(c)
            c=round(m,2)
if len(str(d))>8:
        sys.exit("請重新輸入，資料長度超過長度")
elif d.isalpha()==False:
        print(d.find("."))
        if d.find(".")!=-1:
            n=float(d)
            d=round(n,2)

print('|%8s %8s|' %(a,b))
print('|%8s %8s|' %(c,d))
print('|%-8s %-8s|' %(a,b)) 
print('|%-8s %-8s|' %(c,d)) 
 