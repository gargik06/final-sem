#Conduct a hypothesis chi square test, interpret the results, and draw conclusions based on the test outcomes.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
data = pd.DataFrame({
'Pass': [40, 30],
'Fail': [10, 20]
}, index=['Male', 'Female'])
print(data)
chi2, p, dof, expected = chi2_contingency(data)
print("Chi-Square Value:", chi2)
print("p-value:", p)
print("Degrees of Freedom:", dof)
print(expected)
if p < 0.05:
 print("Variables (Result and Gender) are dependent (related)")
else:
 print("Variables are independent (Not related)")
data.plot(kind='bar')
plt.title("Observed Frequencies: Gender vs Result")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.show() 
