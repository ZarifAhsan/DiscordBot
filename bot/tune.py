import discord
from discord.ext import commands
import youtube_dl


class tune():
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(music.client)