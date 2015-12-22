#import pandas as pd
from os import listdir
import csv
import nltk
from nltk.corpus import stopwords
import re
import pickle

'''This module inputs csv from player's twitters and get a dictionary containing 
all words from their tweets
'''

def tweet2words(raw):
    letter_factorial = re.sub("[^a-zA-Z!0-9:-]", " ", raw)
    words = letter_factorial.lower().split()
    stops = set(stopwords.words("english"))                  
    meaningful_words = [w for w in words if (not w in stops)]    
    return meaningful_words

Dir = listdir('player')
player = {}
for i in Dir:
    with open('player/' + i, 'rU') as csvfile:
        print('processing ' + i + '...')
        reader = csv.reader(csvfile, delimiter=',', quoting = 3)
        all_tweets = []
        for row in reader:
            row = " ".join(row)
            all_tweets.extend(tweet2words(row))
            
        
        all_tweet = " ".join(all_tweets)
        player[i[:-11]] = all_tweet 
        
with open('pickle/wordvec.pkl','w') as f:
    pickle.dump(player,f)
    print('saved')
#This is a dictionary with player id as name an a big string as value
