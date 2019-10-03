import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import random as rd

graphListY = []
graphListX = []
colorList = []

with open("./1880-2017.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    contatore = 0
    for riga in csv_reader:
        if contatore > 4:
            print(riga)
            graphListX.append(int(riga[0]))
            graphListY.append(float(riga[1]))
            r = rd.random()
            g = rd.random()
            b = rd.random()
            rgb = (r,g,b)
            colorList.append(rgb)
        contatore = contatore + 1
        #for campo in riga:
print(graphListX)
print(graphListY)
#plt.plot(graphListX, graphListY)
plt.bar(graphListX, graphListY, edgecolor="black", color=colorList)
plt.xlabel("Anni")
plt.ylabel("Tmedia - Media")
plt.show()
