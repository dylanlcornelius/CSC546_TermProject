import numpy as np
from matplotlib import pyplot as plt
from minisom import MiniSom
import sompy
# pip3 install git+https://github.com/compmonks/SOMPY.git

data = [[]]

'''
with open('PizzaFeatures.txt') as f:
    for line in f:
        current = line.replace('\n', '').split(',')
        thing = []
        thing.append(float(current[0]))
        thing.append(float(current[1]))
        data.append(thing)


data = [[ 0.80,  0.55,  0.22,  0.03],
        [ 0.82,  0.50,  0.23,  0.03],
        [ 0.80,  0.54,  0.22,  0.03],
        [ 0.80,  0.53,  0.26,  0.03],
        [ 0.79,  0.56,  0.22,  0.03],
        [ 0.75,  0.60,  0.25,  0.03],
        [ 0.77,  0.59,  0.22,  0.03]]
        '''

with open('PizzaFeatures.txt') as f:
    data = [line.replace('\n', '').split(',') for line in f]

data = np.array(data, dtype=float)

colors = ['blue', 'red']

#som2 = MiniSom(10,10,8, sigma=0.5, learning_rate=0.1)
#som2.train_random(data, 100)

'''
for line in data:
    for feat in line:
        print(feat)
    print()
'''

som = sompy.SOMFactory.build(data, mapsize=[100,100],mask=None, mapshape='planar', lattice='rect', normalization='var', initialization='pca', neighborhood='gaussian', training='batch', name='sompy')
#som = sompy.SOMFactory.build(data, mapsize=[10,10], normalization='var', initialization='pca')
som.train(n_job=1, verbose='info')

v = sompy.mapview.View2DPacked(50, 50, 'test', text_size=8)
#v.show(som, what='codebook', cmap='jet', col_sz=6)
v.show(som, what='cluster')

#plt.show()