import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.clique import find_cliques
G = nx.read_gpickle("graph.pickle")
print len(G.nodes()), len(G.edges())
for clique in [[G.node[node]['name'] for node in clique] for clique in sorted(find_cliques(G), key=len, reverse=True)]:
    print len(clique), clique
