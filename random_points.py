import csv
from hashlib import new
from matplotlib import pyplot as plt
import math

x = 0
y = 0

l = []

with open("random_points.csv", "w+", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)

    for i in range(100):
        writer.writerow([x, y])
        x += (1/2)*i
        y += (1/2)/(i+1)

        l.append((x, y**(math.e*math.pi)))

plt.plot(*zip(*l))
plt.show()