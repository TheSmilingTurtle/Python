import csv

l = [[j+i+i*j for j in range(3)] for i in range(100)]

with open("test/Test.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")

    for i in range(100):
        writer.writerow(l[i])

file.close()