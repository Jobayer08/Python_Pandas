import pandas as pd
jobayer=pd.read_csv('data.csv')
print(jobayer.to_string())

jobayer["Date"] = pd.to_datetime(jobayer["Date"],errors='coerce')
print(jobayer.to_string())

jobayer.dropna(subset=['Date'],inplace=True)
print(jobayer.to_string()) 