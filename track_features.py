import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from time import sleep

# Configuración de autenticación
client_id = "TU_CLIENT_ID"
client_secret = "TU_CLIENT_SECRET"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Obtener el Top 15 de artistas
def get_top_15_artists(df):
    """
    Obtiene el Top 15 de artistas más escuchados en términos de minutos reproducidos.
    """
    df['minutos'] = df['ms'] / 60000  # Calcular minutos reproducidos
    top_artists = (
        df.groupby('artist')['minutos']
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )
    return top_artists

# Filtrar por los Top 15 artistas
def filter_top_15_songs(df, top_15_artists):
    """
    Filtra las canciones que pertenecen a los Top 15 artistas.
    """
    filtered_df = df[df['artist'].isin(top_15_artists['artist'])]
    # Eliminar duplicados basados en 'song' y 'artist'
    filtered_df = filtered_df.drop_duplicates(subset=['song', 'artist']).reset_index(drop=True)
    return filtered_df

# Obtener géneros del artista desde Spotify
def get_artist_genres(artist_name):
    """
    Obtiene los géneros asociados a un artista.
    """
    try:
        results = sp.search(q=f"artist:{artist_name}", type="artist", limit=1)
        if results['artists']['items']:
            return results['artists']['items'][0]['genres']
        else:
            return []
    except Exception as e:
        print(f"Error al obtener géneros para {artist_name}: {e}")
        return []

# Procesar géneros para un DataFrame (sin límite)
def process_artist_genres(df, progress_callback=None):
    """
    Procesa los géneros para los artistas en el DataFrame.
    """
    total_artists = len(df)
    processed_artists = 0
    genres_list = []

    for _, row in df.iterrows():
        genres = get_artist_genres(row['artist'])

        if genres:
            genres_list.append({
                'song': row['song'],
                'artist': row['artist'],
                'album': row['album'],
                'ms': row['ms'],
                'genres': ", ".join(genres)  # Combinar géneros en una cadena separada por comas
            })

        processed_artists += 1
        if progress_callback:
            progress_callback(processed_artists, total_artists)

        # Pausa para evitar exceder los límites de la API
        sleep(0.2)

    # Crear un DataFrame con los géneros
    genres_df = pd.DataFrame(genres_list)

    # Eliminar duplicados basados en 'song' y 'artist'
    genres_df = genres_df.drop_duplicates(subset=['song', 'artist']).reset_index(drop=True)

    return genres_df
