# Functionality

## Adding Songs

Through the CLI and the optional Discord Bot mutliple Songs can be added to a Spotify playlist specified by it's name. If no Playlist with the specified name exists yet one will automatically be created. To find the Songs on Spotify the Text entered will be used with Spotify's Search API and the first result picked and added.

## Retrieving Audio Features

Through the CLI and the optional Discord Bot the Audio Features for a Playlist will be retrieved. For every Song the Audio Features will be requested on Spotify's API and averaged out over all Songs in the Playlist.

## Setup

### You will need to add a .env file containing

- SPOTIPY_USERNAME: "Your Spotify Username"
- SPOTIPY_CLIENT_ID: "your Spotify client_id"
- SPOTIPY_CLIENT_SECRET: "your Spotify client_secret"
- SPOTIPY_REDIRECT_URI: "a redirection url (e.g. 'https://localhost:8080')"

#### Optional

When using a discord bot you can text the bot the bot the name of the playlist as well as all the songs to be added. It will automatically create a Playlist if the name specified is not yet a Playlist.

- DISCORD_BOT_TOKEN: "the token for the discord bot"
- MY_USER_ID: "Your own Discord user id"
- USERS: "The Discord id's of allowed users"

### Ease of use

- doskey for easier access: `doskey sp=py D:\Programmieren\Python\MakePlaylist\cli.py $\*`
  or

- a .bat file containing `@echo off py D:\Programmieren\Python\MakePlaylist\cli.py %*`
