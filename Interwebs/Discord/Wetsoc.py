import numpy as np
import discord
from PIL import Image
import random
import requests

TOKEN = input("Enter Token: ") #can be found at https://discord.com/developers/applications/

if TOKEN == "":
    with open("token.txt", "r") as file:
        TOKEN = file.read()

client = discord.Client()

@client.event
async def on_message(msg):
    print(msg.author, "in", msg.channel, ": ", msg.content)
    
    if msg.author == client.user:
        return

#ultimate annoying and fuck you shutuper
    #if msg.author == client.get_user(593167194230358037):
    #    await msg.delete()

    elif "hello" in msg.content.lower():
        if msg.content.lower().index("hello") == 0:
            await msg.channel.send("no") 

    elif "hi" in msg.content.lower():
        if msg.content.lower().index("hi") == 0:
            await msg.channel.send("Go away")

    elif "the beautiful people" in msg.content.lower():
        if msg.content.lower() == "the beautiful people":
            await msg.channel.send("WHAAAAAAAA")

    elif "<@!634451153891098649>" in msg.content:
        await msg.channel.send("stop pinging me <@!{}>".format(str(msg.author.id)))
        
    elif msg.content != "":
        chance = random.randint(1,40)
        if chance == 1:
            await msg.channel.send("Thats what she said")
        elif chance == 2:
            await msg.channel.send("Title of your sex tape")

@client.event
async def on_ready():
    print('\nLogged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)