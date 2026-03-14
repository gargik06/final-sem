#Perform one-way ANOVA to compare means across multiple groups.

from scipy import stats
import matplotlib.pyplot as plt
diet_A = [2, 3, 4]
diet_B = [5, 6, 7]
diet_C = [8, 9, 10]
f_stat, p_value = stats.f_oneway(diet_A, diet_B,
diet_C)
print("F-statistic =", f_stat)
print("p-value =", p_value)
if p_value < 0.05:
 print("Reject Null hypothesis (H₀) i.e. At least one diet plan is different")
else:
 print("All diet plans are equal")
data = [diet_A, diet_B, diet_C]
plt.figure(figsize=(6, 4))
plt.boxplot(data)
plt.xticks([1, 2, 3], ['Diet A', 'Diet B', 'Diet C'])
plt.title("One-Way ANOVA: Weight Loss Across Diets")
plt.xlabel("Diet Groups")
plt.ylabel("Weight Loss")
plt.tight_layout()
plt.show() 
