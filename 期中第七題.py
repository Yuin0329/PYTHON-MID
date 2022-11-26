# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 03:12:06 2022

@author: jayyu
"""

n,m=map(int,input().split())
k=[[0]*20 for g in range(7)]
list1=[]
for i in range(1,n+1):
    for j in range(0,6):
        k[i][j]=j+1
for x in range(0,m):
    a,b=map(int,input().split())
    if a>0 and b>0:
        for y in range(0,6):
            k[a][y],k[b][y]=k[b][y], k[a][y]
    if b==-1:
            temp=int()
            temp=k[a][0]
            k[a][0]=k[a][2]
            k[a][2]=k[a][5]
            k[a][5]=k[a][3]
            k[a][3]=temp
    if b==-2:
            temp=int()
            temp=k[a][0]
            k[a][0]=k[a][4]
            k[a][4]=k[a][5]
            k[a][5]=k[a][1]
            k[a][1]=temp
for a in range(1,n+1):
       list1.append(k[a][0])       
upper=" ".join(map(str,list1))
print(upper) 