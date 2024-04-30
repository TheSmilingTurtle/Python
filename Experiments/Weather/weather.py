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

SAVE='/home/thesmilingturtle/coding/Python/Experiments/Weather/Saves/save1'

model.load_weights(SAVE)

loss_object = keras.losses.MeanAbsoluteError()
optimizer = keras.optimizers.Adam()

@tf.function
def train(X, y):
    with tf.GradientTape() as tape:
        predictions = model(X, training=True)
        loss = loss_object(y, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

EPOCHS = 1000

X = get_by_location(["Zch_Stampfenbachstrasse", "Zch_Rosengartenstrasse", "Zch_Schimmelstrasse"], ["T", "Hr", "p", "RainDur", "WD", "WVs"]).dropna()
y = np.vstack([X["T_Zch_Stampfenbachstrasse"][(5+i):(len(X["T_Zch_Stampfenbachstrasse"])+i-4)].values for i in range(5)]).T
X = np.hstack([X[i:i-9].values for i in range(5)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(32)

records = []

start = time.time()

for epoch in range(EPOCHS):
  # Reset the metrics at the start of the next epoch
  for _X, _y in train_ds:
    train(_X, _y)

  test_error = mean_absolute_error(y_test, model(X_test, training=False))
  records.append(test_error)

  print(
    f'Epoch: {epoch + 1}\t',
    f'Test error: {test_error} '
  )

end = time.time()

print(f"\nTraining took {end-start}s")
print(f"Training errors: {mean_absolute_error(y_test, model(X_test, training=False), multioutput='raw_values')}\n")

model.save_weights(SAVE)

plt.plot(range(len(records)), records)
plt.show()

