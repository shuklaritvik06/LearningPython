from bs4 import BeautifulSoup
import spotipy
import os
import requests
from spotipy.oauth2 import SpotifyOAuth


date = input("Enter the date in the YYYY-MM-DD format: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text,'html.parser')
all_h3 = soup.select(name="h3",selector="li h3.c-title")
titles = [item.get_text() for item in all_h3]
newslist = []
for a in titles:
    a = a.strip('\n')
    newslist.append(a)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for song in newslist:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist["id"], tracks=song_uris)