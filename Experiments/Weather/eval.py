import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Model

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import time

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from dataset import get_by_location

class WPM(Model):
    def __init__(self):
        super(WPM, self).__init__()
        self.i = layers.InputLayer(90)
        self.l1 = layers.Dense(64, activation="relu")
        self.l2 = layers.Dense(128, activation="relu")
        self.l3 = layers.Dense(64, activation="relu")
        self.l4 = layers.Dense(16, activation="relu")
        self.out = layers.Dense(5)

    def call(self, X):
        X = self.i(X)
        X = self.l1(X)
        X = self.l2(X)
        X = self.l3(X)
        X = self.l4(X)
        X = self.out(X)
        return X

model = WPM()

SAVE = '/home/thesmilingturtle/coding/Python/Experiments/Weather/Saves/save1'

model.load_weights(SAVE)

data = pd.read_csv("/home/thesmilingturtle/coding/Python/Experiments/Weather/ugz_ogd_meteo_h1_2024.csv")

q = get_by_location(["Zch_Stampfenbachstrasse", "Zch_Rosengartenstrasse", "Zch_Schimmelstrasse"], ["T", "Hr", "p", "RainDur", "WD", "WVs"], d=data).dropna()
print(q.tail(5))
q = tf.convert_to_tensor(np.array(q.tail(5)).flatten().reshape((1,-1)))

print(model(q, training=False))