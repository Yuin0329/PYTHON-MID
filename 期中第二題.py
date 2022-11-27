# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:22:44 2022

@author: jayyu
"""

import sys
list0=[]
k=input().split()
list0=k
for item in list0:
    if len(item)>=8:
        sys.exit("請重新輸入，資料長度超過長度")
    if item.isnumeric()==True:
        eval(item) 
print('|%8s %8s|' %(list0[0],list0[1]))
print('|%8s %8s|' %(list0[2],list0[3]))
print('|%-8s %-8s|' %(list0[0],list0[1]))
print('|%-8s %-8s|' %(list0[2],list0[3]))
