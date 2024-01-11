import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


url="https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

movie_name=[]
year=[]
time=[]
rating=[]
metascore=[]
votes=[]
gross=[]

moive_data=soup.findAll('div',attrs={'class':'lister-item mode-advanced'})
for store in moive_data:
    name=store.h3.a.text
    movie_name.append(name)
    
    year_of_release=store.h3.find('span',class_="lister-item-year text-muted unbold").text.replace('(','').replace(')','')
    year.append(year_of_release)
    
    runtime=store.p.find('span',class_='runtime').text
    time.append(runtime)
    
    rate=store.find('div',class_="inline-block ratings-imdb-rating").text.replace('\n','')
    rating.append(rate)
    
    '''meta=store.find('span',class_='metascore  favorable').text if store.find('span' ,class_='metascore  favorable') else 0
    metascore.append(meta)'''
    
    values=store.find_all('span',attrs={'name':'nv'})
    vote=values[0].text 
    votes.append(vote)
    
    grosses=values[1].text if len(values) > 1 else '^^^'
    gross.append(grosses)
    
movie_DF=pd.DataFrame({'Name of movie':movie_name, 'Year of release':year, 'Watch_time':time,'Movies rating':rating, 'Votes':votes, 'Grosses':gross})  
    
print(movie_DF.head(50))
movie_DF.to_csv('movie.csv', index=False, header=True)






    



   





