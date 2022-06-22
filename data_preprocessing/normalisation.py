#NORMALISATION OF DATA
# BRINGING ALL DATA VALUES BEWEEN 0 and 1

import pandas as pd
def min(x):
    for i in range(0,len(x)-1):
        if(x[i]<x[i+1]):
            d=x[i]
            x[i]=x[i+1]
            x[i+1]=d    

    return d

def max(x):
    for i in range(0,len(x)-1):
        if(x[i]>x[i+1]):
            c=x[i]
            x[i]=x[i+1]
            x[i+1]=c    
    return c
def change(x,dif,deno):
    return (x-dif)/deno    

dataset=pd.read_csv("data.csv")
a=dataset.iloc[:,:17].values    
x=[]
for i in range(17):
    v=[] 
    for j in range(0,1599):
        v.append(a[j][i])
    x.append(v)
mn=[]
mx=[]    
for i in range(len(x)):    
    mn.append(min(x[i]))
    mx.append(max(x[i]))
for i in range(len(x)):
    a=mx[i]-mn[i]
    for j in range(len(x[i])):
        x[i][j]=change(x[i][j],mn[i],a)
