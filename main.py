import discord
import os
from discord.ext import tasks
import time
import logging

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# intents = discord.Intents.all()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN=''

@client.event
async def on_message(message):
    logging.info(f'{message.author}: {message.content}')
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello stranger!")

    if message.content.startswith('$private'):
        await message.channel.send("Hello00000")

# @client.event
# async def on_member_join(member):
#     logging.info(f'{member} joined the server')
#
# @client.event
# async def on_member_remove(member):
#     logging.info(f'{member} left the server')

@client.event
async def on_guild_join(guild):
    logging.info(f'Joined server: {guild.id}')

    channels = guild.text_channels
    voice_channels = guild.voice_channels

    channel = client.get_guild(guild.id).get_channel(channels[0].id)
    await channel.send("hey, guys!")

    channel_voice = client.get_guild(guild.id).get_channel(voice_channels[0].id)
    voice = await channel_voice.connect()
    voice.play(discord.FFmpegPCMAudio("C:/Users/dorin/Downloads/sample.mp3"))

@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user}')

    # while voice.is_playing():
    #     time.sleep(.1)
    # await voice.disconnect()

    # await myLoop.start()

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    await client.wait_until_ready()
    channel = client.get_guild(998234966284582942).get_channel(998234966284582945)
    await channel.send(time.time())


client.run(TOKEN)
