import csv
import math
import random
import time

length = 100
init_time = time.time()

l = [[-math.cos(i*math.pi/25), -math.sin(i*math.pi/25), 1-2*random.random()] for i in range(length)]

with open("test/Test.csv", "w+", newline="") as file:
    writer = csv.writer(file, delimiter=";")

    for i in range(length):
        OUTLIST = ["", time.time()-init_time]+l[i]
        writer.writerow(OUTLIST)
        time.sleep(0.01)

file.close()