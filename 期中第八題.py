# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:35:15 2022

@author: Yuin
"""



import pandas as pd
import matplotlib.pyplot as plt

df_2330 = pd.read_csv('2330.TW.csv')

df_2330.set_index(pd.to_datetime(df_2330['Date'],format='%Y-%m-%d'),inplace=True)
df_2330.head()


#Max
df_2330['9DAYMAX'] =df_2330['High'].rolling(window = 9).max()


#Min
df_2330['9DAYMIN'] =df_2330['Low'].rolling(window = 9 ).min()

#RSV
df_2330['RSV'] = 0
df_2330['RSV'] = 100 * (df_2330['Close'] - df_2330['9DAYMIN']) / (df_2330['9DAYMAX'] - df_2330['9DAYMIN'])


#K
K = 0
def KValue(rsv):
    global K
    K = (2/3) * 50 + (1/3) * rsv
    return K
df_2330['K'] = 0
df_2330['K'] = df_2330['RSV'].apply(KValue)

D = 0
def DValue(k):
    global D
    D = (2/3) * 50 + (1/3) * k
    return D
df_2330['D'] = 0
df_2330['D'] = df_2330['K'].apply(DValue)


fig,ax=plt.subplots(figsize=(10,5))
ax.plot(df_2330['K'],color='skyblue',label='K')
ax.plot(df_2330['D'],color='red',label='D')
ax.legend(loc='upper right')
plt.grid()
plt.show() 
