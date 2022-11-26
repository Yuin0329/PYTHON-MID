# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 04:43:02 2022

@author: jayyu
"""
import math
def compute(p, q):
    return math.gcd(p, q)
x, y = map(int,input().split("/"))
m, n = map(int,input().split("/"))
p = (x*n + m*y) / compute(x*n + m*y,y*n)
q = (y*n) / compute(x*n + m*y, y*n)
print('%d/%d' %(p, q))
