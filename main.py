import discord
import os
from discord.ext import tasks
import time

from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

TOKEN='XX'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello stranger!")

    if message.content.startswith('$private'):
        await message.channel.send("Hello00000")

@client.event
async def on_ready():
    print("Bot connected to the server!")
    channel = client.get_guild(998234966284582942).get_channel(998234966284582945)
    await channel.send("hey, guys!")
    await myLoop.start()

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    await client.wait_until_ready()
    channel = client.get_guild(998234966284582942).get_channel(998234966284582945)
    await channel.send(time.time())


client.run(TOKEN)
