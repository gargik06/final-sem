#BUILD A LOGISTIC REGRESSION MODEL TO PREDICT A BINARY OUTCOME

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
pred = model.predict([[2]])
print("Predicted Class:", pred[0])
