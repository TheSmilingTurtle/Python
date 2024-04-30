import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Model

import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class Shrink(Model):
    def __init__(self):
        super(Shrink, self).__init__()
        self.i = layers.InputLayer(50)
        self.l1 = layers.Dense(128, activation='tanh')
        self.l2 = layers.Dense(64, activation='tanh')
        self.l3 = layers.Dense(5, activation='tanh')
        self.out = layers.Dense(50)

    def call(self, X):
        X = X - 3
        X = self.l1(X)
        X = self.l2(X)
        X = self.l3(X)
        X = self.out(X)
        X = X + 3
        return X
    
    def comp(self, X):
        X = X - 3
        X = self.l1(X)
        X = self.l2(X)
        X = self.l3(X)
        return X
    
    def decomp(self, X):
        X = self.out(X)
        X = X + 3
        return X

person = "Isa"

test = pd.read_csv("/home/thesmilingturtle/coding/Python/Experiments/Shrinking/Tests/data.csv", usecols=['Name', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'])
test = test[test["Name"] == person]
test = test.drop('Name', axis=1)
test.replace(0,3)

test_tensor = tf.convert_to_tensor(test)

SAVE = '/home/thesmilingturtle/coding/Python/Experiments/Shrinking/Models/Monolyth/save1'

shrink = Shrink()

shrink.load_weights(SAVE)

comp = shrink.comp(test_tensor)
decomp = shrink.decomp(comp)

print()
print(f"Results for: {person}")
print(f"comp   = {comp.numpy()}")
print(f"decomp = {decomp.numpy()}")
print(f"test_tensor = {test_tensor.numpy()}")
print(f"decomp rounded = {np.rint(decomp.numpy())}")
print(f"difference = {np.abs(test_tensor.numpy() - np.rint(decomp.numpy()))}")
print("Counts: ", *zip(*np.unique(np.abs((test_tensor - np.rint(decomp.numpy()))), return_counts=True)))
print(f"Error: {mean_squared_error(test_tensor, decomp)}")