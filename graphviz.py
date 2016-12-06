import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.clique import find_cliques
import sys

filename = sys.argv[1] if (len(sys.argv) > 1) else 'graph.pickle';
print ('Reading file: ' + filename);
	
G = nx.read_gpickle(filename)
print(nx.info(G));

for node in G.nodes():
    if len(G.neighbors(node)) < 2:
        G.remove_node(node)
nx.draw_networkx(G, labels=dict((n, d['name'].replace('$$', 'ss')) for n, d in G.nodes(data=True)), font_color='c')
plt.show()
