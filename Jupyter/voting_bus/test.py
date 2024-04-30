from sklearn.linear_model import LinearRegression
import numpy as np

x = np.linspace(0, 100, 100)
y = np.random.rand(100) + x

model = LinearRegression()

model.fit(x.reshape(-1, 1), y)

print(model.score(x.reshape(-1,1),y))