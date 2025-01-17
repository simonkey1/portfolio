import streamlit as st
from pages.Spotify_Wrapped.spotify_wrapped_config import render_spotify_wrapped
from pages.dark_metrics import render_page
import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


# Sidebar
st.sidebar.title("📂 Selecciona la Sección")
section = st.sidebar.radio(
    "Explorar",
    ["Home", "Spotify Wrapped", "Dark Metrics", "Scraping Web"]
)

if section == "Home":
    st.title("Bienvenido a Mi Proyecto de Análisis de Datos")
    st.markdown("""
    Este proyecto contiene diferentes módulos enfocados en análisis de datos.
    Explora las secciones en la barra lateral para ver los diferentes aspectos de este proyecto.
    """)
elif section == "Spotify Wrapped":
    render_spotify_wrapped()
elif section == "Dark Metrics":
 render_page()

print("PYTHONPATH:", sys.path)