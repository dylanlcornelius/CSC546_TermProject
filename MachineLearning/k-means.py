import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

with open('PizzaFeatures.txt') as f:
    data = [line.replace('\n', '').split(',') for line in f]

data = np.array(data, dtype=float)

X = data[:4000]
X = X[:, 0:7]

kmeans = KMeans(n_clusters=2)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

first = 0
second = 3

plt.scatter(X[:, first], X[:, second], c=labels, s=25, cmap='viridis')
plt.scatter(centroids[:,0], centroids[:, 1], c='black', s=200, alpha=0.5)

X = data[:4000]
X = X[:, 0:9]
i = 0
while i < len(X):
    if X[i, 8] == 0:
        X = np.delete(X, i, axis=0)
        i = i - 1
    i = i + 1
plt.scatter(X[:, first], X[:, second], s=2, cmap='Blues')

#X = np.array(list(zip(f1[4001:4041],f2[4001:4041],f3[4001:4041],f4[4001:4041],f5[4001:4041],f6[4001:4041],f7[4001:4041],f8[4001:4041])))
#X = data[4001:4041]
#X = X[:, 1:7]
#X = np.sort(X)
#prediction = kmeans.predict(X);
#plt.scatter(X[:,2], X[:, 4], c=prediction, s=50, cmap='viridis')
#plt.scatter(centroids[:,0], centroids[:, 1], c='black', s=200, alpha=0.5)
#plt.axis('off')
plt.ylabel("Account Age at Request")
plt.xlabel("Upvotes")
plt.show()