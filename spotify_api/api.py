from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Conexión a la API de Spotify
def connect_to_spotify(client_id, client_secret):
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    ))

# Obtener información de un artista
def get_artist_info(sp, artist_name):
    results = sp.search(q=artist_name, type="artist", limit=1)
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        return {
            'name': artist['name'],
            'genres': artist['genres'],
            'followers': artist['followers']['total'],
            'popularity': artist['popularity'],
            'id': artist['id']  # Incluye el ID para obtener álbumes
        }
    return None

# Obtener álbumes de un artista
def get_artist_albums(sp, artist_id):
    albums = sp.artist_albums(artist_id, limit=10)['items']
    return [{'name': album['name'], 'id': album['id']} for album in albums]

# Obtener canciones de un álbum
def get_album_tracks(sp, album_id):
    tracks = sp.album_tracks(album_id)['items']
    return [{'name': track['name'], 'id': track['id']} for track in tracks]

# Obtener características de una canción
def get_track_features(sp, track_id):
    features = sp.audio_features(track_id)[0]
    if features:
        return {
            'danceability': features['danceability'],
            'energy': features['energy'],
            'tempo': features['tempo'],
            'valence': features['valence']
        }
    return None
