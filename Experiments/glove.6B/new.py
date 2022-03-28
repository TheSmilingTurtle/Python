import csv
import time
import sys

csv.field_size_limit(sys.maxsize)

t0 = time.time()
with open("/Users/vojta.kottas/Desktop/glove.6B.50d.csv") as f:
    reader = csv.reader(f, delimiter=" ")
    word_embeddings = {}
    for row in reader:
        if row[0] in word_embeddings:
            pass
        word_embeddings[row[0]] = row[1:]
t = time.time()

print(t-t0)
print(len(word_embeddings))