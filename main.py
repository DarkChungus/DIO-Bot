import discord
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = commands.Bot(command_prefix='!', intents=intents)
botToken = 'token'

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
async def timer10(ctx):
    time.sleep(10)
    await ctx.send("Timer is up!")

@client.command()
async def counttoten(ctx):
    for i in range(1, 11):
        time.sleep(1)
        await ctx.send(i)

client.run(botToken)
