import matplotlib.pyplot as plt
import math

try:
    x = int(input(">>>"))
except:
    x = 100
l = []
f = []
k=1
a = False

def calc(k):
    for i in range(x):
        for j in range (i):
            l.append((-1)**(j/(i*math.e)))
            f.append(j)

def anim():
    global k
    while k>=0:
        l = []
        f = []
        k -= (1/1000)
        calc(k)
        plt.scatter(l, f, s=1, color="black")
        plt.pause(0.00001)
        plt.clf()

if a:
    anim()
else:
    calc(k)

plt.scatter(l, f, s=1, color="black")
plt.show()