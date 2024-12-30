import streamlit as st
from spotify_api.api import connect_to_spotify, get_artist_info, get_track_features

st.title("Análisis con Spotify API")
st.markdown("Usa la API de Spotify para explorar datos de canciones y artistas.")

# Configura tus credenciales
CLIENT_ID = "88ae7b7f86a249209a3afbc7e798fa13"
CLIENT_SECRET = "7fdbe5173c7d40cfab0708552f06b9fc"

sp = connect_to_spotify(CLIENT_ID, CLIENT_SECRET)

# Buscar un artista
st.subheader("Información de Artistas")
artist_name = st.text_input("Introduce el nombre de un artista:")
if artist_name:
    artist_info = get_artist_info(sp, artist_name)
    if artist_info:
        st.write(f"**Nombre:** {artist_info['name']}")
        st.write(f"**Géneros:** {', '.join(artist_info['genres'])}")
        st.write(f"**Seguidores:** {artist_info['followers']}")
        st.write(f"**Popularidad:** {artist_info['popularity']}")
    else:
        st.write("Artista no encontrado.")

# Buscar una canción
st.subheader("Características de Canciones")
track_name = st.text_input("Introduce el nombre de una canción:")
if track_name:
    track_features = get_track_features(sp, track_name)
    if track_features:
        st.write(f"**Danceability:** {track_features['danceability']}")
        st.write(f"**Energy:** {track_features['energy']}")
        st.write(f"**Tempo:** {track_features['tempo']}")
        st.write(f"**Valence:** {track_features['valence']}")
    else:
        st.write("Canción no encontrada.")
 
