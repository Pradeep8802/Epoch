#DEDUPLICATION OF THE DATASET:


import pandas as pd
def there(x,i,j):
    l=len(x)
    l1=len(x[1])
    c=0
    for k in range(l):
        if(abs(x[k][i] - x[k][j])<=10**-9):
            c=c+1
    if(c==l):
        return 1
    else:
        return 0 

dataset=pd.read_csv("data.csv")
a=dataset.iloc[:,:17].values    
x=[]
for i in range(17):
    v=[] 
    for j in range(0,1599):
        v.append(a[j][i])
    x.append(v)

l=len(x)#17
l1=len(x[1])#1599
y=[]
for i in range(l1):
    y.append(0)   
rep=0
for i in range(l1):
    if(y[i]==0):
        for j in range(i+1,l1):
            if(there(x,i,j)==1):
                    
                    y[i]=1
                    y[j]=1
                    rep=rep+1
print(rep)   
