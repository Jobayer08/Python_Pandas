import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


jobayer=pd.read_csv('apple_products.csv')
print(jobayer.head())
print(jobayer.isnull().sum())
print(jobayer.describe())

highest_rated=jobayer.sort_values(by=['Star Rating'],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])

iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
counts=highest_rated['Number Of Ratings']
figure=px.bar(highest_rated,x=label,y=counts,title='number of rating of highest rated iphone')
figure.show()

iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
counts=highest_rated['Number Of Reviews']
figure=px.bar(highest_rated,x=label,y=counts,title='number of rating of highest rated iphone')
figure.show()

figure =px.scatter(data_frame=jobayer,x='Number Of Ratings',y='Sale Price',size='Discount Percentage',trendline='ols',title='relationship between sale price ')
figure.show()

figure =px.scatter(data_frame=jobayer,x='Number Of Ratings',y='Discount Percentage',size='Sale Price',trendline='ols',title='relationship between sale price ')
figure.show()