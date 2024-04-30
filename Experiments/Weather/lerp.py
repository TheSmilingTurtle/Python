from dataset import data, get_by_location
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

X = get_by_location(["Zch_Stampfenbachstrasse", "Zch_Rosengartenstrasse", "Zch_Schimmelstrasse"], ["T", "Hr", "p", "RainDur"]).dropna()
y = np.vstack([X["T_Zch_Stampfenbachstrasse"][(1+i):(len(X["T_Zch_Stampfenbachstrasse"])+i-4)].values for i in range(5)]).T
X= X[:-5].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

model = LinearRegression().fit(X_train, y_train)

print(model.intercept_, model.coef_)
print(mean_squared_error(y_test, model.predict(X_test), squared=False))

q = np.array([[9.55, 61.41, 959.3, 0, 9.62, 63.04, 961.78, 0, 9.38, 62.48, 959.4, 0]])

print(model.predict(q))