import streamlit as st
import pandas as pd
from track_features import (
    get_top_15_artists,
    filter_top_15_songs,
    process_artist_genres,
)

# Título y descripción
st.title("🎵 Géneros Asociados al Top 15 de Artistas")
st.markdown("""
Sube tu archivo de canciones y analizaremos los géneros asociados a los **Top 15 artistas más escuchados**.
""")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV con las canciones", type=["csv"])

if uploaded_file is not None:
    # Cargar el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Validar columnas requeridas
    if {"artist", "song", "ms"}.issubset(df.columns):
        # Obtener el Top 15 artistas
        top_15_artists = get_top_15_artists(df)
        st.subheader("🎧 Top 15 Artistas Más Escuchados")
        st.table(top_15_artists)

        # Filtrar las canciones del Top 15 artistas
        filtered_songs = filter_top_15_songs(df, top_15_artists)

        # Configurar barra de progreso
        st.markdown("### Procesando géneros...")
        progress_bar = st.progress(0)
        progress_text = st.empty()

        def update_progress(processed, total):
            percent = int((processed / total) * 100)
            progress_bar.progress(percent)
            progress_text.write(f"Procesando: {processed}/{total} artistas")

        # Procesar géneros de los artistas (sin límite)
        genres_df = process_artist_genres(filtered_songs, progress_callback=update_progress)

        # Mostrar resultados
        st.subheader("🎶 Géneros de las Canciones del Top 15 Artistas")
        st.dataframe(genres_df)

        # Descargar archivo enriquecido
        csv = genres_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar archivo enriquecido",
            data=csv,
            file_name="artist_genres_top15.csv",
            mime="text/csv"
        )
    else:
        st.error("El archivo debe contener las columnas 'artist', 'song' y 'ms'.")
