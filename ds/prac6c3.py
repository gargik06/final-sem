#Stepwise_Regression.py

import pandas as pd
import statsmodels.api as sm
df = pd.DataFrame({
 'Marks': [60, 65, 70, 75, 80, 85],
 'StudyHours': [2, 3, 4, 5, 6, 7],
 'Attendance': [70, 75, 80, 85, 90, 95],
 'SleepHours': [6, 7, 6, 8, 7, 8]
})
X = df[['StudyHours', 'Attendance', 'SleepHours']]
y = df['Marks']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
