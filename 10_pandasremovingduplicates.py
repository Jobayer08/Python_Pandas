import pandas as pd
jobayer=pd.read_csv('data.csv')
print(jobayer.to_string())

print(jobayer.duplicated())

jobayer.drop_duplicates(inplace=True)
print(jobayer.to_string())