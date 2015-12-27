from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import csv

'''Author: yanofsky github: https://gist.github.com/yanofsky/5436496 with small modification
'''
def get_all_tweets(username):
	
    #authorize twitter, initialize tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = API(auth)
	
    #initialize a list to hold all the tweepy Tweets
    alltweets = []	
	
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = username,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
	
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
	
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
	print "getting tweets before %s" % (oldest)
		
	#all subsiquent requests use the max_id param to prevent duplicates
	new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
	#save most recent tweets
	alltweets.extend(new_tweets)
		
	#update the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
		
	print "...%s tweets downloaded so far" % (len(alltweets))
	
    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
    with open('player/%s_tweets.csv' % screen_name, 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["id","created_at","text"])
	writer.writerows(outtweets)
	
    pass

#This module borrows some basic tweet api code from http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#verification
access_key = "4514505875-yrTmZijaOfrw4xzxWDsVm6K4oq6f1C9xk03Cwah"
access_secret = "7wUuYou28qZo8SoiqtjSeh7kddy17wUlGkjFQnpI36bfT"
consumer_key = "WCHmxZWkcDjzXWts6dMKj4nL4"
consumer_secret = "2MevSHs5OsXMtajrJZBrx721kiVeOLP5rpvN8IDQPzQaYMwtcm"

        
if __name__ == '__main__':
    with open('playerlist.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
	    if row[0] != '':
		print(row[0])
	        get_all_tweets(row[0])
	        print('got ' + row[0] + ' tweets')