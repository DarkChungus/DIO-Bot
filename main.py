import discord
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = commands.Bot(command_prefix='!', intents=intents)
botToken = 'MTMzNzIzNDYxMjAzNjA0Mjc2Mg.GNARI6.1xgqNtR7p4R8XICuJhMLjNDXIg3aLErQx3dSZw'

localTime = time.localtime()

@client.event
async def on_ready():
    print("The bot is ready to use!")
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
