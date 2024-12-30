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

