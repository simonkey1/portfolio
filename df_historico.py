import pandas as pd

# Cargar el DataFrame
df_historico = pd.read_csv("df_final.csv")

# Convertir columna `ts` a tipo datetime
df_historico['ts'] = pd.to_datetime(df_historico['ts'])

# Crear una columna `year` a partir del timestamp
df_historico['year'] = df_historico['ts'].dt.year

# Filtrar filas con URIs válidas
df_historico = df_historico[df_historico['spotify_track_uri'].notnull()]
df_historico = df_historico[df_historico['spotify_track_uri'].str.startswith("spotify:track:")]

# Contar la cantidad de URIs por año
uris_por_año = df_historico.groupby('year')['spotify_track_uri'].count().reset_index()
uris_por_año.columns = ['year', 'count']
print(uris_por_año)
