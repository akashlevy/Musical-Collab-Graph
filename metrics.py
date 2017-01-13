# Metrics

# Import libraries
import networkx as nx
import re
from Queue import Queue
import time
import sys
import matplotlib.pyplot as plt
import numpy as np

G = nx.read_gpickle('graph.pickle')

print("Number of nodes in graph:")
print(nx.number_of_nodes(G))

shortestPathLengths = nx.shortest_path_length(G, source ='spotify:artist:3TVXtAsR1Inumwj472S9r4')

distances = shortestPathLengths.values()

histogram = [0] * 10
# Calculate distances
for i in range(len(distances)):
	histogram[distances[i]] += 1

print histogram

print(len(shortestPathLengths))


G = nx.read_gpickle('beethoven.pickle')

# Create tree of nodes to display in html
beethovenTree = nx.bfs_tree(G, source = 'spotify:artist:2wOqMjp9TyABvtHdOSOTUS')

# Output as a pickle file
nx.write_gpickle(beethovenTree, 'beethovenTree.pickle')

G = nx.read_gpickle('beethovenTree.pickle')

print("Is this a tree?")
print(nx.is_tree(G))

print(nx.info(G));
nx.draw_networkx(G)
plt.show()










