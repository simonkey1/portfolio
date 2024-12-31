from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


# Conectar a la API de Spotify
def connect_to_spotify(client_id, client_secret):
    """
    Conecta a la API de Spotify usando Spotipy.

    Args:
        client_id (str): Client ID de Spotify Developer.
        client_secret (str): Client Secret de Spotify Developer.

    Returns:
        sp (spotipy.Spotify): Cliente autenticado de Spotipy.
    """
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )) 

# Obtener características de una canción
def get_track_features(sp, track_id):
    """
    Obtiene las características de audio de un track por su ID.

    Args:
        sp (spotipy.Spotify): Cliente de Spotipy autenticado.
        track_id (str): ID único del track.

    Returns:
        dict: Características de la canción (danceability, energy, tempo, valence).
    """
    try:
        features = sp.audio_features([track_id])  # El método acepta una lista de IDs
        if features and features[0]:
            return {
                'danceability': features[0]['danceability'],
                'energy': features[0]['energy'],
                'tempo': features[0]['tempo'],
                'valence': features[0]['valence']
            }
    except Exception as e:
        print(f"Error obteniendo características del track {track_id}: {e}")
    return None


# Obtener información de un artista
def get_artist_info(sp, artist_name):
    """
    Busca un artista por nombre y obtiene su información.

    Args:
        sp (spotipy.Spotify): Cliente de Spotipy autenticado.
        artist_name (str): Nombre del artista.

    Returns:
        dict: Información del artista (géneros, seguidores, popularidad).
    """
    try:
        results = sp.search(q=artist_name, type="artist", limit=1)
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            return {
                'name': artist['name'],
                'genres': artist['genres'],
                'followers': artist['followers']['total'],
                'popularity': artist['popularity']
            }
    except Exception as e:
        print(f"Error obteniendo información del artista {artist_name}: {e}")
    return None

# Función auxiliar: Verificar formato de URI
def is_valid_track_uri(uri):
    """
    Verifica si un URI tiene el formato correcto para una canción.

    Args:
        uri (str): URI de la canción.

    Returns:
        bool: True si es válido, False en caso contrario.
    """
    return isinstance(uri, str) and uri.startswith("spotify:track:")


def get_track_details(sp, track_id):
    """
    Obtiene detalles de un track, como nombre, artista y álbum.

    Args:
        sp (spotipy.Spotify): Cliente de Spotipy autenticado.
        track_id (str): ID único del track.

    Returns:
        dict: Información del track (nombre, artista, álbum).
    """
    try:
        track = sp.track(track_id)
        return {
            'track_name': track['name'],
            'artist_name': track['artists'][0]['name'],
            'album_name': track['album']['name']
        }
    except Exception as e:
        print(f"Error obteniendo detalles del track {track_id}: {e}")
    return None
