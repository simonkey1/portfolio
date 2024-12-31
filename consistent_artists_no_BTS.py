import pandas as pd
import plotly.express as px

def prepare_data(filepath):
    """
    Prepara los datos cargando y filtrando según el rango de fechas y formato.
    """
    # Cargar los datos desde el archivo
    df_final = pd.read_csv(filepath)

    # Renombrar la columna 'master_metadata_album_artist_name' a 'artist'
    if 'master_metadata_album_artist_name' in df_final.columns:
        df_final = df_final.rename(columns={'master_metadata_album_artist_name': 'artist'})

    # Convertir 'ts' en formato datetime
    df_final['date'] = pd.to_datetime(df_final['ts'])

    # Extraer el año
    df_final['year'] = df_final['date'].dt.year

    # Eliminar zona horaria de 'date'
    df_final['date'] = df_final['date'].dt.tz_localize(None)

    # Calcular minutos reproducidos a partir de ms_played
    df_final['min_played'] = df_final['ms_played'] / 60000

    # Definir rango de fechas
    fecha_inicio = pd.Timestamp("2017-01-01")
    fecha_fin = pd.Timestamp("2024-12-29")

    # Filtrar el DataFrame dentro del rango de fechas
    df_filtrado = df_final[(df_final['date'] >= fecha_inicio) & (df_final['date'] <= fecha_fin)]

    return df_filtrado

def get_consistent_artists_with_playtime_excluding_bts(df, top_n=15):
    """
    Filtra los artistas más consistentes con años activos = 8, excluyendo a BTS, y selecciona el top N basado en minutos reproducidos.
    """
    # Contar en cuántos años aparece cada artista
    artist_years = df.groupby('artist')['year'].nunique().reset_index()
    artist_years = artist_years.rename(columns={'year': 'years_active'})

    # Filtrar artistas con años activos = 8
    consistent_artists = artist_years[artist_years['years_active'] == 8]

    # Calcular el total de minutos reproducidos por artista
    artist_playtime = df.groupby('artist')['min_played'].sum().reset_index()
    artist_playtime = artist_playtime.rename(columns={'min_played': 'total_min_played'})

    # Unir con los artistas consistentes
    consistent_artists = consistent_artists.merge(artist_playtime, on='artist')

    # Excluir a BTS
    consistent_artists = consistent_artists[consistent_artists['artist'] != 'BTS']

    # Ordenar por minutos reproducidos y tomar el top N
    top_artists = consistent_artists.sort_values(by='total_min_played', ascending=False).head(top_n)

    return top_artists

def create_consistency_chart_no_bts(filepath, top_artists):
    """
    Crea un gráfico de consistencia para los artistas más destacados excluyendo a BTS.
    """
    # Prepara los datos
    df_filtrado = prepare_data(filepath)

    # Obtener el número de apariciones de cada artista por año
    artist_year_data = df_filtrado.groupby(['artist', 'year'])['min_played'].sum().reset_index()

    # Filtrar los datos para incluir solo los artistas destacados
    filtered_data = artist_year_data[artist_year_data['artist'].isin(top_artists)]

    # Crear el gráfico interactivo
    fig = px.line(
        filtered_data,
        x='year',
        y='min_played',
        color='artist',
        title='Consistencia de Artistas Destacados (Excluyendo BTS)',
        labels={'year': 'Año', 'min_played': 'Minutos Reproducidos', 'artist': 'Artista'},
        markers=True
    )

    return fig
