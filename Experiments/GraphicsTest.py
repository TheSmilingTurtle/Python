import tkinter as tk
import turtle
import random as rand

win = tk.Tk()
win.title("test")
win.geometry("500x500")

def Button(text, width=None, height=None, PosX=None, PosY=None, command=None, bg=None):
    b = tk.Button(win, text=text, width=width, height=height, command=command, bg=bg)
    b.place_configure(x=PosX, y=PosY)

#Button("AAAAAAAAAAAA", 30, 30, 50, 40)
#Button("B", 4, 3, 50, 40)

c = tk.Canvas(win, width=200, height=100)
c.place(x=0,y=0)
c.create_rectangle(50, 25, 150, 75)

win.mainloop()