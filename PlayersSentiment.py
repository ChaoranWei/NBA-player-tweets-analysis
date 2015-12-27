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
players_words = {}
players_level = {}
players = pickle.load(open('pickle/this_season_twitter.pkl'))

for key, value in players.iteritems():
    print(key)
    if value == True:
        continue
    value = value.lower().split()
    score = 0
    temp1 = []
    temp2 = []
    for i in value:
        if i in sentiment.keys():
            score = score + sentiment[i] 
            temp1.append(i)
            temp2.append(sentiment[i])
            
    score = float(score)/len(value)*100
    print(score)
    players_sentiment[key] = score
    players_words[key] = temp1
    players_level[key] = temp2
    
    with open('pickle/season_playersentiment.pkl','w') as f:
        pickle.dump(players_sentiment,f)
        print('saved')
    
'''
    
with open('pickle/playersentiment.pkl','w') as f:
    pickle.dump(players_sentiment,f)
    print('saved')
    
with open('pickle/playerwords.pkl','w') as f:
    pickle.dump(players_words,f)
    print('saved')
with open('pickle/playerlevel.pkl','w') as f:
    pickle.dump(players_level,f)
    print('saved')
    
#THis is a dictionary with key as player id and sentiment as value
'''