import matplotlib.pyplot as plt
import pickle

data = pickle.load(open('pickle/playersentiment.pkl'))
season_data = pickle.load(open('pickle/season_playersentiment.pkl'))

plt.title('Derrick Rose\'s emotion overall and this season')

plt.bar([0,1],[float(data['drose']), float(season_data['drose'])], color="r",
align="center", width = 0.3)
plt.xticks([0,1],['before','this season'])
plt.show()