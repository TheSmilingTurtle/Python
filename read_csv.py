import csv
import matplotlib.pyplot as plt

l = []

with open("ToGraph.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        l.append((float(row.strip().split(",")[0]), float(row.strip().split(",")[1])))

plt.scatter(zip(*l))
plt.show()