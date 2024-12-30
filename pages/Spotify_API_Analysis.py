import streamlit as st
from spotify_api.api import (
    connect_to_spotify,
    get_artist_info,
    get_artist_albums,
    get_album_tracks,
    get_track_features
)

# Configura tus credenciales
CLIENT_ID = "TU_CLIENT_ID"
CLIENT_SECRET = "TU_CLIENT_SECRET"

sp = connect_to_spotify(CLIENT_ID, CLIENT_SECRET)

st.title("Análisis con Spotify API")
st.subheader("Motor de Búsqueda Interactivo")

# Paso 1: Buscar Artista
artist_search = st.text_input("Introduce el nombre del artista para buscar:")
if artist_search:
    artist_info = get_artist_info(sp, artist_search)
    if artist_info:
        st.write(f"**Artista seleccionado:** {artist_info['name']}")
        st.write(f"**Géneros:** {', '.join(artist_info['genres'])}")
        st.write(f"**Seguidores:** {artist_info['followers']}")
        st.write(f"**Popularidad:** {artist_info['popularity']}")

        # Paso 2: Buscar Álbumes del Artista
        albums = get_artist_albums(sp, artist_info['id'])
        album_options = [album['name'] for album in albums]
        selected_album = st.selectbox("Selecciona un álbum:", album_options)

        # Paso 3: Buscar Canciones del Álbum
        album_id = [album['id'] for album in albums if album['name'] == selected_album][0]
        tracks = get_album_tracks(sp, album_id)
        track_options = [track['name'] for track in tracks]
        selected_track = st.selectbox("Selecciona una canción:", track_options)

        # Paso 4: Mostrar Características de la Canción
        track_id = [track['id'] for track in tracks if track['name'] == selected_track][0]
        track_features = get_track_features(sp, track_id)

        if track_features:
            st.write(f"**Danceability:** {track_features['danceability']}")
            st.write(f"**Energy:** {track_features['energy']}")
            st.write(f"**Tempo:** {track_features['tempo']}")
            st.write(f"**Valence:** {track_features['valence']}")
    else:
        st.error("No se encontró el artista.")
