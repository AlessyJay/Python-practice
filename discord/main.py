import discord
import os

client = discord.Client()

@client.event
async def on_read():
    print("We're ready! {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author

