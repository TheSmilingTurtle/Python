import numpy as np
import random
import discord
import time

rps_wait = True

rps_vals = ["rock", "paper", "scissors"]

TOKEN = "NjM0NDUxMTUzODkxMDk4NjQ5.XsuMfw.Q64zqERHBbnXyzJZPGJ9MC3HH_A"

client = discord.Client()

def police(msg):
    if len(msg) != 6:
        return False
    if not msg.isupper():
        return False
    for i in msg:
        if i.isdigit():
            return False
    return True

@client.event
async def on_message(msg):
    global rps_wait

    if msg.author == client.user:
        return
    
    print(msg.author, "in", msg.channel, ": ", msg.content)

    if msg.channel == client.get_channel(745691967001985046) and police(msg.content.strip()):
        await client.get_channel(769194239333892116).send(msg.content)
        await msg.delete()
        await msg.channel.send("The game code has been moved to <@!{}>. \n[Insert sassy response.]".format(769194239333892116))

    if "hello" in msg.content.lower() and msg.content.lower().index("hello") == 0:
        await msg.channel.send("no") 

    if "hi" in msg.content.lower() and msg.content.lower().index("hi") == 0:
        await msg.channel.send("Go away")
        return
    
    if msg.content.lower() == "the beautiful people":
        await msg.channel.send("WHAAAAAAAA")
        return

    if "<@!634451153891098649>" in msg.content:
        await msg.channel.send("stop pinging me <@!{}>".format(str(msg.author.id)))
        return
    
    if msg.content == "!rps":
        rps_wait = True
        await msg.channel.send("Okay, i'll count down.")

        t = time.time()
        for i in range(1,4):
            while True:
                if time.time()-t >= 0.2*i:
                    await msg.channel.send(4-i)
                    break
    
        await msg.channel.send("Go!")
        
        return
    
    if rps_wait:
        pick = random.randint(0,2)
        val = -1
        for i in range(3):
            if rps_vals[i] in msg.content:
                val = i
            
        if val >= 0:
            if pick == 0 and val == 2:
                await msg.channel.send("I picked %s \nI win" % rps_vals[pick])
            elif pick == val:
                await msg.channel.send("I picked %s \nIts a tie" % rps_vals[pick])
            elif pick == 2 and val == 0:
                await msg.channel.send("I picked %s \nYou win" % rps_vals[pick])
            elif pick >= val:
                await msg.channel.send("I picked %s \nI win" % rps_vals[pick])
            else:
                await msg.channel.send("I picked %s \nYou win" % rps_vals[pick])
            rps_wait = False
        
        return

    if msg.content:
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