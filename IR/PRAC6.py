#document clustering using k-means algorithm

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

docs=["Cats are known for agility",
      "Dogs are man's best friend",
      "Dogs assist disabled people",
      "Sun rises in east",
      "Cats climb trees"]

X=TfidfVectorizer(stop_words='english').fit_transform(docs)
print(KMeans(n_clusters=3,random_state=0).fit(X).labels_)
