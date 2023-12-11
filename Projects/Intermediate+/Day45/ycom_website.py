from bs4 import BeautifulSoup
import pandas as pd
import requests

response=requests.get("https://news.ycombinator.com/")
soup=BeautifulSoup(response.text,"html.parser")

# print(soup.title)



score=[int(score_text.getText().split()[0]) for score_text in soup.find_all(class_="score")]
print(score)

news_title=soup.find_all(class_="titleline")
text=[heading.find(name="a").getText() for heading in news_title]
print(text)

article=[heading.find(name="a").get("href") for heading in news_title]
print(article)

df=pd.DataFrame({"Text":pd.Series(text),"Article":pd.Series(article),"Score":pd.Series(score)})
df=df.sort_values(by='Score',ascending=False)

print(df)





# largest_number=max(score)
# print(largest_number)
# largest_index=score.index(largest_number)

# print(article[largest_index])
# print(text[largest_index])







    




# soup=BeautifulSoup(yc_web_page,"html.parser")
# print(soup.title)

