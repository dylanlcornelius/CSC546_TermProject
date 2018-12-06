import numpy as np
import sompy
# pip3 install git+https://github.com/compmonks/SOMPY.git

with open('PizzaFeatures.txt') as f:
    data = [line.replace('\n', '').split(',') for line in f]

data = np.array(data, dtype=float)
data = data[:, 0:7]

colors = ['blue', 'red']

som = sompy.SOMFactory.build(data, mapsize=[50,50],mask=None, mapshape='planar', lattice='rect', normalization='var', initialization='pca', neighborhood='gaussian', training='batch', name='sompy')
som.train(n_job=1, verbose='info')

v = sompy.mapview.View2DPacked(100, 100, 'test', text_size=8)
v.show(som, what='codebook', cmap='jet', col_sz=6)
v.show(som, what='cluster')

h = sompy.hitmap.HitMapView(100,100, "Hit Map", text_size=8)
h.show(som)

u = sompy.umatrix.UMatrixView(100,100, "Matrix", text_size=8)
u.show(som)