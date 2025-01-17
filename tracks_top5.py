import pandas as pd
import plotly.express as px
import streamlit as st

def prepare_track_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['ts'])
    df['year'] = df['date'].dt.year
    df['min_played'] = df['ms_played'] / 60000
    return df

def get_top_tracks(df, artist, year, top_n=5):
    filtered_data = df[(df['artist'] == artist) & (df['year'] == year)]
    top_tracks = filtered_data.groupby('song')['min_played'].sum().reset_index()
    top_tracks = top_tracks.sort_values(by='min_played', ascending=False).head(top_n)
    return top_tracks

def split_long_text(text, max_length=20):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= max_length:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word) + 1

    lines.append(" ".join(current_line))
    return "\n".join(lines)

def create_track_chart(filepath, year, artist):
    """
    Crea un gráfico de barras que muestre el top 5 de canciones más escuchadas
    para un artista seleccionado en un año específico, ajustando el rango del eje Y.
    """
    # Preparar los datos
    df = prepare_track_data(filepath)
    top_tracks = get_top_tracks(df, artist, year)

    # Dividir nombres largos de canciones
    top_tracks['song'] = top_tracks['song'].apply(lambda x: split_long_text(x, max_length=20))

    # Calcular un margen adicional para el eje Y
    y_max = top_tracks['min_played'].max() * 1.1  # Aumentar el rango en un 10%

    # Crear el gráfico de barras
    fig = px.bar(
        top_tracks,
        x='song',
        y='min_played',
        title=f"Top 5 Canciones de {artist} en {year}",
        labels={'song': 'Canción', 'min_played': 'Minutos Reproducidos'},
        text='min_played'
    )

    # Personalizar el diseño del gráfico
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(
        title={
            'text': f"Top 5 Canciones de {artist} en {year}",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis=dict(
            title='Canción',
            title_font=dict(size=14, color='lightskyblue'),
            tickfont=dict(size=12, color='lightskyblue')
        ),
        yaxis=dict(
            title='Minutos Reproducidos',
            range=[0, y_max],  # Ajustar el rango del eje Y
            title_font=dict(size=14, color='lightskyblue'),
            tickfont=dict(size=12, color='lightskyblue')
        ),
        showlegend=False
    )

    return fig

