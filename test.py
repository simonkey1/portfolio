import pandas as pd

# Cargar el DataFrame histórico
df_historico = pd.read_csv("df_final.csv")

# Extraer la columna spotify_track_uri y filtrar valores válidos
track_uris = df_historico['spotify_track_uri'].dropna()
valid_uris = track_uris[track_uris.str.startswith("spotify:track:")]

# Extraer solo los IDs de las canciones
track_ids = valid_uris.apply(lambda x: x.split(":")[-1])
print(f"Total de URIs válidos: {len(track_ids)}")
