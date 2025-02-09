# Importing all the required libraries

import discord
from discord.ext import commands
import nextcord
from nextcord import Interaction
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
                    "**/github**: Link to my creator's GitHub.\n"
                    "**/magic8ball**: Ask any question to the Magic 8 Ball! Not to be taken seriously.\n"
                    "**/ship**: Ship any two users!\n"
                    "**/flip**: Flip a coin!",
        color=0xff00ff
    )
    helpEmbed.set_thumbnail("https://imgs.search.brave.com/I8XY4HUTbHeuwa_2mPPwXEe_FlSww2AiuF_tv_a9ciE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy81/YTQ2MTQxOGQwOTlh/MmFkMDNmOWM5OTku/cG5n")
    await interaction.response.send_message(embed=helpEmbed)

# Time Stop GIF
@dioBot.event
async def on_message(message):
    if message.content.lower() == 'dio, the world':
        await message.channel.send('https://tenor.com/view/za-warudo-the-world-dio-brando-stand-joseph-joestar-gif-26463002')

# DIO Introduces himself
@dioBot.slash_command(name="introduction", description="Get an idea of who I am", guild_ids=[serverID])
async def introduction(interaction: Interaction):
    introEmbed = discord.Embed(
        title="DIO's Introduction",
        description="\"He IS PURE EVIL, right down to his very bones! Is he a victim of circumstance, you're wondering? Not on your life! He's been evil since he drew his first breath!\" - Speedwagon\n"
                    "Dio Brando (ディオ・ブランドー Dio Burandō), known as DIO (ディオ) from Part 3 onwards, is the main antagonist in the original universe of JoJo's Bizarre Adventure, featured primarily as the main antagonist in Phantom Blood and Stardust Crusaders, and a posthumous key antagonist in Stone Ocean.",
        color=0xff3300
    )
    introEmbed.set_thumbnail("https://static.wikia.nocookie.net/jjba/images/7/70/Shadow_DIO_Anime.png/revision/latest?cb=20181121204550")
    await interaction.channel.send(embed=introEmbed)

# Simple Greetings
@dioBot.slash_command(name="greet", description="DIO greets anyone!", guild_ids=[serverID])
async def greet(interaction: Interaction, name: str):
    greetEmbed = discord.Embed(
        title="Greetings",
        description="Hey there, "+name+"!",
        color=0x66ccff
    )
    greetEmbed.set_thumbnail("https://imgs.search.brave.com/hLEWH7ANevxmkdok015gZLTkiRittw42-heWrhN0wnM/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMtMDAuaWNvbmR1/Y2suY29tL2Fzc2V0/cy4wMC93YXZpbmct/aGFuZC1lbW9qaS0y/NTB4MjU2LXJtc3Nq/eDEzLnBuZw")
    await interaction.channel.send(embed=greetEmbed)

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

# Magic 8Ball
@dioBot.slash_command(name="magic8ball", description="Ask the Magic 8Ball any question!", guild_ids=[serverID])
async def magic8ball(interaction: Interaction, message: str):
    ballAnswers = ['yes', 'i dont know', 'no', 'maybe', 'i do not care', 'why are you trusting this bot?']
    ballRandom = random.randint(0, 5)
    ballResponse = ballAnswers[ballRandom]
    userMessage = str(message)
    ballEmbed = discord.Embed(
        title="Magic 8Ball",
        description="**Question**:\n"+userMessage+"\n"
                    "**Answer**:\n"+ballResponse,
        color=0x4000ff
    )
    ballEmbed.set_thumbnail("https://imgs.search.brave.com/WaQzsF00WAsav4erjtbCsCM3eQ05-_p15O3tT4oQNPI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJzLmNvbS9p/bWFnZXMvaGQvOC1i/YWxsLXBvb2wtZ2Ft/ZS1iYWxsLW50cDR1/NjNqbDdyYmhvenIu/cG5n")
    await interaction.response.send_message(embed=ballEmbed)

# Shipping Command
@dioBot.slash_command(name="ship", description="Ship any two people using this feature!", guild_ids=[serverID])
async def ship(interaction: Interaction, user1: str, user2: str):
    userOne = str(user1)
    userTwo = str(user2)
    loveChance = random.randint(1, 101)
    if loveChance<20:
        shipReview = "**Oof.. would not ship..**"
    elif loveChance>=20 and loveChance<50:
        shipReview = "**Decent.. still very bad ship..**"
    elif loveChance==50:
        shipReview = "**Honestly, it can go both ways!**"
    elif loveChance>50 and loveChance<69:
        shipReview = "**Wow! A decent ship!**"
    elif loveChance==69:
        shipReview = "**( ͡° ͜ʖ ͡°) noice ( ͡° ͜ʖ ͡°)**"
    elif loveChance>69 and loveChance<80:
        shipReview = "**Wouldn't put my life on it, but it is a good ship!**"
    elif loveChance>=80 and loveChance<100:
        shipReview = "**Wow!!! These people are meant for each other!**"
    elif loveChance==100:
        shipReview = "***THIS IS A PERFECT MATCH! <3 <3 <3***"

    shipEmbed = discord.Embed(
        title="Ship",
        description=userOne+" and "+userTwo+"!!!\nLove Percentage: "+str(loveChance)+"\n"+str(shipReview),
        color=0xff33cc
    )
    shipEmbed.set_thumbnail("https://imgs.search.brave.com/ccznmW8qR0CSyUekQdwAbdhp0tKbp0FQLSEHfQeoODk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL2hlYXJ0cy1w/bmctaGQtZG93bmxv/YWQtcG5nLWltYWdl/LWhlYXJ0LXBuZy1o/ZC0yNDM1LTk5OS5w/bmc")
    await interaction.response.send_message(embed=shipEmbed)

# Coin Flip
@dioBot.slash_command(name="flip", description="Flip a coin", guild_ids=[serverID])
async def flip(interaction: Interaction):
    coinToss = ['heads', 'tails']
    temp = random.randint(0, 1)
    outcome = coinToss[temp]
    if outcome=='heads':
        coinEmbed = discord.Embed(
            title="Coin Toss",
            description="You tossed **heads**!",
            color=0xffff00
        )
    else:
        coinEmbed = discord.Embed(
            title="Coin Toss",
            description="You tossed **tails**!",
            color=0xcc6600
        )
    coinEmbed.set_thumbnail("https://imgs.search.brave.com/YIK6s2rsoLtz6vh0uMvENk5VIM8ZQWgP8u5PjPU4-Kw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wbmcu/cG5ndHJlZS5jb20v/cG5nLWNsaXBhcnQv/MjAyMzA1MjAvb3Vy/bWlkL3BuZ3RyZWUt/ZC1nb2xkLWNvaW4t/ZG9sbGFyLXVzLWN1/cnJlbmN5LW1vbmV5/LWljb24tc2lnbi1v/ci1zeW1ib2wtcG5n/LWltYWdlXzcxMDE3/ODUucG5n")
    await interaction.response.send_message(embed=coinEmbed)

# Run the bot
dioBot.run(botToken)
