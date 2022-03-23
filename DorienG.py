import math
import matplotlib.pyplot as plt

f = [0, 1]
for i in range (2, 1000):
    n = f[i-2] + f[i-1]
    if n%2:
        fi = 10*math.tan(n)/(math.tan(n)%3)
    else:
        fi = 7*math.sin(n)
    f.append(int(fi))
for i in range(0,4):
    f[i]=None

plt.scatter(range(0,len(f)), f, s=1)
plt.show()