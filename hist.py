import pickle
import matplotlib.pyplot as plt
print('load data...')
data = pickle.load(open('pickle/playerlevel.pkl'))

print('drawing histogram...')

plt.hist(data['KingJames'])
plt.title("Lebron James Emotion Histogram")
plt.xlabel("key words")
plt.ylabel('frequency')
plt.show()