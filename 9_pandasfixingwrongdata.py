import pandas as pd
jobayer=pd.read_csv('data.csv')
print(jobayer.to_string())

jobayer.loc[7,'Duration']=45
print(jobayer.to_string())

jobayer=pd.read_csv('data.csv')
print(jobayer.to_string())

for i in jobayer.index:
    if jobayer.loc[i,'Duration']>120:
        jobayer.loc[i,'Duration']=120

print(jobayer.to_string())  

jobayer=pd.read_csv('data.csv')
print(jobayer.to_string())

for i in jobayer.index:
    if jobayer.loc[i,'Duration']>120:
        jobayer.drop(i,inplace=True)

print(jobayer.to_string()) 

