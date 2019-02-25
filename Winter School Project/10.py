# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:26:37 2019

@author: SOHAM
"""

import pandas as pd
import math
import re

df = pd.read_csv("diffsydiw.csv")
df = df.fillna(0)
dia = pd.read_csv("dia_t.csv")
sym = pd.read_csv("sym_t.csv")
def change(x):
    grp = df.groupby('did')
    temp = grp.get_group(x)
    m = temp['wei'].mean()
    if m==0:
        return 2
    else:
        return math.ceil(m)
df['wei'] = df.apply(lambda x : change(x['did']) if x['wei']==0 else x['wei']\
  ,axis=1)
df.rename(columns={'wei':'weight','syd':'symptom id','did':'diagnosis id'}\
           ,inplace=True)
sym.rename(columns={'syd':'symptom id'},inplace=True)
dia.rename(columns={'did':'diagnosis id'},inplace=True)
def colu(g):
    if g==1.0:
        s='common'        
        return s

    elif g==2.0:
        s='life-threatening'        
        return s

    elif g==3.0:
        s='common-paediatrics'        
        return s

df['weight']=df['weight'].apply(lambda x:colu(x))
sym['symptom'] = sym.apply(lambda x: x['symptom']\
   if type(x['symptom'])==str else 'unnamed',axis=1)
def repair(i):
    l = i.split('\x0b')
    s = ""
    for j in l:
        s = s+' '+j
    return s
dia['diagnose'] = dia['diagnose'].apply(lambda x: repair(x))

for i,row in dia.iterrows():
    res = re.search('[Aa]ppendicitis',row['diagnose'])
    if res:
        grp = df.groupby('diagnosis id')
        appendicitis = grp.get_group(row['diagnosis id'])
tempdf = pd.DataFrame()
for i,row in appendicitis.iterrows():
    tempdf = tempdf.append(sym[sym['symptom id']==row['symptom id']])
print(tempdf)