import pandas as pd
import plotly.express as px

def prepare_data(filepath_or_df):
    """
    Prepara los datos cargando y filtrando según el rango de fechas y formato.
    """
    # Si es un archivo, cárgalo. Si ya es un DataFrame, úsalo directamente.
    if isinstance(filepath_or_df, str):
        df = pd.read_csv(filepath_or_df)
    else:
        df = filepath_or_df

    # Renombrar columnas clave si existen
    if 'spotify_track_uri' in df.columns:
        df = df.rename(columns={
            'spotify_track_uri': 'id',
            'master_metadata_album_artist_name': 'artist',
            'master_metadata_track_name': 'song',
            'master_metadata_album_album_name': 'album',
            'ms_played': 'ms',
            'min_played': 'minutos',
            'genres': 'genres'
        })

    # Convertir 'fecha' a formato datetime
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    df['year'] = df['fecha'].dt.year

    # Filtrar por rango de fechas entre 2017 y 2024
    df = df[(df['fecha'] >= '2017-01-01') & (df['fecha'] <= '2024-12-31')]

    return df

def format_genres_column(df):
    """
    Separa la columna 'genres' en listas (arrays).
    """
    # Validar si la columna 'genres' está presente
    if 'genres' not in df.columns:
        raise ValueError("La columna 'genres' no está presente en el DataFrame.")
    
    # Asegurarnos de que todos los valores en 'genres' sean cadenas o NaN
    df['genres'] = df['genres'].apply(lambda x: x if isinstance(x, str) else "")

    # Convertir los géneros en listas
    df['genres_list'] = df['genres'].apply(lambda x: x.split(", ") if x else [])
    return df

def consolidate_genres_using_index(df):
    """
    Consolida los géneros usando el índice de la lista de géneros.
    """
    # Mapeo de subcategorías a categorías principales por índice
    genre_mapping = {
        0: {  # Índice 0
            'k-pop': 'k-pop',
            'reggaeton': 'urbano latino',
            'canadian pop': 'pop',
        },
        1: {  # Índice 1
            'k-pop boy group': 'k-pop',
            'k-pop girl group': 'k-pop',
            'trap latino': 'urbano latino',
        },
        2: {  # Índice 2
            'pop': 'pop',
            'urbano latino': 'urbano latino',
            'latin pop': 'pop',
        }
    }

    # Función para mapear géneros según índice
    def map_genre(genres_list):
        consolidated_genres = []
        for index, genre in enumerate(genres_list):
            if index in genre_mapping and genre in genre_mapping[index]:
                consolidated_genres.append(genre_mapping[index][genre])
            else:
                consolidated_genres.append(genre)  # Mantener sin cambios si no está en el mapping
        return list(set(consolidated_genres))  # Eliminar duplicados

    # Consolidar los géneros en una nueva columna
    df['consolidated_genres'] = df['genres_list'].apply(map_genre)
    return df

def calculate_genre_trends(df):
    """
    Calcula las tendencias de géneros en el tiempo agrupando por año.
    """
    # Expandir los géneros consolidados en filas
    df_exploded = df.explode('consolidated_genres')

    # Filtrar valores nulos
    df_exploded = df_exploded.dropna(subset=['consolidated_genres'])
    
    # Agrupar por año y género y contar ocurrencias
    genre_trends = df_exploded.groupby(['year', 'consolidated_genres']).size().reset_index(name='count')
    return genre_trends

def create_genre_trend_chart(genre_trends):
    """
    Crea un gráfico de líneas que muestra las tendencias de los géneros consolidados en el tiempo.
    """
    fig = px.line(
        genre_trends,
        x='year',
        y='count',
        color='consolidated_genres',
        title='Tendencias de Géneros Musicales por Año (2017-2024)',
        labels={'year': 'Año', 'count': 'Número de Canciones', 'consolidated_genres': 'Género'},
        markers=True
    )

    # Personalizar estilo del gráfico
    fig.update_layout(
        title={
            'text': 'Tendencias de Géneros Musicales por Año (2017-2024)',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis=dict(
            title='Año',
            title_font=dict(size=14, color='lightskyblue'),
            tickfont=dict(size=12, color='lightskyblue')
        ),
        yaxis=dict(
            title='Número de Canciones',
            title_font=dict(size=14, color='lightskyblue'),
            tickfont=dict(size=12, color='lightskyblue')
        ),
        legend=dict(
            x=0.5,
            xanchor='center',
            orientation='h'
        )
    )

    return fig

def save_chart(fig, filename="genre_trend_chart.png"):
    """
    Guarda el gráfico como una imagen PNG.
    """
    import kaleido
    fig.write_image(filename, width=800, height=800)
