#Rank artists according to the pagerank algorithm

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.link_analysis import pagerank
import spotipy

spotify = spotipy.Spotify()
GRAPHFILE = 'graph' #name of graph you're reading in

G = nx.read_gpickle(GRAPHFILE + '.pickle')
ranked = pagerank(G)
i = 1

#print artist name, pagerank influence, and spotify popularity
for k, v in sorted(ranked.items(), key=lambda t: t[1], reverse=True):
	artist = spotify.artist(k)
	print str(i) + '. ' + artist['name'] + ': ' + str(v) + ' (' + str(artist['popularity']) + ')'
	i += 1
