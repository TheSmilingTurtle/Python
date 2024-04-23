import os
import pandas as pd

from copy import deepcopy

dir_path = "D:\\Videos_07_03_2024\\"

dishes = {"MD": "Metal Dish", "LD": "Large Dish", "WD": "White Dish", "SD": "Small Dish"}
particles = {"mp": "Magnetic", "poly": "Polyethylene", "glass": "Glass"}

videos = os.listdir(dir_path)

videos = filter(lambda x: "faulty" not in x and ".csv" not in x, videos)


v = deepcopy(videos)
d = map(lambda x: x.replace("kHz","_kHz").replace("uL", "_uL").replace("V", "_V").replace("x", "_").replace(".mov","").split("_"), v)

data = deepcopy(list(d))
for k in data:
    k[2] = dishes[k[2]]
    k[4] = particles[k[4]]

df = pd.DataFrame(zip(videos, *zip(*data)), columns=["File_Name", "Frequency", "Frequency_Units", "Dish", "Location", "Particle", "Medium", "Vpp", "Amplification", "Vpp_Units", "Amount", "Amount_Units"])

df = df.apply(pd.to_numeric, errors='coerce').fillna(df)

df.to_csv(dir_path + "registry.csv", index=False)

print((df == pd.read_csv(dir_path + "registry.csv")).all().all())