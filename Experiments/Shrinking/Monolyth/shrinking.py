import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Model

import pandas as pd
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

shrink = Shrink()

SAVE = '/home/thesmilingturtle/coding/Python/Experiments/Shrinking/Models/Monolyth/save1'

shrink.load_weights(SAVE)

loss_object = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam()

@tf.function
def train_step(vector):
    with tf.GradientTape() as tape:
        predictions = shrink(vector, training=True)
        loss = loss_object(vector, predictions)
        gradients = tape.gradient(loss, shrink.trainable_variables)
        optimizer.apply_gradients(zip(gradients, shrink.trainable_variables))

train = pd.read_csv("/home/thesmilingturtle/coding/Python/Experiments/Shrinking/BIG5/data.csv", sep="\t", usecols=['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'])
train.replace(0, 3)
print(train.head(3))

train_tensor = tf.convert_to_tensor(train)

train_ds = tf.data.Dataset.from_tensor_slices(train_tensor).batch(32)

EPOCHS = 100

records = []

for epoch in range(EPOCHS):
    for person in train_ds:
        train_step(person)

    e = mean_squared_error(train_tensor, shrink(train_tensor, training=False))
    records.append(e)

    print(
    f'Epoch {epoch + 1} \t'
    f'Train_loss: {e}'
    )

shrink.save_weights(SAVE)

plt.plot(range(len(records)), records)
plt.show()
