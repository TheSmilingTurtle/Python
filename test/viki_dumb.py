from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

import matplotlib.pyplot as plt

data = [3, 4, 5.5, 7.5, 11.333, 19.6651, 38.2305, 76.7694, 149.383, 294.6102]

X = np.arange(0, len(data), 1).reshape(-1,1)
y = np.array(data).reshape(-1,1)

poly = PolynomialFeatures(degree=9)
X_t = poly.fit_transform(X)

model = LinearRegression(fit_intercept=False)

model.fit(X_t,y)

next_pt = poly.fit_transform(np.array(len(data)).reshape(-1,1))

pred = model.predict(next_pt)
score = model.score(X_t, y)
print(f"Prediction: {pred[0,0]}, score: {score}")
print(f"Coefficients: {model.coef_}")
x_p = np.linspace(0, next_pt[0,1], 100).reshape(-1,1)

out = model.predict(poly.fit_transform(x_p))

plt.plot(x_p, out, c="blue")
plt.scatter(X, y, c="red")
plt.scatter(next_pt[0,1], pred[0,0], c="orange")
plt.show()