# Import libraries
import matplotlib.pyplot as plt
import networkx as nx
import sys

# Load graph from pickle file
filename = sys.argv[1] if (len(sys.argv) > 1) else 'graph.pickle'
print('Reading file: ' + filename)
G = nx.read_gpickle(filename)
print(nx.info(G))

# Draw network with matplotlib
nx.draw_networkx(G, labels=dict((n, d['name'].replace('$$', 'ss')) for n, d in G.nodes(data=True)), font_color='c')
plt.show()
