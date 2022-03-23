from typing import ValuesView
import matplotlib.pyplot as plt
import math

x, y = ([], [])

file = open(r"C:\Users\\vojta\OneDrive\VSCode\C++Proj\ToGraph.csv", encoding="utf8")
for line in file:
    l = line.split(",")
    x.append((float(l[0].strip())))
    y.append((float(l[1].strip())))
    del l

plt.scatter(x, y, s=1)
plt.scatter([x/100 for x in range(0, 200)],[math.sin((x/100)) for x in range(0, 200)], s=1)
plt.show()