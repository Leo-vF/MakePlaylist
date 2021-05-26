import discord
from os import getenv
from discord import player
from dotenv import load_dotenv
from main import setup
from Playlist import from_dcbot, get_avg_analysis

client = discord.Client()
load_dotenv()
token = getenv("DISCORD_BOT_TOKEN")
correct_channel_id = int(getenv("MY_CHANNEL_ID"))


@client.event
async def on_message(message: discord.message):
    if message.author == client.user:
        return
    # print(message)
    # print(message.channel)
    # print(message.channel.id)

    if message.channel.id == correct_channel_id:
        response = handle_commands(message.content)
        await message.channel.send(response)


def handle_commands(message: str) -> str:
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


client.run(token)
