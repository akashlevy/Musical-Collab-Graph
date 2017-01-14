#Rank artists according to the degree centrality algorithm                                                                                                                   

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.centrality import degree_centrality
from networkx.algorithms.approximation.clustering_coefficient import average_clustering
import spotipy
import pylab

spotify = spotipy.Spotify()
GRAPHFILE = 'graph4' #name of graph you're reading in                                                                                                                

G = nx.read_gpickle(GRAPH + 'pickle')
ranked = degree_centrality(G)
i = 1

# print average clustering coefficient
print "Average Clustering Coefficient: ", nx.average_clustering(G)


#print artist name, pagerank influence, and spotify popularity                                                                                                      
for k, v in sorted(ranked.items(), key=lambda t: t[1], reverse=True):
        artist = spotify.artist(k)
        print str(i) + '. ' + artist['name'] + ': ' + str(v) + ' (' + str(artist['popularity']) + ') degree: ' + str(G.degree(k))
        i += 1




