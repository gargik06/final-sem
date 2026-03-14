#Perform basic data pre-processing tasks such as handling missing values and outliers

import pandas as pd
df = pd.read_csv('Enrollment.csv')
print("Original Dataset:")
print(df)
print("\nDataset after filling NA in Age column:")
df['Age'] = df['Age'].fillna(18)
print(df)
print("\nDataset after dropping rows with NA:")
df_cleaned = df.dropna()
print(df_cleaned)