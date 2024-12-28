import streamlit as st
import scraping  # Importa el archivo de scraping como módulo

# Título de la Landing Page
st.title("Mi Portfolio de Proyectos")
st.markdown("Bienvenido a mi portfolio. Explora mis proyectos y habilidades.")

# Menú de navegación
menu = st.sidebar.selectbox(
    "Navegación",
    ["Inicio", "Scraping Web"]
)

# Navegación basada en la selección del usuario
if menu == "Inicio":
    st.header("Inicio")
    st.markdown("Esta es la página principal de mi portfolio, donde encontrarás una descripción general de mis proyectos.")
elif menu == "Scraping Web":
    st.header("Scraping Web")
    scraping.run_scraping()  # Llama a la función de scraping definida en scraping.py
