# Metrics

# Import libraries
import networkx as nx
import re
from Queue import Queue
import time
import sys
import matplotlib.pyplot as plt

G = nx.read_gpickle('graph.pickle')

#print(G.nodes())

nx.bfs_tree(G, 'spotify:artist:3TVXtAsR1Inumwj472S9r4')

nx.write_gpickle(G, 'draketree.pickle')

try:
    from networkx import graphviz_layout
except ImportError:
    raise ImportError("This example needs Graphviz and either PyGraphviz or Pydot")

pos=nx.graphviz_layout(G,labels=dict((n, d['name'].replace('$$', 'ss')) for n, d in G.nodes(data=True)))
plt.figure(figsize=(8,8))
nx.draw(G,pos,labels=dict((n, d['name'].replace('$$', 'ss')) for n, d in G.nodes(data=True)),node_size=20,alpha=0.5,node_color="blue")
plt.axis('equal')
#plt.savefig('circular_tree.png')
plt.show()