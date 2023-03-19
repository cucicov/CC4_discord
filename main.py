import discord
import os

from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

TOKEN='MTA4Njk3NTQ4MjMyMDM5NjI5OQ.GVVczL.g7RNMT1akcx6TXKwiNGWHFGKGOX0ZlYlf-fa9c'

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

client.run(TOKEN)
