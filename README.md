# A musical collaboration graph
Understanding musical collaborations via graph-based analysis

## Dependencies
- [Python 2.7](https://www.python.org/)
- [Numpy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/)
- [NetworkX](https://networkx.github.io/)
- [Spotipy](https://spotipy.readthedocs.io/en/latest/)

## Methodology
Song data is fetched from Spotify's web API

Graph analysis
- (Erica) Calculate pagerank importance vectors, digraph based analysis
- (Daniel) Hub/centrality measures, clustering coefficient
- (Vincent) Metric based influence: Most collabs, 
- (Akash) Clique analysis / Almost fully connected

Visualization
- Neo4J
- (Akash) Options to search up selected cliques
- (Sunny) Distance based plot from a starting node
