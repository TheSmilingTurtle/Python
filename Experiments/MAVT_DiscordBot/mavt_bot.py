import discord 
import pprint

TOKEN = "MTAxOTg5OTIwMjg3ODMyODg0Mw.GndPQo.VdaNphhyMCSBxWUjPEUCXrveI7jJBmwX5-aNV4"

client = discord.Client()

@client.event
async def on_ready(): 
    print("Connected")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_raw_reaction_add(payload):
    for message in json['Messages']:
        if message['id'] == payload.message_id and payload.emoji.name == message['reaction']:
            role = discord.utils.get(payload.member.guild.roles, name=message['role'])
            await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    pass

json = {
    'Messages': [{
        'id': 1019904334751871006,
        'reaction': "👍",
        'role': "fabu special",
        }
    ]
}

client.run(TOKEN)