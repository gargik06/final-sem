#Construct a decision tree model and interpret the decision rules for classification. 

from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X = [
 [1, 50],
 [2, 60],
 [3, 65],
 [4, 70],
 [5, 75],
 [6, 80],
 [7, 85],
 [8, 90]
]
y = [0, 0, 0, 0, 1, 1, 1, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
feature_names = ["Study_Hours", "Attendance"]
tree_rules = export_text(model, feature_names=feature_names)
print("\nDecision Tree Rules:\n")
print(tree_rules)
