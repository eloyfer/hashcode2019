import numpy as np
import networkx as nx

def some_func(filename):
    return np.random.rand(80000, 100)

array = some_func("blala")

score1 = np.dot(array, array.T)
score2 = np.dot(1-array, array.T)
score3 = np.dot(array, 1 - array.T)

stack_the_layers = np.stack((score1, score2, score3), axis=-1)
adj = np.min(stack_the_layers, axis=-1)

G = nx.from_numpy_matrix(adj)
G_directed = G.to_directed()
