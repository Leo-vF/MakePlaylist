from Playlist import from_file
import spotipy
from spotipy import client
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
import yaml


def load_conf():
    conf = yaml.full_load(open('config.yaml'))
    return conf.values()


# if more scopes are required append them with a spece between each one
scope = "playlist-modify-private"

username, client_id, client_secret, redirect_uri = load_conf()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               username=username,
                                               client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri))


from_file(sp, username)
