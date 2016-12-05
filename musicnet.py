# Creates a collab graph for the specified START_ARTIST and saves it in graph.pickle

# Import libraries
import networkx as nx
import re
import spotipy
from queue import Queue

# Spotify client and graph
spotify = spotipy.Spotify()
G = nx.Graph()

# Start search
START_ARTIST = 'Drake'
results = spotify.search(q='artist:' + START_ARTIST, type='artist', limit=1)
artist = results['artists']['items'][0]
queue = Queue()
queue.put(artist['uri'])
G.add_node(artist['uri'], name=artist['name'])
artists_done = set()

# Do graph search
MAX_ARTISTS = 1000
while len(artists_done) < MAX_ARTISTS:
    # Get artist_uri
    print((len(artists_done)))
    artist_uri = queue.get()
    if artist_uri in artists_done:
        continue
    artists_done.add(artist_uri)

    # Get all albums/singles
    results = spotify.artist_albums(artist_uri, album_type='album,single', country='US')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    # Filter albums/singles to unique
    real_albums = []
    albums_seen = []
    for album in albums:
        name = re.sub(r'\([^)]*\)', '', album['name']).strip()
        if name not in albums_seen:
            albums_seen.append(name)
            real_albums.append(album)

    # Get tracks in albums
    for album in real_albums:
        results = spotify.album_tracks(album['id'])
        tracks = results['items']
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])

        # Get collaborating artists in each track
        for track in tracks:
            for artist in track['artists']:
                if artist['uri'] != artist_uri:
                    print((artist['name']))
                    queue.put(artist['uri'])
                    if artist['uri'] not in G:
                        G.add_node(artist['uri'], name=artist['name'])
                    try:
                        G[artist['uri']][artist_uri]['freq'] += 1
                    except KeyError:
                        G.add_edge(artist['uri'], artist_uri, freq=1)

# Save graph
nx.write_gpickle(G, 'graph.pickle')
