 
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
