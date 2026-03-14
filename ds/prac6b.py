#Explore and interpret the regression model coefficients and goodness-offit measures.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = {
 'Hours': [1, 2, 3, 4, 5, 6],
 'Marks': [35, 40, 50, 65, 70, 85]
}
df = pd.DataFrame(data)
print(df)
X = df[['Hours']]
y = df['Marks']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print("Predicted Marks:", y_pred)
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.show()
new_hours = [[7]]
predicted_marks = model.predict(new_hours)
print("Predicted marks for 7 hours:", predicted_marks[0])
