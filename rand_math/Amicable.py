import math
import time

f = []
a = []

try:
    it = int(input(">>>"))
except: 
    print("You didn't input an integer, so here are the first two amicable numbers:\n") 
    it = 284

def lcalc(i):
    l = 0
    num = math.ceil(math.sqrt(i))
    for j in range(1,num):
        if not i%j:
            l+=j
            if j!=1:
                l+=int(i/j)
    return l

def fcalc():
    iterations = it+1
    for i in range(0,iterations):
        f.append(lcalc(i))

def amic():
    fcalc()
    for i in range(0,len(f)):
        if not f[i] or (f[i],i) in a or i==f[i]:
            continue
        if f[i]<len(f):
            if i==f[f[i]]:
                a.append((i,f[i]))

t0 = time.time()
amic()
t = time.time()

print(str(a)[1:-1])
print((t-t0)*1000,"ms")