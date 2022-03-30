import csv
import math
import random

length = 200

l = [["", math.sin(i*math.pi/50), math.cos(i*math.pi/50), 1-2*random.random()] for i in range(length)]

with open("test/Test.csv", "w+", newline="") as file:
    writer = csv.writer(file, delimiter=";")

    for i in range(length):
        writer.writerow(l[i])

file.close()