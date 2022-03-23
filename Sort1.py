import random
import time
import matplotlib.pyplot as plt

l1= []
l = []
g = []
m = []

try:
    num = int(input(">>>"))
except:
    pass

plt.ylim = 1
plt.xlim = num

for i in range(0,num):
    l1.append(random.random())
print("done")

def min(li):
    x = li[0]
    for i in range(0, len(li)):
        if l1[i]<x:
            x = li[i]
    return x

def plot():
    plt.bar(range(0,len(g)),g,color="black")
    plt.bar(range(0,len(l)),l,color="red")
    plt.pause(0)

g = l1.copy()

for i in range(0,len(l1)):

    l.append(min(l1))
    l1.pop(l1.index(min(l1)))
    g[l1.index(min(l1))] = 0
    plot()

plt.bar(g,range(0,len(g)),color="black")
plt.bar(l,range(0,len(l)),color="red")
plt.show()

print(l)