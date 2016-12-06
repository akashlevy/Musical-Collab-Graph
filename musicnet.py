# Creates a collab graph for the specified START_ARTIST and saves it in graph.pickle

# Import libraries
import networkx as nx
import re
import spotipy
from Queue import Queue
import time
import sys

start = time.time()
MAX_ARTISTS = int(sys.argv[1]) if (len(sys.argv) > 1) else 100;
print ('Running over ' + str(MAX_ARTISTS) + ' artists');

# Spotify client and graph
spotify = spotipy.Spotify()
G = nx.Graph()

# Start search
START_ARTIST = 'Drake'
results = spotify.search(q='artist:' + START_ARTIST, type='artist', limit=1)
artist = results['artists']['items'][0]

# Queue of artists nodes yet to be traversed
queue = Queue()
queue.put(artist['uri'])
G.add_node(artist['uri'], name=artist['name'])

# Artists that have been examined
artists_done = set()

# Do graph search
while len(artists_done) < MAX_ARTISTS:
    # Get next artist_uri
    print((len(artists_done)))
    artist_uri = queue.get();
    if artist_uri in artists_done:
        continue;
        
    # Mark artist as analyzed
    artists_done.add(artist_uri)

    # Get all albums/singles
    results = spotify.artist_albums(artist_uri, album_type='album,single', country='US')
    albums = results['items']
    while results['next']:
        # Depaginate
        results = spotify.next(results)
        albums.extend(results['items'])

    # Filter albums/singles to unique
    real_albums = dict()
    for album in albums:
        # Strip extraneous characters
        name = re.sub(r'\([^)]*\)', '', album['name']) # Remove (Deluxe edition) tags
        name = re.sub(r'\[[^)]*\]', '', name) # Remove [Feat. asdf] tags
        name = re.sub(r'\W','', name).lower().strip() # Remove all non-alphanumerical characters
        if name not in real_albums:
            print('Adding ' + name);
            real_albums[name] = album;

    # Get tracks in albums
    for album in real_albums:
        print('\tAlbum: ' + real_albums[album]['name']);
        results = spotify.album_tracks(real_albums[album]['id'])
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
                        G.add_node(artist['uri'], name=artist['name'])
                    try:
                        G[artist['uri']][artist_uri]['freq'] += 1
                    except KeyError:
                        G.add_edge(artist['uri'], artist_uri, freq=1)

print('Collected ' + str(nx.number_of_nodes(G)) +' nodes in ' + str(time.time() - start) + ' seconds');

# Save graph
nx.write_gpickle(G, 'graph.pickle')