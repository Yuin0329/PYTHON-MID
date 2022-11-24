# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 02:18:51 2022

@author: Yuin
"""
n=int(input("input a num between 2 and 1000："))
if n==1 or n==0 or n>1000:
    print("Error")
else:
    print("{} = ".format(n),end=' ')
    while n>1 :
        for i in range(2,n+1):
            if n%i==0:
                n=int(n/i)
                if n==1:
                    print(i)
                else:
                    print("{} *".format(i),end=' ')
                    break

