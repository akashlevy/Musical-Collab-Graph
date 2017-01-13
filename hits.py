#Run hits algorithm
import matplotlib.pyplot as plt
import networkx as nx
import spotipy
import pylab

spotify = spotipy.Spotify()
GRAPHFILE = 'digraph_1000nodes' #name of graph you're reading in                                                                                                                
NUMRANKED = 15

G = nx.read_gpickle(GRAPHFILE + '.pickle')
H = nx.hits(G)

hubs = H[0]
auth = H[1] 

i = 1

print 'Top artists ranked by hub score'
print '==============================='

for k, v in sorted(hubs.items(), key=lambda t:t[1], reverse=True):
	artist = spotify.artist(k)
	print str(i) + '. ' + artist['name'] + ' {h: ' + str(v) + ', a: ' + str(auth[k]) + '}'
	i += 1
	if i > NUMRANKED:
		break

i = 1
print ''
print 'Top artists ranked by authority score'
print '==============================='

for k, v in sorted(auth.items(), key=lambda t:t[1], reverse=True):
	artist = spotify.artist(k)
	print str(i) + '. ' + artist['name'] + '{a: ' + str(v) + ', h: ' + str(hubs[k]) + '}'
	i += 1
	if i > NUMRANKED:
		break

