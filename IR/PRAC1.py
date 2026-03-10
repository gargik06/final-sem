#implementation of documentation indexing and retrieval using inverted index
#pip install nltk


import nltk
from nltk.corpus import stopwords
doc1="The quick brown fox jumped over the lazy dog".lower().split()
doc2="The lazy dog slept in the sun".lower().split()
nltk.download('stopwords'); stop=set(stopwords.words('english'))
for t in set(doc1+doc2):
    if t not in stop:
        d=[]
        if t in doc1: d.append(f"Document1({doc1.count(t)})")
        if t in doc2: d.append(f"Document2({doc2.count(t)})")
        print(t,"->",", ".join(d))
print("Performed by 740_Pallavi & 743_Deepak")
