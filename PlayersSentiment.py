import pickle
import numpy
import csv

f = open('AFINN.txt', 'r')
sentiment = {}
for line in f:
    line = line.lower().split()
    if len(line) > 2:
        temp = ['','']
        temp[0] = " ".join(line[:-1])
        temp[1] = line[-1]
        line = temp
    sentiment[line[0]] = int(line[1])

players_sentiment = {}
players = pickle.load(open('pickle/wordvec.pkl'))

for key, value in players.iteritems():
    print(key)
    value = value.lower().split()
    score = 0
    for i in value:
        if i in sentiment.keys():
            score = score + sentiment[i]  
    score = float(score)/len(value)*100
    print(score)
    players_sentiment[key] = score