from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



CLIENT_ID = "0fb8a5b634854bb1b9a2b3fb3100db41"
CLIENT_SECRET = "064c43e2f2e74debbfdebb93e62787cf"
DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + DATE
response = requests.get(url=url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

list_of_songs = soup.select("li.o-chart-results-list__item h3.c-title")

titles = [title.get_text().strip() for title in list_of_songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31tf2a6nhws5vx3xozzrhxrdouuy",
    )
)
user_id = sp.current_user()["id"]

def get_song_uri(title):
    query = f'track: "{title}" {DATE}'
    result = sp.search(q=query, type="track", limit=1)
    tracks = result.get('tracks', {}).get('items', []) #Understand this!!
    if tracks:
        return tracks[0]["uri"]
    return None

song_uris = [get_song_uri(title) for title in titles]

try:
    playlist = sp.user_playlist_create(
        user=user_id,
        name = f"{DATE} Billboard 100",
        public=False,
        description=f"Top 100 songs on Billboard on {DATE}"
    )
    sp.playlist_add_items(
        playlist_id=playlist["id"],
        items = song_uris
    )

    print(f"Playlist created: {playlist['external_urls']['spotify']}")
except None:
    print("Error occurred, please provide a proper date")