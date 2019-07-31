import music
list_of_music = music.get_songs()
import matplotlib.pyplot as plt

tempo = []
hottness = []

for i in range(len(list_of_music)):
    alltempos = list_of_music[i]["song"]["tempo"]
    tempo.append(alltempos)

for i in range(len(list_of_music)):
    allhottness =  list_of_music[i]["artist"]["hotttnesss"]
    hottness.append(allhottness)
x = tempo
y = hottness
plt.plot(x, y)
plt.title("Hotness vs. Tempo")
plt.xlabel("Tempo")
plt.ylabel("Hottness")
plt.show()
