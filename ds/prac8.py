#K-MEANS CLUSTERING

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = {
 "Marketing_Spend": [50, 60, 70, 200, 220, 250],
 "Sales": [200, 250, 300, 800, 850, 900]
}
df = pd.DataFrame(data)
kmeans = KMeans(n_clusters=2)
df["Cluster"] = kmeans.fit_predict(df)
plt.scatter(df["Marketing_Spend"], df["Sales"], c=df["Cluster"])
plt.xlabel("Marketing Spend")
plt.ylabel("Sales")
plt.title("K-Means Clustering: Sales & Marketing")
plt.show()
print("\nClustered Data:\n")
print(df)
