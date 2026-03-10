from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
import numpy as np; from numpy.linalg import norm

train=["The sky is blue","The sun is bright"]
test=["The sun in the sky is bright"]

v=CountVectorizer(stop_words='english')
X=v.fit_transform(train).toarray(); Y=v.transform(test).toarray()

cos=lambda a,b: round(np.inner(a,b)/(norm(a)*norm(b)),3)
print("Train:",X,"\nTest:",Y,"\nCosine:",cos(X[1],Y[0]))

print(TfidfTransformer().fit_transform(X).toarray())
print(TfidfTransformer().fit_transform(Y).todense())
