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

client_id = "01cbf6272b014997b6d2fa234b7c788e"
client_secret = "ac1498c3cd354058bada1f4cf65488f3"

token = spotipy.util.prompt_for_user_token(scope="user-read-currently-playing", client_id=client_id, client_secret=client_secret, redirect_uri="https://localhost/")
sp = spotipy.Spotify(auth=token)

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