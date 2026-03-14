#Manipulate and transform data using functions like filtering, sorting, and grouping.
import pandas as pd
df = pd.read_csv('Student_Marks.csv')
print("Original Dataset:")
print(df)
print("\nStudents from Science Stream:")
filtered_df = df[df['stream'] == 'Science']
print(filtered_df)
print("\nStudents having percentage > 90:")
high_Per = df[df['per'] > 90]
print(high_Per)
print("\nStudents having percentage > 90 and from Science Stream:")
high_Per_stm = df[(df['per'] > 90) & (df['stream'] == 'Science')]
print(high_Per_stm)
print("\nSorting Students data by 'per' column:")
sorted_df = df.sort_values(by='per', ascending=False)
print(sorted_df)
sorted_df.to_csv("filtered_sorted_Student_Marks.csv",index=False)