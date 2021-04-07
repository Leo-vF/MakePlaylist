from json import load
from Playlist import from_file
import spotipy
from spotipy import client
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
import yaml
from dotenv import load_dotenv
from os import getenv


# def load_conf():
#     conf = yaml.full_load(
#         open('D:\Programmieren\Python\MakePlaylist\config.yaml'))
#     return conf.values()


def setup():
    # if more scopes are required append them with a spece between each one
    load_dotenv()
    scope = "playlist-modify-private"

    # username, client_id, client_secret, redirect_uri = load_conf()

    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
    #                                                username=username,
    #                                                client_id=client_id,
    #                                                client_secret=client_secret,
    #                                                redirect_uri=redirect_uri))
    # return username, sp
    username = getenv("SPOTIPY_USERNAME")
    print(username)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return username, sp


if __name__ == "__main__":
    username, sp = setup()
    sp = setup()
    from_file(sp, username)
