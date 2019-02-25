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

tempdf = pd.DataFrame()
for i,row in sym.iterrows():
    res = re.search('[Hh]eadache',row['symptom'])
    if res:
        tempdf = tempdf.append(row)
newdf = pd.DataFrame()
for i,row in tempdf.iterrows():
    newdf = newdf.append(df[df['symptom id']==row['symptom id']])
tempdf = pd.DataFrame()
for i,row in newdf.iterrows():
    tempdf = tempdf.append(dia[dia['diagnosis id']==row['diagnosis id']])
m,t,o,e,f = 0,0,0,0,0
for i,row in tempdf.iterrows():
    res1 = re.search('[Mm]igraine',row['diagnose'])
    res2 = re.search('[Tt]umor',row['diagnose'])
    res3 = re.search('[Ee]ye',row['diagnose'])
    res4 = re.search('[Ff]ever',row['diagnose'])
    res5 = re.search('[Ii]nfluenza',row['diagnose'])
    res6 = re.search('[Ii]nfection',row['diagnose'])
    if res1:
        m+=1
    elif res2:
        t+=1
    elif res3:
        e+=1
    elif res4 or res5 or res6:
        f+=1
    else:
        o+=1
ser = pd.Series({'Migraine': m,'Tumor': t,'Eye Problems':e,\
                 'Fever,Influenza and other infections':f, 'Others': o})
ser.plot(kind = 'pie',autopct = '%0.2f%%')