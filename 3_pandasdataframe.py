import pandas as pd
sharad={"cal":[1,2,6],"duration":[4,5,9]}
sharadnew=pd.DataFrame(sharad,index=['d1','d2','d3'])
print(sharadnew)
print(sharadnew.loc['d1'])
print(sharadnew.loc[['d1','d2']])

