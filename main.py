import streamlit as st
import main  # Importa tu archivo de scraping como módulo

# Título de la Landing Page
st.title("Mi Portfolio de Proyectos")
st.markdown("Bienvenido a mi portfolio. Explora mis proyectos y habilidades.")

# Menú de navegación
menu = st.sidebar.selectbox(
    "Navegación",
    ["Inicio", "Scraping Web"]
)

# Navegación basada en la selección
if menu == "Inicio":
    st.header("Inicio")
    st.markdown("Esta es la página principal de mi portfolio.")
elif menu == "Scraping Web":
    st.header("Scraping Web")
    # Llama al código del archivo main.py
    main.run_scraping()
