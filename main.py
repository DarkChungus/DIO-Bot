# Importing all the required libraries

import discord
from discord.ext import commands
import time
import random
from botToken import *

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
dioBot = commands.Bot(command_prefix="dio, ", intents=intents)

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

# Time Stop GIF
@dioBot.command()
async def THEWORLD(ctx):
    await ctx.send("https://tenor.com/view/za-warudo-the-world-dio-brando-stand-joseph-joestar-gif-26463002")

# Random number generator from 1 to 100
@dioBot.command()
async def random(ctx):
    randomNumber = random.randint(1, 101)
    strRandom = str(randomNumber)
    await ctx.send("The random number from 1 to 100 is "+strRandom+".")

# My GitHub promotion using an embed
@dioBot.command()
async def github(ctx):
    githubEmbed = discord.Embed(
                                title="My Github",
                                url="https://github.com/DarkChungus",
                                description="This bot is a project by Prakrit Gajurel(godchunguus). Please support me on GitHub by starring any of my repositories that can be helpful to you!",
                                color=0x33ccff
                                )
    await ctx.send(embed=githubEmbed)

# Run the bot
dioBot.run(botToken)
