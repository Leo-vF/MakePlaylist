from spotipy.client import Spotify
from Song import Song


class Playlist:
    def __init__(self, sp: Spotify, name: str, username: str) -> None:
        self.sp = sp
        self.name = name
        self.username = username
        self.songs = []
        self.id = ""
        self.features = []
        self.avg_features = {}

        self.sp_get_playlist_id()

    def sp_create_playlist(self):
        self.id = self.sp.user_playlist_create(
            self.username, self.name, public=False)['id']

    def sp_get_playlist_id(self):
        response = self.sp.current_user_playlists()
        exists = False
        for item in response["items"]:
            if item["name"] == self.name:
                self.id = item["id"]
                exists = True
                break
        if not exists:
            self.sp_create_playlist()

    def sp_add_songs_to_playlist(self):
        song_ids = [song.id for song in self.songs]
        self.sp.playlist_add_items(self.id, song_ids)

    def sp_get_features(self):
        song_ids = [song.id for song in self.songs]
        self.features = self.sp.audio_features(song_ids)
        unwanted_features = ["type", "id", "uri", "track_href", "analysis_url"]
        for feature in self.features:
            for unwanted_feature in unwanted_features:
                feature.pop(unwanted_feature)

    def add_songs(self, search_names):
        """Adds multiples Songs based on searchname

        Args:
            search_names (list[str]): The search_name for every song to be added
        """
        for search_name in search_names:
            self.songs.append(Song(self.sp, search_name))
        self.sp_add_songs_to_playlist()

    def avg_danceability(self):
        danceabilities = [feature["danceability"] for feature in self.features]
        avg_danceability = sum(danceabilities)/len(danceabilities)
        self.avg_features["danceability"] = avg_danceability

    def avg_features(self):
        for key in self.features[0].keys():
            features = [feature[key] for feature in self.features]
            avg_feature = sum(features)/len(features)
            self.avg_features[key] = avg_feature


def from_file(sp, username, path="Songs.txt"):
    lines = open(path, "r", encoding="utf-8").readlines()
    lines = [line[:-1] for line in lines if line != "\n"]
    #
    # Remove timestamps from lines
    #
    playlist_name = lines[0]
    playlist = Playlist(sp, playlist_name, username)
    playlist.add_songs(lines[1:])
