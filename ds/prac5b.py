#Conduct post-hoc tests to identify significant differences between group means.

import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
data = {
"Group": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
"Value": [2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)
tukey = pairwise_tukeyhsd(endog=df["Value"],
groups=df["Group"], alpha=0.05)
print(tukey)
