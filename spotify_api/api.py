 
# spotify_api/api.py
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Configuración de la API
def connect_to_spotify(client_id, client_secret):
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    ))

# Ejemplo: buscar información de un artista
def get_artist_info(sp, artist_name):
    results = sp.search(q=artist_name, type="artist", limit=1)
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        return {
            'name': artist['name'],
            'genres': artist['genres'],
            'followers': artist['followers']['total'],
            'popularity': artist['popularity']
        }
    return None

def get_track_features(sp, track_name):
    results = sp.search(q=track_name, type="track", limit=1)
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        features = sp.audio_features(track_id)[0]
        return {
            'danceability': features['danceability'],
            'energy': features['energy'],
            'tempo': features['tempo'],
            'valence': features['valence']
        }
    return None