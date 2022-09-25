import time
import numpy as np
import matplotlib.pyplot as plt

vector = np.genfromtxt('start.dat')
matrixDefault = np.zeros([len(vector), len(vector)])
matrixDefault[0][0] = 1
matrixDefault[0][len(vector)-1] = -1
for i in range(1, len(vector)):
    matrixDefault[i][i] = 1
    matrixDefault[i][i-1] = -1

def changeGraph_by_Matrix(vector, matrix):
    return vector - matrix.dot(vector)/2
plt.ion()
for i in range(255):
    vector = changeGraph_by_Matrix(vector, matrixDefault)
    plt.clf()
    plt.plot(vector)
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.2)
plt.ioff()
plt.show()
