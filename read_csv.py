import csv
import matplotlib.pyplot as plt

l = []

with open(r"C:\Users\vojta\Documents\Coding\Python\ToGraph.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        l.append((float(row[0]), float(row[1])))

plt.scatter(*zip(*l), s=1)
plt.show()