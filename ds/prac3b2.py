#Perform feature dummification to convert categorical variables into numerical representations.

import pandas as pd
df = pd.DataFrame({
'Gender': ['Male', 'Female', 'Male'],
'City': ['Pune', 'Delhi', 'Mumbai']
})
print("Original Data:")
print(df)
df_encoded = pd.get_dummies(df, columns=['Gender', 'City'])
print("\nAfter Dummification:")
print(df_encoded)
