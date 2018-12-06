#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas as pd
import numpy as np 

# Load dataset
with open('PizzaFeatures.txt') as f:
    data = [line.replace('\n', '').split(',') for line in f]

data = np.array(data, dtype=float)

X = data[:4000]
# Setting up x-axis labels for dendrogram
receivedpizza = X[:,8]
# Removing karma and did_receieve_pizza
X = X[:,0:7] 
samples = X

from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

mergings = linkage(samples, method='complete')

# Plot a dendrogram using the dendrogram() function on mergings
dendrogram(mergings,
           truncate_mode='lastp',
           labels=receivedpizza,
           leaf_rotation=90,
           leaf_font_size=10,
)
plt.savefig('hierarchical_clustering.pdf', bbox_inches='tight')
plt.show()


# In[ ]:




