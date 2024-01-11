import pandas as pd
data=pd.read_csv("/content/movie (1).csv")
data['Grosses']=data.Grosses.str.replace('$','')
data['Grosses']=data.Grosses.str.replace('#','')
data['Grosses']=data.Grosses.str.replace('M','')
data['Grosses']=data.Grosses.str.replace('111111','127.34')
data['Grosses']=data.Grosses.astype(float)
data['Grosses']=data['Grosses'] * 1000000
data['Grosses'] = data['Grosses'].astype(int)
data
