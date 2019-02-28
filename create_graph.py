import numpy as np
import networkx as nx
# import read_data
def some_func(filename):
    return 10*np.random.rand(80000, 100)

array = some_func("blala").astype('int')
# array = read_data.read_data("a_example.txt")

dot_prod = np.dot(array, array.T)
dot_ones = np.dot(1, array.T)

score1 = dot_prod               #np.dot(array, array.T)
score2 = dot_ones - dot_prod    #np.dot(1-array, array.T)
score3 = dot_ones.T - dot_prod  #np.dot(array, 1 - array.T)

stack_the_layers = np.stack((score1, score2, score3), axis=-1)
adj = np.min(stack_the_layers, axis=-1)

G = nx.from_numpy_matrix(adj)
G_directed = G.to_directed()
