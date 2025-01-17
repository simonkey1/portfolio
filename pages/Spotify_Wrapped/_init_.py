import streamlit as st

import streamlit as st
from Spotify_Wrapped import render_page as render_minutes_per_year
from consistent_artists import render_page as render_top3_artists
from consistent_artists_no_BTS import render_page as render_top15_excluding_bts
from bts_playtime import render_page as render_bts_analysis
from tracks_top5 import render_page as render_top_tracks

st.title("🎧 Spotify Wrapped")

st.markdown("""
¡Bienvenido al análisis de tu Spotify Wrapped personalizado! Aquí puedes explorar diferentes aspectos de tus datos musicales.
""")

# Opciones de subpáginas
subpage = st.radio(
    "Explora diferentes aspectos de tus datos:",
    [
        "Minutos escuchados por año",
        "Top 3 artistas consistentes",
        "Top 15 artistas excluyendo BTS",
        "Análisis dedicado a BTS",
        "Popularidad de canciones"
    ]
)

# Redirigir a la subpágina seleccionada
if subpage == "Minutos escuchados por año":
    from Spotify_Wrapped import render_page
    render_page()

elif subpage == "Top 3 artistas consistentes":
    from consistent_artists import render_page
    render_page()

elif subpage == "Top 15 artistas excluyendo BTS":
    from consistent_artists_no_BTS import render_page
    render_page()

elif subpage == "Análisis dedicado a BTS":
    from bts_playtime import render_page
    render_page()

elif subpage == "Popularidad de canciones":
    from tracks_top5 import render_page
    render_page()