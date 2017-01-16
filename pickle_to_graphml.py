import networkx as nx 

graphs = ['graph', 'graph2', 'graph3', 'graph4', 'digraph', 'digraph2', 'digraph3', 'digraph4']

for g in graphs:
	G = nx.read_gpickle('graph_pickles/' + g + '.pickle')
	nx.write_graphml(G, 'graph_graphmls/' + g + '.graphml')

