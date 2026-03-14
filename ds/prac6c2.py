#Multiple_linear_regression.py

import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.DataFrame({
 'Area': [800, 1000, 1200, 1500],
 'Bedrooms': [2, 3, 3, 4],
 'Price': [40, 55, 65, 80]
})
X = df[['Area', 'Bedrooms']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
