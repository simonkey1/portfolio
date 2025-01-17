import streamlit as st
from pages.Spotify_Wrapped.bts_playtime import render_page as render_bts_playtime
from pages.Spotify_Wrapped.consistent_artists import render_page as render_consistent_artists
from pages.Spotify_Wrapped.consistent_artists_no_BTS import render_page as render_consistent_artists_no_bts
from pages.Spotify_Wrapped.tracks_top5 import render_page as render_tracks_top5

def render_spotify_wrapped():
    st.title("🎵 Spotify Wrapped: Análisis Longitudinal de Datos")
    st.markdown("""
    Bienvenido a la sección de **Spotify Wrapped**, donde exploramos datos de hábitos de escucha a lo largo de los años.
    Selecciona uno de los análisis disponibles para profundizar:
    """)

    # Opciones para subpáginas
    subpage = st.selectbox(
        "Explorar Subpáginas",
        ["Minutos Escuchados por Año", 
         "Top 3 Artistas Consistentes", 
         "Top 15 Artistas (Excluyendo BTS)", 
         "Evolución de BTS", 
         "Top 5 Canciones por Año y Artista"]
    )

    # Redirigir a la subpágina seleccionada
    if subpage == "Minutos Escuchados por Año":
        render_consistent_artists()
    elif subpage == "Top 3 Artistas Consistentes":
        render_consistent_artists()
    elif subpage == "Top 15 Artistas (Excluyendo BTS)":
        render_consistent_artists_no_bts()
    elif subpage == "Evolución de BTS":
        render_bts_playtime()
    elif subpage == "Top 5 Canciones por Año y Artista":
        render_tracks_top5()


