import pandas as pd
from spotify_api.api import (
    connect_to_spotify,
    get_track_features,
    get_artist_info
)

# Configura tus credenciales
CLIENT_ID = "88ae7b7f86a249209a3afbc7e798fa13"
CLIENT_SECRET = "7fdbe5173c7d40cfab0708552f06b9fc"

# Conectar a la API de Spotify
sp = connect_to_spotify(CLIENT_ID, CLIENT_SECRET)

# Leer el archivo con datos históricos
df_historico = pd.read_csv("df_final.csv")

# Filtrar filas válidas


# Crear nuevas columnas para datos enriquecidos
df_historico['artist_genres'] = None
df_historico['artist_followers'] = None
df_historico['artist_popularity'] = None
df_historico['track_danceability'] = None
df_historico['track_energy'] = None
df_historico['track_tempo'] = None
df_historico['track_valence'] = None

        # Obtener características de la canción usando el URI
        # track_features = get_track_features(sp, row['spotify_track_uri'])
        # if track_features:
        #     df_historico.at[index, 'track_danceability'] = track_features['danceability']
        #     df_historico.at[index, 'track_energy'] = track_features['energy']
        #     df_historico.at[index, 'track_tempo'] = track_features['tempo']
        #     df_historico.at[index, 'track_valence'] = track_features['valence']


# Iterar sobre las filas para enriquecer los datos
for index, row in df_historico.iterrows():
    try:

        # Obtener información del artista
        artist_info = get_artist_info(sp, row['master_metadata_album_artist_name'])
        if artist_info:
            df_historico.at[index, 'artist_genres'] = ', '.join(artist_info['genres'])
            df_historico.at[index, 'artist_followers'] = artist_info['followers']
            df_historico.at[index, 'artist_popularity'] = artist_info['popularity']

    except Exception as e:
        print(f"Error procesando fila {index}: {e}")

# Guardar el DataFrame enriquecido
df_historico.to_csv("historico_enriquecido.csv", index=False)
print("Datos enriquecidos guardados en 'historico_enriquecido.csv'")
