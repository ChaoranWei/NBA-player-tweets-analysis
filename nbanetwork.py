import json
import numpy as np
import networkx as nx
import requests
from pattern import web
import matplotlib.pyplot as plt
from matplotlib import rcParams

'''
This module is supposed to be a practice for network analysis inspired by one of
the project assigned in Harvard data science, so it borrows significantly from
the project solution. For the original code, please go to http://nbviewer.ipython.org/github/cs109/content/blob/master/HW5_solutions.ipynb
'''

dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.grid'] = False
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'none'

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecessary plot borders and axis ticks
    
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()
        
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import csv
import tweepy
import time
import pickle

access_key = "4514505875-yrTmZijaOfrw4xzxWDsVm6K4oq6f1C9xk03Cwah"
access_secret = "7wUuYou28qZo8SoiqtjSeh7kddy17wUlGkjFQnpI36bfT"
consumer_key = "WCHmxZWkcDjzXWts6dMKj4nL4"
consumer_secret = "2MevSHs5OsXMtajrJZBrx721kiVeOLP5rpvN8IDQPzQaYMwtcm"

def get_network_from_tweepy():
    '''Get network data from tweepy. http://stackoverflow.com/questions/26792734/get-all-friends-of-a-given-user-on-twitter-with-tweepy
    '''
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = API(auth)    
   # user = api.lookup_users(user_ids= [18004919, 1019195455])
   # for u in user:
   #     print(u.screen_name)
    
    full_dict = {}
    with open('playerlist.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        listofplayers = [row for row in reader]
        
        for row in listofplayers:
            print(row)
            ids = []
            for page in tweepy.Cursor(api.friends_ids, screen_name=row[0]).pages():
                ids.extend(page) 
            screen_names = {}
            for i in ids:
                user = api.lookup_users(user_ids= [i]) 
                for u in user:
                    if [u.screen_name] in listofplayers:
                        screen_names[u.screen_name] = 1
                        print(u.screen_name)
                time.sleep(5)
                
            #screen_names = {user.screen_name: 1 for user in api.lookup_users(user_ids= ids) 
            #                                           if user.screen_name in listofplayers}
            print(screen_names)
            full_dict[row[0]] = screen_names
        return full_dict, listofplayers
        
        
def _color(s):
    '''a function to make multicolor graph in network
    '''
    if 'E' in s:
        return 'r'
    if 'S' in s:
        return 'b'
    return 'k'
        
def draw_simple_network(data, players):
    g = nx.DiGraph()
    for node in players:
        g.add_node(node)
        g.node[node]['color'] = _color(node)
        
    for player1, neighbors in data.items():
        for player2, weight in neighbors.items():
            if weight == 0:
                continue
            g.add_edge(player1, player2, weight = weight, difference = 1./weight)
            
    print('ready to draw the network...')
    np.random.seed(1)
    
    color = [g.node[player]['color'] for player in g.nodes()]
    pos = nx.spring_layout(g, iterations = 200)
    
    nx.draw_networkx_edges(g, pos, alpha = .05)
    nx.draw_networkx_nodes(g, pos, node_color = color)
    lbls = nx.draw_networkx_labels(g, pos, alpha = 5, font_size = 8)
    
    plt.xticks([])
    plt.yticks([])
    remove_border(left = False, bottom = False)
    
    
if __name__ == '__main__':
    data, players = get_network_from_tweepy()
    pickle.dump(data, open('dict.pkl','wb'))
    pickle.dump(players, open('players.pkl','wb'))
    #draw_network(data, players)
    
    