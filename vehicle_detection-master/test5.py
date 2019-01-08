import math
import numpy as np
import sys

matrix = np.array([
        [0, 1, 1, 2, 3],
        [0, 0, 2, 3, 3],
        [0, 1, 2, 2, 3],
        [1, 2, 3, 2, 2],
        [2, 2, 3, 3, 2]], dtype=np.float32)

P = np.array([
        [2.5, 2.0, 0.75, 0],
        [2.0, 1.0, 2.25, 0.5],
        [0.75, 2.25, 7, 5.25],
        [0, 0.5, 5.25, 4]], dtype=np.float32)

#print matkok[3, 3]
EN = 0
Px = 0
Py = 0
MeanX = 0
MeanY = 0
StdevX = 0
StdevY = 0

for j in range(4):
    Px += P[0, j]

for i in range(4):
    Py += P[i, 0]

for i in range(4):
    for j in range(4):
        MeanX += i * P[i, j]

for j in range(4):
    for i in range(4):
        MeanY += j * P[i, j]

Mean = np.average(P)

for i in range(4):
    for j in range(4):
        StdevX += math.pow((i - (i * P[i, j])), 2)

for j in range(4):
    StdevX += P[0, j]

for i in range(4):
    for j in range(4):
        StdevY += math.pow((j - (j * P[i, j])), 2)

for i in range(4):
    StdevY += P[i, 0]

StdevX = math.sqrt(StdevX)
StdevY = math.sqrt(StdevY)

# Contras: (((i * j) * P[i, j]) - (MeanX * MeanY)) / (StdevX * StdevY)
# IDM: (1 / (1 + math.pow((i - j), 2))) * P[i, j]
# ENT: P[i, j] * math.log(P[i, j] + sys.float_info.epsilon, 2)

for i in range(4):
    for j in range(4):

        temp = math.pow((i - Mean), 2) * P[i, j]

        EN += temp
        #print EN


print "Px: {0} | Py: {1} | MeanX: {2} | MeanY: {3} | EN: {4}".format(Px, Py, MeanX, MeanY, EN)
print "StedvX: {0} | StedvY: {1}".format(StdevX, StdevY)