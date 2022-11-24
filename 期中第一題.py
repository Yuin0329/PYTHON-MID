# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:36:45 2022

@author: Yuin
"""

def snake_and_camel():
    N=int(input())
    list0=[]
    list1=[]
    for i in range(0,N):
        text=input(str())
        list0+=[text]
    for item in list0:
            if item.find('_')!=-1 and len(item)<=20:
                a=item.split('_')
                camel = a[0] + ''.join(n.title() for n in a[1:])
                list1.append(camel)
            elif item.find('_')==-1 and len(item)<=20  :
                 for n in item: 
                    list2=[]
                    if n.isupper():
                        item = item.replace(n,"_"+str(n.lower())) 
                    list2+=[item]
                 del list2[:-1]
                 k="".join(map(str,list2))
                 list1.append(k)
            else:                       
                list1.append('invalid name')
    k="\n".join(list1)
    print("======以下為輸出======")
    print(k)
    #print(list2)
snake_and_camel()     

 
