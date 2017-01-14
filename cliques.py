# Find cliques within the collab graph saved in graph.pickle

# Import libraries
import networkx as nx
from networkx.algorithms.clique import find_cliques

# Find cliques
G = nx.read_gpickle('graph.pickle')
sorted_cliques = sorted(find_cliques(G), key=len, reverse=True)
for clique in [[G.node[node]['name'] for node in clique if 'name' in G.node[node] ] for clique in sorted_cliques]:
    print len(clique), clique
