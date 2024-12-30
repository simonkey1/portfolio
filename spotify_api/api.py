 
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
    try:
        # Busca la canción por nombre
        results = sp.search(q=track_name, type="track", limit=1)
        if not results['tracks']['items']:
            return None  # Canción no encontrada

        # Obtiene el ID de la canción
        track_id = results['tracks']['items'][0]['id']

        # Recupera las características de la canción
        features = sp.audio_features(track_id)
        if features and features[0]:
            return {
                'danceability': features[0]['danceability'],
                'energy': features[0]['energy'],
                'tempo': features[0]['tempo'],
                'valence': features[0]['valence']
            }
        return None  # Si no hay características disponibles
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error al obtener características de la canción: {e}")
        return None
