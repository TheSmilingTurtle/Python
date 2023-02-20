import discord 

TOKEN = ""

client = discord.Client(intents=discord.Intents.all())

desired_roles = {
    1017142654737326170,
    1016368292442677380,
    1016356214197731379,
    1021740813442629642,
    1072450271336202280
}

New_User_Role_ID = 1059806699789221928

Guild_ID = 884139481911918603

@client.event
async def on_ready():
    print("Connected")

@client.event
async def on_member_update(_, after):
    role_ids = {x.id for x in after.roles}

    role = client.get_guild(Guild_ID).get_role(New_User_Role_ID)

    if not role_ids.intersection(desired_roles):
        if New_User_Role_ID not in role_ids:
            await after.add_roles(role)
            print(f"{after.name} was given the New User role.")
        else:
            print(f"{after.name} already has the New User role.")
    else:
        if New_User_Role_ID in role_ids:
            await after.remove_roles(role)
            print(f"{after.name} had the New User role removed.")
        else:
            print(f"{after.name} is already missing the New User role.")

client.run(TOKEN)