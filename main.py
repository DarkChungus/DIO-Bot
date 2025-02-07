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

# Help command
@dioBot.slash_command(name="help", description="A list with the commands of this bot", guild_ids=[serverID])
async def help(interaction: Interaction):
    helpEmbed = discord.Embed(
        title="Commands List",
        description="**/help**: Gives you a list of the commands this bot uses.\n"
                    "**/github**: Link to my creator's GitHub.",
        color=0xff00ff
    )
    helpEmbed.set_thumbnail("https://imgs.search.brave.com/I8XY4HUTbHeuwa_2mPPwXEe_FlSww2AiuF_tv_a9ciE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy81/YTQ2MTQxOGQwOTlh/MmFkMDNmOWM5OTku/cG5n")
    await interaction.response.send_message(embed=helpEmbed)


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
