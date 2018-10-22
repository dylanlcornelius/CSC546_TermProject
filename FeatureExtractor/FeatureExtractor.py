#Dylan Cornelius and Matthew Smith
#CSC 546 - Articiial Intelligence
#date
#Term Project - r/randomactsofpizza

import os
from sklearn.feature_extraction.text import CountVectorizer

path = os.path.dirname(os.path.realpath(__file__))

#convert json to csv?

lines = [line.rstrip('\n') for line in open(path + '\\train.csv')]

for line in lines:
    print(line)
    #number of up-doots/down-doots
    #text was edited
    #text