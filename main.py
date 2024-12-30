import streamlit as st
import scraping  # Importa el archivo de scraping como módulo
from chart import create_trend_chart  # Importa la función para el gráfico

# Título de la Landing Page
st.title("Simón Gómez | Sociólogo y Data Scientist")
st.subheader("Mi Portfolio de Proyectos")
st.write("¡Hola!, me apasiona la ciencia de datos y la programación.")
st.markdown("Bienvenido a mi portfolio. Explora mis proyectos y habilidades.")
st.button("Currículum Vitae")
st.button("Contactar")
st.button("GitHub")
st.button("LinkedIn")
st.button("Proyectos")

# Menú de navegación
menu = st.sidebar.selectbox(
    "Navegación",
    ["Inicio", "Scraping Web", "Análisis de Datos"]
)

# Navegación basada en la selección del usuario
if menu == "Inicio":
    st.header("Inicio")
    st.markdown("Esta es la página principal de mi portfolio, donde encontrarás una descripción general de mis proyectos.")

elif menu == "Scraping Web":
    st.header("Scraping Web")
    scraping.run_scraping()

elif menu == "Análisis de Datos":
    st.header("Análisis de Datos")
    st.markdown("Explora tendencias y análisis interactivos.")
    
    # Mostrar gráfico de tendencias
    st.subheader("Tendencias de Minutos Escuchados por Mes")
    fig = create_trend_chart()
    st.plotly_chart(fig, use_container_width=True)
