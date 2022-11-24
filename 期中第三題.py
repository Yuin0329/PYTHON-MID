# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 03:10:28 2022

@author: Yuin
"""

def splitString(str):
 if len(text)>=8 and len(text)<=20:
    upper = ""
    lower = ""
    num = ""
    special = ""
    for i in range(len(str)):
        if (str[i].isdigit()):
            num = num+ str[i]
            
        elif(str[i] >= 'A' and str[i] <= 'Z'):
            upper += str[i]
            if upper.isspace():
                break
        elif(str[i] >= 'a' and str[i] <= 'z'):
            lower += str[i]
            if lower.isspace():
                break
        else:
            special += str[i] 
    if num.isspace()==True or upper.isspace()==True or lower.isspace()==True or len(special)>0:
        print("Invalid	password")
    elif num.isnumeric()==True and len(upper)>0 and len(lower)>0 and len(special)==0:
        print("Valid password")
    else:
        print("Invalid	password")
    #print(upper)
    #print(lower)
    #print(num)
    #print(special)
 else:
      print("Invalid password") 
      
text=input(str())
splitString(text)
