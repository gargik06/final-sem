#logistic_regression.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
df = pd.DataFrame({
 'Hours': [2, 4, 6, 8],
 'Result': [0, 0, 1, 1]
})
X = df[['Hours']]
y = df['Result']
model = LogisticRegression()
model.fit(X, y)
pred = model.predict([[5]])
prob = model.predict_proba([[5]])
print("Predicted Class:", pred[0])
print("Probability:", prob)
