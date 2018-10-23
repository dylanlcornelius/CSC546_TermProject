#Dylan Cornelius and Matthew Smith
#CSC 546 - Articiial Intelligence
#date
#Term Project - r/randomactsofpizza

import os
import csv
from sklearn.feature_extraction.text import CountVectorizer

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '\\train.csv'

featFile = open(path + '\\PizzaFeatures.txt', 'w')


with open(dataFile, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader, None)
    for row in reader:
        featFile.write(repr((float(row[1])/ 0.000001 if float(row[2]) == 0 else float(row[2]))))
    #print(line)
    #number of up-doots/down-doots
    #text was edited
    #text
    #account age at request
    #days since first post