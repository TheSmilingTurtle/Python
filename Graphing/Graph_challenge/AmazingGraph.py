import math
import matplotlib.pyplot as plt

l = []

m = input("Mode [s]/a: ").lower()
mode = m[:1]

try:
    num = int(m[1:])
except:
    num = None

def anim(i, t): 
    if i < t/20:
        if not i%(t/2000):
            plt.scatter(range(0,len(l)), l, s=0.02, color = "black")
            plt.pause(1/(i**3))
    elif i < t/2:
        if not i%(t/100):
            plt.scatter(range(0,len(l)), l, s=0.02, color = "black")
            plt.pause(1/(i**3))
    elif i > t/2:
        if not i%(t/40):
            plt.scatter(range(0,len(l)), l, s=0.02, color = "black")
            plt.pause(1/(i**3))        

def run_anim(t = 20000):
    for i in range(1, t):
        l.append(math.sin(i/(i**(100/i))/2))
        anim(i, t)


def run(t = 20000):
    for i in range(1, t):
        l.append(math.sin(i/(i**(100/i))/2))

def show():
    plt.scatter(range(0,len(l)), l, s=0.001, color = "black")
    plt.show()

if mode == "a":
    if num:
        run_anim(num)
    else:
        run_anim()
    plt.show()

elif mode == "s" or mode == "":
    if num:
        run(num)
    else:
        run()
    show()