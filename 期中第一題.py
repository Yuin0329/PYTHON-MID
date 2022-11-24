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
            elif item.find('_')==-1 and len(text)<=20  :
                for n in item: 
                    if n.isupper():
                        item = item.replace(n,"_"+str(n.lower())) 
                        list1+=[item]
                        del list1[:-1]
                        k="".join(map(str,list1))
                        list1.append(k)
                    elif  len(item)>20:                       
                        list1.append('invalid name')
            else: 
                list1.append('')
    print(list1)
    k="\n".join(list1)
    print(k)
snake_and_camel() 


