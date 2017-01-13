# Convert pickle to json for visualization
# Usage: python pickle_to_json.py [GRAPHFILE=graph.pickle] [OUTFILE=graph.json]

# Import libraries
import json
import networkx as nx
import sys
from networkx.readwrite import json_graph

# Load graph from pickle file
filename = sys.argv[1] if (len(sys.argv) > 1) else 'graph.pickle'
print('Reading file: ' + filename)
G = nx.read_gpickle(filename)
print(nx.info(G))

# Convert to table
data = json_graph.node_link_data(G, dict(id='id', source='source', target='target', key='key'))

# Write JSON to file
writefilename = sys.argv[2] if (len(sys.argv) > 2) else 'graph.json'
with open(writefilename, 'w') as f:
    f.write(json.dumps(data))
