# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:55:51 2022

@author: jayyu 
"""
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
    
a,b=map(int,input().split())
list1=[]
if a!=b :
    if a>b:
        for i in range(b,a):
            if is_prime(i)==True:
                strnum=str(i)
                list1.append(strnum)
        list1.reverse()
        k=" ".join(list1)
        print(k)
    elif b>a:
        for j in range(a,b):
            if is_prime(j)==True:
                strnum=str(j)
                list1.append(strnum)
        k=" ".join(list1)
        print(k)  
