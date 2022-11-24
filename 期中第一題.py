# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:36:45 2022

@author: Yuin
"""

def snake_and_camel(text):   
    if text.find('_')!=-1 and len(text)<=20:
      a=text.split('_')
      camel = a[0] + ''.join(n.title() for n in a[1:])
      print(camel)
    elif text.find('_')==-1 and len(text)<=20  :
        list1=[]
        for n in text: 
            if n.isupper():
                text = text.replace(n,"_"+str(n.lower())) 
                list1+=[text]
        del list1[:-1]
        k="".join(map(str,list1))
        print(k)
    elif  len(text)>20:
        print('invalid name')
    else:
        print('') 
text=input(str())
snake_and_camel(text) 