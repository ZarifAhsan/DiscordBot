import discord
from discord.ext import commands
import tune

cogs = [tune]

client = commands.Bot(command_prefix='@', 
intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

    
client.run("ODg5NTkxNDk2MDQ5ODE5NjQ4.YUjepA.lSQ1C8Dw4t2NEHDsy2cBDPARhyM") # Add your discord bot code (The one here is fake :P)
