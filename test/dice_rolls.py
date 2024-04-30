import pandas as pd
from random import randint
import matplotlib.pyplot as plt

N = 100_000

def roll(d, n, disc=1):
    return sum( sorted( [randint(1,d) for _ in range(n)] )[disc:] )

raw = [roll(6, 1, 0) for _ in range(N)]

series = pd.Series(raw)

counts = series.value_counts()/N
print("mean = ", series.mean())

plt.bar(counts.keys(), counts.values)
plt.show()