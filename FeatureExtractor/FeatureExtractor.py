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
    #i = 2
    sumUp = 0
    sumDown = 0
    avg = 0
    sumUp2 = 0
    sumDown2 = 0
    avg2 = 0
    for row in reader:
        # number of up-doots/down-doots
        if row[22] == 'TRUE':
            sumUp += float(row[2])
            sumDown += float(row[1])
            avg += 1
        else:
            sumUp2 += float(row[2])
            sumDown2 += float(row[1])
            avg2 += 1

        featFile.write(repr(float(row[1])) + ',')
        featFile.write(repr(float(row[2])) + ',')

        #text was edited
        '''
        appended = 0
        if row[3] == 'TRUE':
            appended = 1
        featFile.write(repr(appended) + ',')
        '''

        #number of comments
        featFile.write(repr(float(row[5])) + ',')
        #account age at request
        featFile.write(repr(float(row[9])) + ',')
        #days since first post on raop
        featFile.write(repr(float(row[11])) + ',')
        #number of comments in raop
        featFile.write(repr(float(row[15])) + ',')
        #number of posts in raop
        featFile.write(repr(float(row[19])) + ',')
        #up-doots - down-doots: karma
        featFile.write(repr(float(row[23])))

        #print(row[6])
        #text = ['Hi bb cc', 'cc dd ee', row[6]]
        #count_vect = CountVectorizer()
        #counts = count_vect.fit_transform(text)
        #print(counts.shape)
        #print(count_vect.vocabulary_.get(u'Hi'))

        featFile.write('\n')

'''
    print(avg)
    print(avg2)
    print()
    print(sumUp/avg)
    print(sumUp2/avg2)
    print()
    print(sumDown/avg)
    print(sumDown2/avg2)
'''
    #text
    #account age at request
    #days since first post