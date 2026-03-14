#INSTALL NUMPY,PANDAS,MATPLOTLIB,SCIKIT-LEARN,STATSMODEL BY USING PIP COMMAND
#PRINCIPAL COMPONENT ANALYSIS(PCA)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
data = {
 "Math": [85, 90, 78, 92, 88, 76, 95, 89],
 "Science": [80, 85, 75, 95, 90, 70, 96, 88],
 "English": [78, 88, 72, 91, 85, 74, 94, 86],
 "History": [70, 82, 68, 89, 84, 65, 90, 80]
}
df = pd.DataFrame(data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)
pca_df = pd.DataFrame(data=principal_components,columns=["PC1", "PC2"])
plt.scatter(pca_df["PC1"], pca_df["PC2"])
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Reduced to 2 Dimensions")
plt.show()
