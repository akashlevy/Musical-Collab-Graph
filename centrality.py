# Rank artists according to the degree centrality algorithm
# Usage: python centrality.py [GRAPHFILE=graph.pickle]

# Import libraries
import networkx as nx
import sys
from networkx.algorithms.centrality import degree_centrality, closeness_centrality, betweenness_centrality, eigenvector_centrality
from networkx.algorithms.link_analysis import pagerank
import spotipy 

# Load graph from pickle file
filename = sys.argv[1] if (len(sys.argv) > 1) else 'graph.pickle'
print('Reading file: ' + filename)
G = nx.read_gpickle(filename)
print(nx.info(G))

# Spotify API
spotify = spotipy.Spotify()

# Get different centrality measures
for measure in [degree_centrality, closeness_centrality, betweenness_centrality, eigenvector_centrality, pagerank]:
    # Display which measure
    print(measure.__name__)
    centralities = measure(G)

    # Print artist name, centrality, and Spotify popularity
    i = 1
    for k, v in sorted(centralities.items(), key=lambda t: t[1], reverse=True):
        print str(i) + '. ' + G.node[k]['name'] + ': ' + str(v) + ' (' + str(spotify.artist(k)['popularity']) + ') degree: ' + str(G.degree(k))
        i += 1
        if i > 10:
            break
