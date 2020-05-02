import sys
import spotipy
import yaml
import spotipy.util as util


def load_config():
    global user_config
    stream = open('config.yaml')
    user_config = yaml.load(stream)
    print(user_config)


def make_list_from_string(split_character):
    global timestamp
    raw_lines = open("Songs.txt", "r").readlines()
    lines = []
    for i, line in enumerate(raw_lines):
        if line != "\n":
            lines.append(line[:-1])
    for i, line in enumerate(lines):
        lines[i] = line.split(split_character)
        if timestamp == "y":
            lines[i] = lines[i][:-1]
    return lines


def query_spotify(artist, track_name):
    return sp.search(q="{} {}".format(artist, track_name), type='track', limit=1)


def get_track_ids(separation_symbol):
    tracks = make_list_from_string(separation_symbol)
    track_ids = []
    for i in range(len(tracks)):
        track_id = query_spotify(tracks[i][0], tracks[i][1])
        try:
            track_id = track_id['tracks']['items'][0]['id']
            track_ids.append(track_id)
        except:
            pass
    return track_ids


def make_playlist(separation_symbol):
    global playlist_id
    tracks = get_track_ids(separation_symbol)
    sp.user_playlist_add_tracks(
        user=user_config['username'], playlist_id=playlist_id, tracks=tracks)


if __name__ == '__main__':
    global sp
    global user_config
    global playlist_id
    global timestamp
    load_config()
    token = util.prompt_for_user_token(user_config['username'],
                                       scope='playlist-modify-private',
                                       client_id=user_config['client_id'],
                                       client_secret=user_config['client_secret'],
                                       redirect_uri=user_config['redirect_uri'])
    if token:
        sp = spotipy.Spotify(auth=token)
        print("------ ! DO NOT FOGET TO UPDATE THE Songs.txt FILE BEFORE ENTERING THE PLAYLIST NAME! ------")
        separation_symbol = input(
            "Write the Separtion Symbol(s) between Artist and Name in a given line: ")
        print(separation_symbol)
        name = input("Name your new Playlist: ")
        print(name)
        timestamp = input("is a timestamp given? y/n: ")
        print(timestamp)
        playlist_id = sp.user_playlist_create(
            user=user_config['username'], name=name, public=False)['id']
        make_playlist(separation_symbol)
