import streamlit as st
from chart import create_trend_chart  # Importa el gráfico desde charts.py

# En pages/Análisis de Datos.py
import streamlit as st
from spotify_api.api import connect_to_spotify, get_artist_info

st.title("Análisis de Datos con Spotify API")

# Configura tus credenciales
CLIENT_ID = "88ae7b7f86a249209a3afbc7e798fa13"
CLIENT_SECRET = "7fdbe5173c7d40cfab0708552f06b9fc"

sp = connect_to_spotify(CLIENT_ID, CLIENT_SECRET)

# Ejemplo: Buscar un artista
artist_name = st.text_input("Introduce un artista para buscar:")
if artist_name:
    artist_info = get_artist_info(sp, artist_name)
    if artist_info:
        st.write(f"Artista: {artist_info['name']}")
        st.write(f"Géneros: {', '.join(artist_info['genres'])}")
        st.write(f"Seguidores: {artist_info['followers']}")
        st.write(f"Popularidad: {artist_info['popularity']}")
    else:
        st.write("Artista no encontrado.")
