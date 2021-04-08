from requests.models import Response
from spotipy.client import Spotify


class Song:
    def __init__(self, sp: Spotify, search_name: str = None, id: str = None, name: str = None, artist: str = None) -> None:
        self.sp = sp

        if id and name and artist:
            self.id = id
            self.name = name
            self.artist = artist
            self.search_name = name + " " + artist
        elif id:
            self.id = id

            self.get_spotify_info_by_id()
        elif search_name:
            self.search_name = search_name
            self.name = ""
            self.artist = ""

            self.get_spotify_info()

    def __str__(self) -> str:
        if self.name and self.artist:
            return "{} by {}".format(self.name, self.artist)
        else:
            return self.search_name

    def get_spotify_info(self):
        response = self.sp.search(q=self.search_name, type='track', limit=1)
        # test to see if a song was found or not
        if response["tracks"]["total"] == 0:
            print("Couldn't find {}".format(self.search_name))
        else:
            self.id = response["tracks"]["items"][0]["id"]
            self.name = response["tracks"]["items"][0]["name"]
            self.artist = response["tracks"]["items"][0]["artists"][0]["name"]

    def get_spotify_info_by_id(self):
        response = self.sp.track(self.id)
        self.name = response["name"]
        self.artist = response["artists"][0]["name"]

    def sp_get_features(self):
        self.features = self.sp.audio_features(self.id)[0]

    def get_id(self):
        return self.id
