# Creates pruned graphs

# Import libraries
import networkx as nx
import sys

# Load graph from pickle file
filename = 'graph.pickle'
print('Reading file: ' + filename)
G = nx.read_gpickle(filename)
print(nx.info(G))

# Recursively remove all nodes with degree < 2
print('Recursively removing all nodes with degree < 2:')
for i in range(10):
    for node in G.nodes():
        if G.degree(node) < 2:
            G.remove_node(node)
print(nx.info(G))

# Save graph to pickle file
filename = 'graph2.pickle'
print('Saving graph to: ' + filename)
nx.write_gpickle(G, filename)

# Reload original graph from pickle file
filename = 'graph.pickle'
print ('Reading file: ' + filename)
G = nx.read_gpickle(filename)
print(nx.info(G))

# Keep only marked nodes
print('Keeping only marked nodes:')
for node, data in G.nodes(data=True):
    if 'marked' not in data:
        G.remove_node(node)
print(nx.info(G))

# Save graph to pickle file
filename = 'graph3.pickle'
print('Saving graph to: ' + filename)
nx.write_gpickle(G, filename)

# Recursively remove all nodes with degree < 2
print('Recursively removing all nodes with degree < 2:')
for i in range(10):
    for node in G.nodes():
        if G.degree(node) < 2:
            G.remove_node(node)
print(nx.info(G))

# Save graph to pickle file
filename = 'graph4.pickle'
print('Saving graph to: ' + filename)
nx.write_gpickle(G, filename)
