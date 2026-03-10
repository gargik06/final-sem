#text categorization using machine learning techniques

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"C:\Users\Administrator\Documents\Sem\6\IR\Dataset.csv")

X = (df["covid"] + " " + df["fever"]).astype(str)
y = df["flu"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

vec = CountVectorizer()
model = MultinomialNB()

X_train = vec.fit_transform(X_train)
model.fit(X_train, y_train)

X_test = vec.transform(X_test)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

test = pd.read_csv(r"C:\Users\Administrator\Documents\Sem6\IR\Test.csv")
pred = model.predict(vec.transform((test["covid"]+""+test["fever"]).astype(str)))

print(pred)
test["flu_prediction"] = pred
test.to_csv(r"C:\Users\Administrator\Documents\Sem 6\IR\Test1.csv",index=False)