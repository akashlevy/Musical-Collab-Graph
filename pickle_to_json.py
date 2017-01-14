# Convert pickle to json for visualization
# Usage: python pickle_to_json.py [GRAPHFILE=graph.pickle] [OUTFILE=graph.json]

# Import libraries
import json
import networkx as nx
from networkx.readwrite import json_graph
from os import listdir
import os.path

def pickle_to_json(source_file='graph.pickle', dest_file='graph.json'):
    # Load graph from pickle file
    print('Reading file: ' + source_file)
    G = nx.read_gpickle(source_file)
    print(nx.info(G))
    
    # Convert to table
    data = json_graph.node_link_data(G, dict(id='id', source='source', target='target', key='key'))
    
    # Write JSON to file
    print('Writing to: ' + dest_file);
    with open(dest_file, 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    import sys
    # Generates jsons for all .pickles files in specified directory
    # Usage: python plot_all.py directory_name
    if len(sys.argv) == 0:
        pickle_to_json();
    
    directory_name = sys.argv[1];
    
    # Make figures for all files
    files = [];
    for f in listdir(directory_name):
        file_path = os.path.join(directory_name, f);
        if os.path.isfile(file_path) and file_path.endswith('.pickle'):
            files.append(file_path);
            print('====== ' + f + ' ======');
            pickle_to_json(file_path, file_path[:-7]+'.json');