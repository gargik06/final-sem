#spelling correction in information retrieval system

def editDistance(a,b,m,n):
    if m==0: return n
    if n==0: return m
    if a[m-1]==b[n-1]:
        return editDistance(a,b,m-1,n-1)
    return 1+min(editDistance(a,b,m,n-1),
                 editDistance(a,b,m-1,n),
                 editDistance(a,b,m-1,n-1))
print("Edit Distance:",editDistance("sunday","saturday",6,8))
