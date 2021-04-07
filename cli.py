import click
from main import setup
from Playlist import from_file, from_cli


@click.command("add")
@click.option("--file", "-f", help="Path to file from local dir")
@click.option("--playlist-name", "-p", help="The Playlists name")
@click.option("--songs", "-s", help="The Songs to be added")
def file(file, playlist_name, songs):
    username, sp = setup()
    if file and playlist_name:
        from_file(sp, username, path=file, playlist_name=playlist_name)
    elif file:
        from_file(sp, username, path=file)
    elif playlist_name and songs:
        from_cli(sp, username, playlist_name, songs)


if __name__ == "__main__":
    file()
