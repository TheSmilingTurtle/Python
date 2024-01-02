import pandas as pd 

df = pd.read_csv("tracks.csv")

print(df.groupby("Track").mean())
print()
print(df.groupby("Album").mean())
print()
print(df.groupby("Year").mean())
print()
print(df.describe())
print()
print(df.corr())
print()
print(f"Average: {df.mean().mean()}")