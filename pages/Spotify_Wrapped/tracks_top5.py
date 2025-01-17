import pandas as pd
import streamlit as st
from tracks_top5 import create_track_chart, prepare_track_data

def render_page():
    st.title("🎵 Análisis Interactivo de Canciones")

    filepath = "df_final.csv"
    track_data = prepare_track_data(filepath)

    search_query = st.text_input("Busca un Artista")
    artists = sorted(track_data['artist'].dropna().unique())
    filtered_artists = [a for a in artists if search_query.lower() in a.lower()]
    artist = st.selectbox("Selecciona el Artista", filtered_artists)

    year = st.selectbox("Selecciona el Año", sorted(track_data['year'].unique()))

    if artist and year:
        st.subheader(f"Top 5 Canciones de {artist} en {year}")
        fig = create_track_chart(filepath, year, artist)
        st.plotly_chart(fig, use_container_width=True)
