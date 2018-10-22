#Dylan Cornelius and Matthew Smith
#CSC 546 - Articiial Intelligence
#date
#Term Project - r/randomactsofpizza

import os

path = os.path.dirname(os.path.realpath(__file__))

#convert json to csv?

lines = [line.rstrip('\n') for line in open(path + '\\train.json')]

for line in lines:
    print(line)
