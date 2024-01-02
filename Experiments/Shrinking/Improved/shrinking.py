import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Model

class Compressor(Model):
    def __init__(self):
        super(Compressor, self).__init__()
        self.i = layers.InputLayer((50,))
        self.l1 = layers.Dense(128, activation='tanh')
        self.l2 = layers.Dense(128, activation='tanh')
        self.out = layers.Dense(5,  activaiton='tanh')
    
    def call(self, X):
        X = self.i(X)
        X = self.l1(X)
        X = self.l2(X)
        X = self.out(X)
        return X

class Decompressor(Model):
    def __init__(self):
        super(Decompressor, self).__init__()
        self.i = layers.InputLayer((6,))
        self.out = layers.Dense(50)
    
    def call(self, X):
        X = self.i(X)
        X = self.l1(X)
        X = self.l2(X)
        X = self.out(X)
        return X

class Shrink(Model):
    def __init__(self):
        super(Shrink, self).__init__()
        self.comp = Compressor()
        self.decomp = Decompressor()

    def call(self, X):
        X = self.comp(X)
        X = self.decomp(X)
        return X
    

shrink = Shrink()

loss_object = tf.keras.losses.MeanAbsoluteError()
optimizer = tf.keras.optimizers.Adam()

train_loss = tf.keras.losses.MeanAbsoluteError()

@tf.function
def train(vector):
    with tf.GradientTape() as tape:
        predictions = shrink(vector, training=True)
        loss = loss_object(vector, predictions)
        gradients = tape.gradient(loss, shrink.trainable_variables)
        optimizer.apply_gradients(zip(gradients, shrink.trainable_variables))

        train_loss(predictions, vector)

