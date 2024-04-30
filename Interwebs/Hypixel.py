import requests

info = {}

page = requests.get("https://api.mojang.com/users/profiles/minecraft/superb0ygamer")

print(page.content.decode("UTF-8"))

text = page.content.decode("UTF-8")[1:-1].replace('"',"").split(",")

for i in text:
    sequence = i.split(":")
    info[sequence[0]] = sequence[1]

print(info)