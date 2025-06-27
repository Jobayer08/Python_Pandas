import pandas as pd
sharad=[1,2,3]
sharadmew=pd.Series(sharad)
print(sharadmew)
print(sharadmew[1])
sharadmew=pd.Series(sharad,index=['a','b','c'])
print(sharadmew['a'])

cal={"d1":23,"d2":45}
sharadnew=pd.Series(cal)
print(sharadnew)
result=pd.Series(cal,index=['d1'])
print(result)

