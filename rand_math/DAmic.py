import math
import time

a = int(input(">>>"))
g = []
c = []

t0 = time.time()
for x in range (0, a+1):
    d = []
    sd = 0
    j = 0
    g.append(0)
    for i in range (1, x):
        if not x%i:
            d.append(i)
    if d:
        while j < len(d):
            sd = sd + d[j-1]
            j += 1
    if math.gcd(sd, x) > 1:
        g[x] = sd
        if sd > a:
            g[x] = 0
        if x == sd:
            g[x] = 0
    else:
        g[x] = 0
x = 1
while x < len(g):
    b = g[x]
    if g[b] != x:
        g[x] = 0
    else:
        print("(%s, %s)" % (x, g[x]))
        g[g[x]] = 0
        c.append(x)
        c.append(g[x])
    x += 1
t2 = time.time()

print("The total time is: %s ms" % ((t2-t0)*1000))
print("There are %s pair(s) of amicable numbers" % (int(len(c)/2)))