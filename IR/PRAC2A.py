#retrieval using boolean operator and vector space model
#pip install pandas scikit-learn

docs={1:"apple banana orange",2:"apple banana",3:"banana orange",4:"apple"}
index={}
for i,t in docs.items():
    for w in set(t.split()):
        index.setdefault(w,set()).add(i)
AND=lambda q: list(index[q[0]].intersection(index[q[1]]))
OR=lambda q: list(index[q[0]].union(index[q[1]]))
NOT=lambda q: list(set(docs)-index[q])
print("apple AND banana:",AND(["apple","banana"]))
print("apple OR orange:",OR(["apple","orange"]))
print("NOT orange:",NOT("orange"))
