import pandas as pd
jobayer=pd.read_csv('data.csv')
print(jobayer.to_string())

jobayernew=jobayer.dropna()
print(jobayernew.to_string())

jobayer["Calories"].fillna(130,inplace=True)
print(jobayer.to_string())



jo1=jobayer.fillna(130)
print(jo1.to_string())



x=jobayer['Calories'].mean()
jo3=jobayer['Calories'].fillna(x)
print(jo3.to_string())

x1=jobayer['Calories'].median()
jo4=jobayer['Calories'].fillna(x1)
print(jo4.to_string())

x2=jobayer['Calories'].mode()[0]
jo5=jobayer['Calories'].fillna(x2)
print(jo5.to_string())

