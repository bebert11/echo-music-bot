import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='&', intents = discord.Intents.all())


for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODkxMzcwODI4NTA2MjI2Nzk5.YU9Xxg.AszKPGx6Rv5sZTqW_KEqxpTCxXM")
