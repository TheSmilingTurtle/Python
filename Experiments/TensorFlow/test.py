import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.losses import SparseCategoricalCrossentropy

import numpy as np

def get_data():
    return np.ones((1000, 100))

train = get_data()

print(train[:1].shape)

model = Sequential([
    layers.Dense( 100, input_shape=(100,), name="input"),
    layers.Dense(  50, activation='relu'),
    layers.Dense(  12, activation='relu'),
    layers.Dense(  12, activation='relu'),
    layers.Dense(   6, activation='relu', name="compressed"),
    layers.Dense(  12, activation='relu'),
    layers.Dense(  25, activation='relu'),
    layers.Dense(  50, activation='relu'),
    layers.Dense( 100, name="output")
])

predictions = model(train[:1]).numpy()
print(predictions)

print(tf.nn.softmax(predictions).numpy())

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(train, train, epochs = 1000)

model.evaluate(train, train, verbose=2)

print( tf.nn.softmax( model.predict( np.ones((1, 100)) ) ).numpy() )