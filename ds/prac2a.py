#Read data from CSV and JSON files into a DataFrame
#(Do pip install pandas in cmd if not there)

import pandas as pd
df = pd.read_csv('Student_Marks.csv')
print("=" * 10)
print("CSV Data")
print("=" * 10)
print(df)
print("=" * 10)
print("JSON Data")
print("=" * 10)
data = pd.read_json('employees.json')
print(data) 