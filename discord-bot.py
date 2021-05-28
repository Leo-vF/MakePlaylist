import discord
from os import getenv
from discord import user
from dotenv import load_dotenv
from main import setup
from Playlist import from_dcbot, get_avg_analysis

client = discord.Client()
load_dotenv()
token = getenv("DISCORD_BOT_TOKEN")
correct_user = int(getenv("MY_USER_ID"))
other_users = getenv("USERS").split(",")


@client.event
async def on_message(message: discord.message):
    if message.author == client.user:
        return
    # print(message)
    # print(message.channel)
    # print(message.channel.id)

    print(message.author.id)

    if message.author.id == correct_user:
        response = handle_commands_full(message.content)
        await message.channel.send(response)
    elif str(message.author.id) in other_users:
        print(message.author)
        response = handle_commands(message.content, message.author)
        await message.channel.send(response)


def handle_commands_full(message: str) -> str:
    parts = message.splitlines()
    _idx = parts[0].find(" ")
    cmd = parts[0][:_idx].strip()
    playlist = parts[0][_idx:].strip()
    songs = parts[1:]

    username, sp = setup()

    if cmd == "add":
        return from_dcbot(sp, username, playlist, songs)
    elif cmd == "features":
        return str(get_avg_analysis(sp, username, playlist))
    else:
        return "Error the commmand you specified does not exist."


def handle_commands(message: str, playlist: str) -> str:
    playlist = str(playlist)

    parts = message.splitlines()
    cmd = parts[0]
    songs = parts[1:]

    username, sp = setup()

    if cmd == "add":
        print(playlist, songs)
        return from_dcbot(sp, username, str(playlist), songs)
    elif cmd == "features":
        return str(get_avg_analysis(sp, username, playlist))
    elif cmd == "songs":
        return str()
    else:
        return "Error the command you specified does not exist."


client.run(token)
