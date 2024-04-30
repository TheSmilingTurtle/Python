import pandas as pd
from dateutil import parser
import numpy as np

data = pd.read_csv("/home/thesmilingturtle/coding/Python/Experiments/Weather/ugz_ogd_meteo_h1_2023.csv")
del data["Status"]

data["Datum"] = pd.to_datetime(data["Datum"])

def get_by_parameters(params, d=data):
    c = []

    for p in params:
        c.append(d[d["Parameter"] == p].reset_index()["Wert"].rename(p))
    
    return pd.concat(c, axis=1)

def get_by_location(loc, params, d=data):
    a = []

    for l in loc:
        c = get_by_parameters(params, d=d[d["Standort"] == l])
        if len(loc) > 1:
            b = []
            for k in c.columns:
                b.append(k + "_" + l)
            c.columns = b
        a.append(c)
    return pd.concat(a, axis=1)