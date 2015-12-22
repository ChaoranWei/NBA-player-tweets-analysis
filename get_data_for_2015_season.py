import pickle
import datetime

'''This module extract all twitters from this season for all players, and store the dictionary
'''
data = pickle.load(open('pickle/wordvec.pkl'))

def getStringBeforeDate(string, date):
    if date == datetime.datetime(2015,12,19):
        return True
    elif str(date)[:9] in string:
        return string.split(str(date)[:9],1)[0] #heart of this module, get all texts before this given date string
    else:
        date += datetime.timedelta(days=1)
        return getStringBeforeDate(string, date) #recursive call to move on to the next date
        
date = datetime.datetime(2015,10,27)
this_season_twitter = {}

for i in data.keys():
    this_season_twitter[i] = getStringBeforeDate(data[i], date)
    print(i)

with open('pickle/this_season_twitter.pkl','w') as f:
    pickle.dump(this_season_twitter,f)
    print('saved')