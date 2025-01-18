import streamlit as st
from consistent_artists import (
    prepare_data,
    create_consistency_chart,
    create_bts_playtime_chart,
    get_bts_playtime_in_days,
    get_total_playtime_in_days,
    get_consistent_artists_with_playtime,
)
from tracks_top5 import create_track_chart, prepare_track_data
from consistent_artists_no_BTS import (
    get_consistent_artists_with_playtime_excluding_bts,
    create_consistency_chart_no_bts,
)
from chart import create_trend_chart

def add_styles():
    """
    Agrega estilos CSS para centrar el contenido y aplicar padding.
    """
    st.markdown(
        """
        <style>
        /* Centra todo el contenido de la página */
        .main {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px; /* Añade espacio alrededor */
        }

        /* Ajusta el ancho máximo del contenido */
        .block-container {
            max-width: 800px; /* Cambia este valor según lo que prefieras */
            padding: 2rem;
        }

        /* Opcional: Personaliza los encabezados */
        h1, h2, h3 {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_spotify_wrapped():
    # Agregar estilos al inicio
    add_styles()

    # Título del proyecto
    st.title("🎵 Spotify Wrapped: Análisis Longitudinal de Datos")

    # Introducción
    st.markdown("""
    Este proyecto tiene como objetivo analizar las tendencias musicales de un período extenso, desde 2017 hasta 2024. 
    Basándonos en datos proporcionados por una usuaria de 23 años, originaria de Chile, hemos desarrollado visualizaciones que 
    destacan patrones únicos en su consumo musical.
    """)

    # Ruta al archivo
    data_filepath = "df_final.csv"

    try:
        # Preparar los datos
        df = prepare_data(data_filepath)
        track_data = prepare_track_data(data_filepath)

        # Sección 1: Minutos Totales por Año
        st.header("📊 Minutos Totales por Año")
        st.markdown("""
        Este gráfico muestra cómo evolucionó el tiempo total escuchado por año. 
        Observamos un pico notable en 2020, coincidiendo con el inicio de la pandemia.
        """)
        fig = create_trend_chart()
        st.plotly_chart(fig, use_container_width=True)

        # Sección 2: Top 3 Artistas Consistentes
        st.header("🎤 Top 3 Artistas Más Consistentes")
        st.markdown("""
        Aquí se destacan los tres artistas más reproducidos consistentemente cada año entre 2017 y 2024. 
        BTS, Bad Bunny y Justin Bieber lideran la lista.
        """)
        total_days = get_total_playtime_in_days(df)
        st.metric(label="🎧 Total de Días de Reproducción", value=f"{total_days} días")
        top_artists_df = get_consistent_artists_with_playtime(df, top_n=3)
        top_artists = top_artists_df['artist'].tolist()
        fig = create_consistency_chart(data_filepath, top_artists)
        st.plotly_chart(fig, use_container_width=True)

        # Sección 3: Top 15 Excluyendo BTS
        st.header("🎶 Top 15 Artistas Excluyendo BTS")
        st.markdown("""
        Excluyendo a BTS, exploramos los 15 artistas más reproducidos entre 2017 y 2024. 
        Visualiza cómo evolucionaron sus reproducciones a lo largo del tiempo.
        """)
        top_artists_df = get_consistent_artists_with_playtime_excluding_bts(df, top_n=15)
        top_artists = top_artists_df['artist'].tolist()
        fig = create_consistency_chart_no_bts(data_filepath, top_artists)
        st.plotly_chart(fig, use_container_width=True)

        # Sección 4: Análisis Exclusivo de BTS
        st.header("💜 Análisis de BTS")
        st.markdown("""
        Analizamos cómo evolucionaron las reproducciones de BTS durante el periodo. 
        Sus lanzamientos como 'Dynamite' impulsaron picos importantes.
        """)
        bts_days = get_bts_playtime_in_days(data_filepath)
        st.metric(label="🎧 Total de Días Reproducidos por BTS", value=f"{bts_days} días")
        bts_fig = create_bts_playtime_chart(data_filepath)
        st.plotly_chart(bts_fig, use_container_width=True)

        # Sección 5: Top 5 Canciones por Artista y Año
        st.header("🎵 Top 5 Canciones por Artista y Año")
        st.markdown("""
        Selecciona un artista y un año para explorar las cinco canciones más populares basadas en minutos reproducidos.
        """)
        search_query = st.text_input("Busca un Artista")
        artists = sorted(track_data['artist'].dropna().unique())
        filtered_artists = [a for a in artists if search_query.lower() in a.lower()]
        artist = st.selectbox("Selecciona el Artista", filtered_artists)
        year = st.selectbox("Selecciona el Año", sorted(track_data['year'].unique()))
        if artist and year:
            fig = create_track_chart(data_filepath, year, artist)
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Hubo un problema al procesar los datos: {e}")

