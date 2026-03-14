#Perform feature dummification to convert categorical variables into numerical representations.

import pandas as pd
df = pd.DataFrame({'City': ['Mumbai', 'Delhi', 'Pune',
'Mumbai']})
print("Original DataFrame:")
print(df)
df_dummies = pd.get_dummies(df, columns=['City'])
print("\nAfter Dummification:")
print(df_dummies)
