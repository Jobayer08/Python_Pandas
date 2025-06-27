import pandas as pd
fileload=pd.read_csv('EmbeddedNuls.csv')
print(fileload.to_string())
print(fileload)

print(pd.options.display.max_rows)

pd.options.display.max_rows=9999
