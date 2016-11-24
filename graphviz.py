import matplotlib.pyplot as plt
import networkx as nx
G = nx.read_gpickle("graph.pickle")
for node in G.nodes():

    if len(G.neighbors(node)) < 2:
        G.remove_node(node)
nx.draw_networkx(G, labels=dict((n, d['name'].replace('$$', 'ss')) for n, d in G.nodes(data=True)))
plt.show()
