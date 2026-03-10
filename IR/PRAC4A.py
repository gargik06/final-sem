#evaluation metrics for information retrieval system

retrieved={"doc1","doc2","doc3"}
relevant={"doc1","doc4"}

tp=len(retrieved&relevant)
fp=len(retrieved-relevant)
fn=len(relevant-retrieved)

p=tp/(tp+fp); r=tp/(tp+fn)
f=2*p*r/(p+r)

print("Precision:",p,"\nRecall:",r,"\nF-measure:",f)
