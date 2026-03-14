#Apply feature-scaling techniques like standardization and normalization to numerical features.

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
df = pd.DataFrame({'Age': [18, 22, 25, 30, 40]})
print("Original Data:")
print(df)
scaler = StandardScaler()
df['Age_std'] = scaler.fit_transform(df[['Age']])
print("\nAfter Standardization:")
print(df)
normalizer = MinMaxScaler()
df['Age_norm'] = normalizer.fit_transform(df[['Age']])
print("\nAfter Normalization:")
print(df)
