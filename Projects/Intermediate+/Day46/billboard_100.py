from bs4 import BeautifulSoup

import requests


YEAR="2015-01-12"
# input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response=requests.get(f"https://www.billboard.com/charts/hot-100/{YEAR}")
soup=BeautifulSoup(response.text,"html.parser")

song_details=soup.find_all(name="li",class_="lrv-u-width-100p")
# print(song_details)

song_title=[song.find(name="h3") for song in song_details ]
# print(song_title)


song_list=[]
for song in song_title:
    # on the below, we checking all song_title that have element (name="h3") if it doesnt it will return none and you cannot getText()
    if song:
      song_name=song.getText()
      song_list.append(song_name)
     
    else:pass
    

#strip the \t and \n in the song name so only the name appears 
song_name=[s.strip("\n\t")for s in song_list]
print(song_name)
print(len(song_name))

with open("billb_100.txt","w") as file:
   for song in song_name:
      file.write(f"{song}\n")
   