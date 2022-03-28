import turtle
import random
import math
i = 0
g = False
pi = math.pi
try:
    n = float(input(">>>"))
except:
    n = 1711/2560 * pi

l = []
f = []
t = turtle.Pen()
t.radians()
t.speed(0)

def fetch():
    for i in range(0, len(l)):
        if math.sqrt(t.pos()[0]**2+t.pos()[1]**2)+1/len(str(n)) >= l[i] and math.sqrt(t.pos()[0]**2+t.pos()[1]**2)-1/len(str(n)) <= l[i]:
            f.append(t.pos())
            break
    l.append(math.sqrt(t.pos()[0]**2+t.pos()[1]**2))

while True:
    if i >= 20*pi:
        i -= 20*pi
        if g:
            break 
        g = True
    i += pi/10
    if n:
        t.forward(15-i/n)
    else:
        t.forward(15)
    t.left(i/10)
    fetch()

print(f)
print(len(l)/2 >= len(f))
turtle.done()