# Creates completely pruned graph for a given artist

# Creates a collab graph around specified START_ARTIST, saves in graph.pickle
# Usage: python musicnet.py [MAX_ARTISTS=1000] [START_ARTIST='Drake']

# Import libraries
import networkx as nx
import re
import spotipy
import time
import sys
from Queue import Queue

# Get number of artists to scrape
MAX_ARTISTS = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
print('Running over ' + str(MAX_ARTISTS) + ' artists')

# Initialize number of requests and start time for logging purposes
requests = 0
start = time.time()

# Spotify client and graph
spotify = spotipy.Spotify()
G = nx.Graph()

# Start search
START_ARTIST = sys.argv[2] if len(sys.argv) > 2 else 'Drake'
results = spotify.search(q='artist:' + START_ARTIST, type='artist', limit=1)
artist = results['artists']['items'][0]
print artist

# Queue of artists nodes yet to be traversed
queue = Queue()
queue.put(artist['uri'])
G.add_node(artist['uri'], name=artist['name'], popularity=artist['popularity'])

# Artists that have been examined
artists_done = set()

# Albums that have been examined
albums_done = set()

# Do graph search
while len(artists_done) < MAX_ARTISTS:
    # Get next artist_uri (skip if already done)
    print(len(artists_done))
    artist_uri = queue.get()
    if artist_uri in artists_done:
        continue

    # Mark artist as analyzed
    try:
        G.node[artist_uri]['marked'] = True
    except KeyError:
        print("ERROR: skipping " + artist_uri)
    artists_done.add(artist_uri)

    # Get all albums/singles
    results = spotify.artist_albums(artist_uri, album_type='album,single', country='US')
    albums = results['items']
    requests += 1
    while results['next']:
        # Depaginate
        results = spotify.next(results)
        albums.extend(results['items'])

    # Filter albums/singles to unique
    real_albums = dict()
    for album in albums:
        # Strip extraneous characters
        name = re.sub(r'\([^)]*\)|\[[^)]*\]', '', album['name']) # remove (Deluxe edition) and [Feat. asdf] tags
        name = re.sub(r'\W','', name).lower().strip() # remove all non-alphanumerical characters
        if name not in real_albums:
            print('Adding ' + name)
            real_albums[name] = album

    # Analyze the albums of this artist
    for album in real_albums:
        if album not in albums_done:
            # Mark album as analyzed
            albums_done.add(album)
            print('\tAlbum: ' + real_albums[album]['name'])

            # Get tracks in this album
            results = spotify.album_tracks(real_albums[album]['id'])
            requests += 1
            tracks = results['items']
            while results['next']:
                results = spotify.next(results)
                tracks.extend(results['items'])

            # Get collaborating artists in each track
            for track in tracks:
                for artist in track['artists']:
                    if artist['uri'] != artist_uri:
                        print('\t\t' + artist['name'])
                        queue.put(artist['uri'])
                        if artist['uri'] not in G:
                            # Get detailed description of artist and create node
                            artist = spotify.artist(artist['uri'])
                            G.add_node(artist['uri'], name=artist['name'], popularity=artist['popularity'])
                            # Try adding artist's image
                            if len(artist['images']) > 0:
                                G.node[artist['uri']]['image_url'] = artist['images'][0]['url']
                            else:
                                G.node[artist['uri']]['image_url'] = "https://developer.spotify.com/wp-content/uploads/2016/07/icon1@2x.png"
                        # Count how many collaborations
                        try:
                            G[artist['uri']][artist_uri]['freq'] += 1
                        except KeyError:
                            G.add_edge(artist['uri'], artist_uri, freq=1)

# Print statistics
print('Collected ' + str(nx.number_of_nodes(G)) +' nodes in ' + str(time.time() - start) + ' seconds with ' + str(requests) + ' requests')
print(str(len(artists_done)) + ' artists analyzed')

# Keep only marked nodes
print('Keeping only marked nodes:')
for node, data in G.nodes(data=True):
    if 'marked' not in data:
        G.remove_node(node)
print(nx.info(G))

# Recursively remove all nodes with degree < 2
print('Recursively removing all nodes with degree < 2:')
for i in range(10):
    for node in G.nodes():
        if G.degree(node) < 2:
            G.remove_node(node)
print(nx.info(G))

# Save graph to pickle file
filename = sys.argv[3] if (len(sys.argv) > 3) else 'graphHist.pickle'

print('Saving graph to: ' + filename)
# Save graph
nx.write_gpickle(G, filename)
