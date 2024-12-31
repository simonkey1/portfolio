


import pandas as pd
import time
from spotify_api.api import connect_to_spotify, get_track_details

# Configura tus credenciales
CLIENT_ID = "88ae7b7f86a249209a3afbc7e798fa13"
CLIENT_SECRET = "7fdbe5173c7d40cfab0708552f06b9fc"

# Conectar a la API
sp = connect_to_spotify(CLIENT_ID, CLIENT_SECRET)

# Verificar conexión
print("Conexión exitosa. Probando acceso a Spotify...")
try:
    result = sp.search(q="test", type="track", limit=1)
    print("Prueba de conexión exitosa. La API está activa.")
except Exception as e:
    print(f"Error al conectar con la API: {e}")
    exit()

# Cargar el DataFrame histórico
df_historico = pd.read_csv("df_final.csv")

# Extraer la columna spotify_track_uri y filtrar valores válidos
track_uris = df_historico['spotify_track_uri'].dropna()
valid_uris = track_uris[track_uris.str.startswith("spotify:track:")]

# Extraer solo los IDs de las canciones
track_ids = valid_uris.apply(lambda x: x.split(":")[-1])
print(f"Total de URIs válidos: {len(track_ids)}")

# Crear un nuevo DataFrame para almacenar los resultados
track_data = []

# Iterar sobre los track IDs
for index, track_id in enumerate(track_ids[:50]):  # Limitar a 50 para pruebas
    try:
        print(f"Procesando track {index + 1} de {len(track_ids)}: {track_id}")
        track_details = get_track_details(sp, track_id)
        if track_details:
            track_data.append({
                'track_id': track_id,
                'track_name': track_details['track_name'],
                'artist_name': track_details['artist_name'],
                'album_name': track_details['album_name']
            })
        # Retraso entre solicitudes
        time.sleep(0.1)
    except Exception as e:
        print(f"Error al procesar track {track_id}: {e}")

    # Guardar resultados intermedios cada 10 iteraciones
    if index % 10 == 0:
        pd.DataFrame(track_data).to_csv("track_details_temp.csv", index=False)

# Guardar el resultado final
df_tracks = pd.DataFrame(track_data)
df_tracks.to_csv("track_details.csv", index=False)
print("Datos guardados en 'track_details.csv'")
