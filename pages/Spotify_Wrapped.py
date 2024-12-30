import streamlit as st
from chart import create_trend_chart  # Importa el gráfico desde charts.py

st.title("Análisis de Datos")
st.markdown("Explora tendencias y análisis interactivos.")
fig = create_trend_chart()
st.plotly_chart(fig, use_container_width=True)
