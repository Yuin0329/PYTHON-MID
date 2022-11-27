# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 01:02:38 2022

@author: Yuin
"""

import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv('Giannis Antetokounmpo.csv',encoding='big5')
df2=pd.read_csv('KevinDurant.csv',encoding='big5')
df3=pd.read_csv('LukaDoncic.csv',encoding='big5')
df4=pd.read_csv('NikolaJokic.csv',encoding='big5')
df5=pd.read_csv('StephenCurry.csv',encoding='big5')

def player_eff(n):
    avg=0
    avg2=0
    end=len(n)
    
    for i in range(1, end):
        avg +=(n.iloc[i,29] +n.iloc[i,23] +n.iloc[i,24] +n.iloc[i,25] +n.iloc[i,26] ) *n.iloc[i,5]
        avg2 +=(n.iloc[i,9] - n.iloc[i,8] +n.iloc[i,19] - n.iloc[i,18] +n.iloc[i,26] ) *n.iloc[i,5]
   
    return (avg - avg2) / sum(n["G"])


values = []
values.append(player_eff(df1))
values.append(player_eff(df2))
values.append(player_eff(df3))
values.append(player_eff(df4))
values.append(player_eff(df5))
    
item = [sum(df1["3P%"])/len(df1),sum(df2["3P%"])/len(df2),sum(df3["3P%"])/len(df3),sum(df4["3P%"])/len(df4),sum(df5["3P%"])/len(df5),]
plt.xlabel("Values")
plt.ylabel("3P%")

plt.scatter(values[0], item[0], c = "m",marker = "o", label= "Giannis Antetokounmpo")
plt.scatter(values[1], item[1], c = "y",marker = "X", label= "KevinDurant")
plt.scatter(values[2], item[2], c = "r",marker = "s", label= "LukaDoncic")
plt.scatter(values[3], item[3], c = "g",marker = "<", label= "NikolaJokic")
plt.scatter(values[4], item[4], c = "b",marker = ">", label= "StephenCurry")
plt.legend() 