from Playlist import from_file, get_avg_analysis
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from os import getenv


def setup():
    # if more scopes are required append them with a spece between each one
    load_dotenv()
    scope = "playlist-modify-private playlist-read-private"
    username = getenv("SPOTIPY_USERNAME")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return username, sp


if __name__ == "__main__":
    username, sp = setup()
    playlist_name = str(input("Enter the Playlists name: "))
    print(get_avg_analysis(sp, username, playlist_name))
