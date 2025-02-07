# Importing all the required libraries

import discord
import nextcord
from nextcord import Interaction
from discord.ext import commands
import time
import random
from botToken import *

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
dioBot = commands.Bot(command_prefix="dio, ", intents=intents)
serverID = 1337236814217478257

# Notifies in console that the bot is running
@dioBot.event
async def on_ready():
    print("--------------------------")
    print(" The bot is ready to use")
    print("--------------------------")

# Simple hello command
@dioBot.command()
async def hello(ctx):
    await ctx.send("Hello there!")

# Ping Pong
@dioBot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Timer for 10 seconds
@dioBot.command()
async def timer(ctx):
    for i in range(1, 11):
        await ctx.send(i)
        time.sleep(1)
    await ctx.send("Your timer for 10 seconds is up!")

# Random number generator from 1 to 100
@dioBot.command()
async def random(ctx):
    randomNumber = random.randint(1, 101)
    strRandom = str(randomNumber)
    await ctx.send("The random number from 1 to 100 is "+strRandom+".")

# Time Stop GIF
@dioBot.event
async def on_message(message):
    if message.content.lower() == 'dio, the world':
        await message.channel.send('https://tenor.com/view/za-warudo-the-world-dio-brando-stand-joseph-joestar-gif-26463002')

# Slash command to my GitHub
@dioBot.slash_command(name="github", description="Link to my GitHub", guild_ids=[serverID])
async def github(interaction: Interaction):
    githubEmbed = discord.Embed(
        title="My Github",
        url="https://github.com/DarkChungus",
        description="This bot is a project by Prakrit Gajurel(godchunguus). Please support me on GitHub by starring any of my repositories that can be helpful to you!",
        color=0x33ccff
    )
    await interaction.response.send_message(embed=githubEmbed)

# Run the bot
dioBot.run(botToken)
