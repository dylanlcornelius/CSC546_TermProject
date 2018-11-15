import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

'''
data = [[]]
f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []
f7 = []
f8 = []

with open('PizzaFeatures.txt') as f:
    for line in f:
        current = line.replace('\n', '').split(',')
        #data.append(current)
        f1.append(current[0])
        f2.append(current[1])
        f3.append(current[2])
        f4.append(current[3])
        f5.append(current[4])
        f6.append(current[5])
        f7.append(current[6])
        f8.append(current[7])
'''
'''
for line in data:
    for feat in line:
        print(feat)
    print()
    '''

with open('PizzaFeatures.txt') as f:
    data = [line.replace('\n', '').split(',') for line in f]

data = np.array(data, dtype=float)

#X = np.array(list(zip(f1[:4000],f2[:4000],f3[:4000],f4[:4000],f5[:4000],f6[:4000],f7[:4000],f8[:4000])))
#X = np.array(list(zip(f1[:4000],f2[:4000],f3[:4000],f4[:4000],f5[:4000],f6[:4000],f7[:4000],f8[:4000])))
X = data[:4000]

kmeans = KMeans(n_clusters=2)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_


#print(centroids)
plt.scatter(X[:, 1], X[:, 3], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:,0], centroids[:, 1], c='black', s=200, alpha=0.5)
plt.axis('off')

#X = np.array(list(zip(f1[4001:4041],f2[4001:4041],f3[4001:4041],f4[4001:4041],f5[4001:4041],f6[4001:4041],f7[4001:4041],f8[4001:4041])))
#X = data[4001:4041]
#X = np.sort(X)
#prediction = kmeans.predict(X);
#plt.scatter(X[:,0], X[:, 1], c=prediction, s=50, cmap='viridis')

plt.show()