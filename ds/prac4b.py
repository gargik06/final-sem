#Conduct a hypothesis t-test, interpret the results, and draw conclusions based on the test outcomes.

import numpy as np
from scipy import stats
salary = np.array([47000, 52000, 51000, 48000, 53000, 49500,
50500])
mu_0 = 50000
t_stat, p_value = stats.ttest_1samp(salary, mu_0)
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
 print("Reject Null Hypothesis (H₀)")
else:
 print("Fail to Reject Null Hypothesis (H₀)")
