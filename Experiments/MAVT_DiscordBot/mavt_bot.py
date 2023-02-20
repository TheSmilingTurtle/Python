import discord
import json

TOKEN = ""
PREFIX = '$'

PATH_TO_JSON = "./reaction_messages.json"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready(): 
    print("Connected")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith(PREFIX) and message.author.get_role(884151381416615947) is not None:
        split_message = message.content.split(" ")
        
        if split_message[0] == PREFIX + "add_role_message":
                    
            try:
                message_id = int(split_message[1])
            except:
                await message.channel.send("Please pass a message id.")
                return

            try:
                role_id = int(split_message[2][3:-1])
            except:
                await message.channel.send("Please pass a role.")
                return 
                                    
            def check(reaction, user):
                return user.id == message.author.id

            reaction, _ = await client.wait_for("reaction_add", timeout=200, check=check)

            if reaction is not None:

                with open(PATH_TO_JSON, "r") as file:
                    message_list = json.loads(file)

                for message in message_list:
                    if message["id"] == message_id and message["reaction"] == reaction.emoji:
                        return

                message_list['Messages'].append({ 
                    'id': message_id,    
                    'role_id': role_id,  
                    'reaction': reaction.emoji
                })

                with open(PATH_TO_JSON, "w") as file:
                    file.write(json.dumps(message_list, indent = 4))
        
            else:
                await message.channel.send("Reaction Message could not be added.")
                return
        
            await message.channel.send(f"Message { message_id } has been added.")
            return

        if split_message[0] == PREFIX + "remove_role_message":
            
            try:
                message_id = int(split_message[1])
            except:
                await message.channel.send("Please pass a message id.")
                return

            try:
                role_id = split_message[2][3:-1]
            except:
                role_id = None

            flag = False

            for m in message_list['Messages']:
                if m['id'] == message_id:
                    if role_id is None or role_id == m['role_id']:
                        message_list['Messages'].remove(m)
                        flag = True
            
            if flag:
                with open(PATH_TO_JSON, "w") as file:
                    file.write(json.dumps(message_list, indent = 4))

                if role_id == None:
                    await message.channel.send(f"Message { message_id } has been removed.")
                else:
                    await message.channel.send(f"Role <@&{ role_id }> has been removed from message { message_id }.")

            
            await message.channel.send(f"Message could not be removed.")
            return

        if split_message[0] == PREFIX + "list_role_messages":
            with open(PATH_TO_JSON, "r") as file:
                await message.channel.send(f"""```json
{ file.read() }```""")
        
        if split_message[0] == PREFIX + "help":
            await message.channel.send(f"""The prefix is currently set to: { PREFIX }

**The following commands are available:**
```{ PREFIX }add_role_message message_id role```
```{ PREFIX }remove_role_message message_id [optional: role]```
```{ PREFIX }list_role_messages```
```{ PREFIX }help```
If you have any questions, ask TheSmilingTurtle.""")

@client.event
async def on_raw_reaction_add(payload):

    with open(PATH_TO_JSON, "r") as file:
        message_list = json.loads(file)

    for message in message_list['Messages']:
        if message['id'] == payload.message_id and payload.emoji.name == message['reaction']:
            guild = await client.fetch_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = guild.get_role(message['role_id'])
            await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):

    with open(PATH_TO_JSON, "r") as file:
        message_list = json.loads(file)

    for message in message_list['Messages']:
        if message['id'] == payload.message_id and payload.emoji.name == message['reaction']:
            guild = await client.fetch_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = guild.get_role(message['role_id'])
            await member.remove_roles(role)

client.run(TOKEN)
