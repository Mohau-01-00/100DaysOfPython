import os
import spotipy
from dotenv import load_dotenv
load_dotenv()

from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
 
CLIENT_ID_SPOTIFY = os.getenv("YOUR_SPOTIFY_ID")
CLIENT_SECRET_SPOTIFY = os.getenv("YOUR_SECRET")
URL_REDIRECT = "http://example.com"
 
spotify = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY, 
                                      client_secret=CLIENT_SECRET_SPOTIFY, 
                                      redirect_uri=URL_REDIRECT,
                                      scope="playlist-modify-private",
                                      show_dialog=True,
                                      cache_path="token.txt",
                                       username="Mohau"
                                      )
access_token = spotify.get_access_token()

user_id = spotify.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#-------------------------billboard 100-------------------------------------------


with open("billb_100.txt") as file:
    song_file=file.readlines()

song_list=[]
for song in song_file:
    song_list.append(song)

song_names=[s.strip("\n")for s in song_list]






#-----------------------------Spotify---------------------------------------------


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#client id dbba53c8c5d84afe8fb5898b81b7a1b3
#client secret f28b6bb11a834d95af291a45f811ef7d