import tkinter as tk
import random as rand

m = tk.Tk()
m.title("Scru u")
m.geometry(f"70x50+{rand.randint(1, m.winfo_screenwidth())}+{rand.randint(1, m.winfo_screenheight())}")

def scru_u():
    m = tk.Tk()
    m.title("Scru u")
    m.geometry(f"70x50+{rand.randint(1, m.winfo_screenwidth())}+{rand.randint(1, m.winfo_screenheight())}")
    m.mainloop()

while True:
    scru_u()