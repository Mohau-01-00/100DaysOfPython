from bs4 import BeautifulSoup
import pandas as pd
import requests
import re


response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup=BeautifulSoup(response.text,"html.parser")

#get all the titles in the class titles
titles=soup.find_all(name="h3",class_="title")

#get all the text in the class title 
movie_title=[title.getText() for title in titles]


numbers=[num.split(")")[0] for num in movie_title]


df=pd.DataFrame({"Movie Title":pd.Series(movie_title),"Ranking":pd.Series(numbers)})
df=df.sort_values(by='Ranking')
df.loc[88, 'Ranking'] = "12"


print(df)



print(movie_title)
print(numbers)





