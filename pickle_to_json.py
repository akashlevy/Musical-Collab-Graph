import networkx as nx
from networkx.readwrite import json_graph
import sys
import json

filename = sys.argv[1] if (len(sys.argv) > 1) else 'graph.pickle';
print ('Reading file: ' + filename);
G = nx.read_gpickle(filename)

print(nx.info(G));
print('Pruning nodes with less than 2 neighbors')
for node in G.nodes():
    if len(G.neighbors(node)) < 2:
        G.remove_node(node)
print(nx.info(G));
# Convert to table
data = json_graph.node_link_data(G, dict(id='id', source='source', target='target', key='key'));

writefilename = sys.argv[2] if (len(sys.argv) > 2) else 'graph.json';
f = open(writefilename, 'w');
f.write(json.dumps(data));