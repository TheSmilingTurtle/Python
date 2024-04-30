import pandas as pd

import matplotlib.pyplot as plt

from tqdm import tqdm

import tensorflow as tf
from tensorflow import keras
from keras import Model
from keras.layers import Dense

train = pd.read_csv("Shrinking/BIG5/data.csv", sep="\t", usecols=['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'])
train.replace(0, 3)
print(train.head(3))

train_tensor = tf.convert_to_tensor(train)

train_ds = tf.data.Dataset.from_tensor_slices(train_tensor).batch(32)

class Compressor(Model):
    def __init__(self):
        super(Compressor, self).__init__()
        self.l1 = Dense(50, input_shape=(50,))
        self.l2 = Dense(50, activation='relu')
        self.l3 = Dense(50, activation='tanh')
        self.l4 = Dense(20, activation='tanh')
        self.out = Dense(6, activation='tanh')

    def call(self, X):
        X = self.l1(X)
        X = self.l2(X)
        X = self.l3(X)
        X = self.l4(X)
        X = self.out(X)
        return X

class Decompressor(Model):
    def __init__(self):
        super(Decompressor, self).__init__()
        self.l1 = Dense(6, input_shape=(6,))
        self.l2 = Dense(40, activation='tanh')
        self.out = Dense(50)

    def call(self, X):
        X = self.l1(X)
        X = self.l2(X)
        X = self.out(X)
        return X
    
class Shrink(Model):
    def __init__(self):
        super(Shrink, self).__init__()
        self.compressor = Compressor()
        self.decompressor = Decompressor()

    def call(self, X):
        X = self.compressor(X)
        X = self.decompressor(X)
        return X

shrink = Shrink()

LOAD = './Shrinking/Models/save2/save2'

shrink.load_weights(LOAD)

for person in train_ds:
    print(shrink.compressor(person, training=False)[0:3])
    break