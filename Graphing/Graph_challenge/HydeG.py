import matplotlib.pyplot as plt
import math

def graph(func, to):
    g = []
    for i in range(to):
        g.append(func(i))
    plt.scatter(range(len(g)), g , s=1)
    plt.show()

def func(x):
    if x==0:
        return None
    out = (x//4)//math.sin(x)
    if abs(out)>600:
        return None
    return out

if __name__ == "__main__":
    graph(func, 1000)
