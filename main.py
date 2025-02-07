import discord
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = commands.Bot(command_prefix='!', intents=intents)
botToken = 'token'

localTime = time.localtime()

@client.event
async def on_ready():
    print("------------------------")
    print("!!!!!!BOT IS READY!!!!!!")
    print("------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am godchunguus' bot.")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def time(ctx):
    await ctx.send("Feature in development")

client.run(botToken)
