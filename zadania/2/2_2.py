import numpy as np

data = np.genfromtxt('data.csv', delimiter=';')

edin = np.eye(data.shape[0])

result = data.dot(edin)

np.savetxt('result.csv', result, delimiter=';')
