#link analysis and page ranking using PageRank algorithm

import numpy as np

g=[[1,2],[0,2],[0,1],[1,2]]
n=len(g); pr=np.ones(n)/n; d=0.85

for _ in range(50):
    new=np.ones(n)*(1-d)/n
    for i in range(n):
        for j in g[i]:
            new[j]+=d*pr[i]/len(g[i])
    pr=new
for i,v in enumerate(pr):
    print("Page",i,":",v)
