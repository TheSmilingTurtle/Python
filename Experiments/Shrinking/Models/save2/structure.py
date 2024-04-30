import tensorflow as tf
from tensorflow import keras
from keras import Model
from keras.layers import Dense

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
