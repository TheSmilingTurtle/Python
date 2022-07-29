import time
import spotipy

html = """
<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="style.css">
    <meta http-equiv="refresh" content="1" />
    <meta charset="utf-8">
    <title>Currently Playing</title>
</head>
<body>
    <div id="img-div">
        <img id="img" src="{2}">
    </div>
    <div id="tracks">
        <h1 id="song-title">{0}</h1>
        <h2 id="artist">{1}</h2>
    </div>
</body>"""

with open("client_creds.txt") as file:
    client_id = file.readlines[0]
    client_secret = file.readlines[1]

auth_manager = spotipy.SpotifyOAuth(scope="user-read-currently-playing", client_id=client_id, client_secret=client_secret, redirect_uri="https://localhost:8080")
sp = spotipy.Spotify(auth_manager=auth_manager)

current_track = sp.current_user_playing_track()
raw_track = current_track

if current_track:
    track = {"name": current_track["item"]["name"], "artists": [x["name"] for x in current_track["item"]["artists"]], "image": current_track["item"]["album"]["images"][0]["url"]}

    with open("out.html", "w+") as file:
        message = html.format(track["name"], ", ".join(track["artists"]), track["image"])
        file.write(message)
        file.close() 

    print(track)

while True:
    time.sleep(0.1)

    current_track = sp.current_user_playing_track();
    if current_track:
        if raw_track["item"]["name"] != current_track["item"]["name"]:
            raw_track = current_track

            track = {"name": raw_track["item"]["name"], "artists": [x["name"] for x in raw_track["item"]["artists"]], "image": raw_track["item"]["album"]["images"][0]["url"]}

            with open("out.html", "w+") as file:
                message = html.format(track["name"], ", ".join(track["artists"]), track["image"])
                file.write(message)
            file.close()

            print(track)