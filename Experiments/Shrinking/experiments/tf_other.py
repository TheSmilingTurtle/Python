import tensorflow as tf
import pandas as pd 
import numpy as np

x_train = pd.read_csv("Shrinking/BIG5/data.csv", sep="\t", usecols=['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'])
x_train.replace(0, 3)
print(x_train.head(3))

y_train = pd.read_csv("Shrinking/BIG5/data.csv", sep="\t", usecols=['age', 'gender'])

keep = y_train['age']<120

x_train = x_train[keep]
y_train = y_train[keep]

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(50, input_shape=(50,)),
  tf.keras.layers.Dense(50, activation='sigmoid'),
  tf.keras.layers.Dense(20, activation='sigmoid'),
  tf.keras.layers.Dense(2)
])

model.compile(
    optimizer=tf.optimizers.Adam(),
    loss=tf.keras.losses.MeanSquaredError(),
    metrics=['MSE']
)

model.summary()

x_train_tensor = tf.convert_to_tensor(x_train)
y_train_tensor = tf.convert_to_tensor(y_train)

model.fit(x_train_tensor, y_train_tensor, epochs=5)

pred = model.predict(x_train_tensor)
print(pd.DataFrame(data=tf.math.round(pred), columns=y_train.columns, dtype=np.uint).head(10))
print(y_train.head(10))

model.evaluate(x_train_tensor, y_train_tensor, verbose=2)
