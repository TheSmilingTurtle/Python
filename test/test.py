import csv
import math
import random

l = [[math.sin(i*math.pi/50), math.cos(i*math.pi/50), 1-2*random.random()] for i in range(100)]

with open("test/Test.csv", "w+", newline="") as file:
    writer = csv.writer(file, delimiter=";")

    for i in range(100):
        writer.writerow(l[i])

file.close()