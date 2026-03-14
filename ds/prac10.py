#DATA VISUALIZATION AND STORYTELLING

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
 "Customer_ID": [1,2,3,4,5,6,7,8,9,10],
 "Rating": [5,4,3,5,2,1,4,5,3,2], # Rating out of 5
 "Review": ["Positive","Positive","Neutral","Positive",
 "Negative","Negative","Positive","Positive",
 "Neutral","Negative"]
}
df = pd.DataFrame(data)
sns.set_style("whitegrid")
plt.figure()
sns.countplot(x="Rating", data=df)
plt.title("Customer Rating Distribution")
plt.xlabel("Rating (1-5)")
plt.ylabel("Number of Customers")
plt.show()
plt.figure()
sns.countplot(x="Review", data=df)
plt.title("Customer Review Analysis")
plt.xlabel("Review")
plt.ylabel("Count")
plt.show()
avg_rating = df["Rating"].mean()
positive_count = len(df[df["Review"]=="Positive"])
negative_count = len(df[df["Review"]=="Negative"])
neutral_count = len(df[df["Review"]=="Neutral"])
story = f"""
CUSTOMER REVIEW DATA STORY:
Out of {len(df)} customers, {positive_count} gave positive feedback,
{neutral_count} gave neutral feedback, and {negative_count} gave negative
feedback.
The average customer rating is {round(avg_rating,2)} out of 5.
The majority of customers provided positive ratings,
indicating overall customer satisfaction with the product.
However, a small number of negative reviews suggest areas for improvement.
CONCLUSION:
The product performance is generally strong,
but focusing on resolving customer complaints could further improve satisfaction
and brand reputation.
"""
print(story)
