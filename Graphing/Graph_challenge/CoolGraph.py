import matplotlib.pyplot as plt
import math

f = []
l = []

try:
    n = int(input(">>>"))
except:
    n = 1024

def num(it):
    for i in range(0,it):
            f.append(i)

def XOR_anim(it):
    for i in range(1,len(f)):
        l.append(f[i]^f[i-1])
        if '0' not in str(bin(i))[1:]:
            plt.scatter(range(0,len(l)),l,s=10,color="black")
            plt.pause(1)

def XOR():
    for i in range(1,len(f)):
        l.append(f[i]^f[i-1])

def AND():
    for i in range(1,len(f)):
        l.append(f[i]&f[i-1])

def OR():
    for i in range(1,len(f)):
        l.append(f[i]|f[i-1])

num(n)
AND()

for i in range(len(l)):
    l[i] += 1

print(l.index(n)+1)

plt.scatter(range(0,len(l)),l,s=10,color="black")
plt.show()