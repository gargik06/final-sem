#Implement simple linear regression using a dataset.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.title("Simple Linear Regression")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.grid(True)
plt.show()
