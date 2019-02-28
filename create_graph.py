import numpy as np
import networkx as nx
#from read_data import *
import read_data.py


array, im_inds = read_data.read_data("a_example.txt", True)
# array = read_data.read_data("a_example.txt")
ones = np.ones_like(array)
dot_prod = np.dot(array, array.T)
dot_ones = np.dot(ones, array.T)

del ones

score1 = dot_prod               #np.dot(array, array.T)
score2 = dot_ones - dot_prod    #np.dot(1-array, array.T)
score3 = dot_ones.T - dot_prod  #np.dot(array, 1 - array.T)

stack_the_layers = np.stack((score1, score2, score3), axis=-1)
adj = np.min(stack_the_layers, axis=-1)

G = nx.from_numpy_matrix(adj)
G = nx.maximum_spanning_tree(G)
G = G.to_directed()
slideshow = list(nx.dfs_preorder_nodes(G, source=0))

    # print(slideshow)
with open(args.input + '.out', 'w') as fid:
    fid.write(str(len(slideshow)) + '\n')
    for elem in slideshow:
        inds = im_inds[elem]
        if type(inds) == int:
            inds = [inds]
        inds = list(inds)
        inds = [str(x) for x in inds]
        fid.write(' '.join(inds) + '\n')

