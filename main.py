import discord
from discord.ext import commands
from mcstatus import JavaServer
import os
###################
token = "tokenhere"
###################
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='-', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def server(ctx, arg2, arg1):
    serverjava = JavaServer.lookup(arg1)
    print("[COMMAND] | $server execution ")
    if arg2 == "status":
        status = serverjava.status()
        await ctx.send(f"> **Server {arg1}** \n> \n> Player: \n> {status.players.online}/{status.players.max} \n> Ping: \n> {status.latency.__round__(1)} ms\n> MOTD: \n> ``{status.motd.raw.get('text')}`` \n> Version: \n> {status.version.name} protocol\n> Protocol ({status.version.protocol})")
        print("status")

@client.command()
async def iplookup(ctx, arg1):
    await ctx.send(os.system([f"curl https://ipapi.co/{arg1}/json/"])

@client.command()
async def ping(ctx):
    print("[COMMAND] | $ping")
    await ctx.send("pong!")

client.run(token)
