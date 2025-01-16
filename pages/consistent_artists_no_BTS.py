# pages/consistent_artists_no_bts.py
import streamlit as st
from consistent_artists_no_BTS import (
    prepare_data,
    get_consistent_artists_with_playtime_excluding_bts,
    create_consistency_chart_no_bts,
    create_bar_chart_animation
)


# Título y descripción de la página
st.title("🎶 Consistencia de Artistas (Excluyendo BTS)")

st.markdown("""
Explora los artistas más consistentes (presentes todos los años entre 2017 y 2024), 
excluyendo a BTS, quienes acumulan una cantidad desproporcionada de minutos reproducidos.
""")

data_filepath = "df_final.csv"

try:
    df_filtrado = prepare_data(data_filepath)
    top_artists_df = get_consistent_artists_with_playtime_excluding_bts(df_filtrado, top_n=15)
    top_artists = top_artists_df['artist'].tolist()

    # Gráfico estático
    st.subheader("📊 Gráfico Estático")
    static_fig = create_consistency_chart_no_bts(data_filepath, top_artists)
    st.plotly_chart(static_fig, use_container_width=True)

    # Animación
    st.subheader("🎥 Animación de Tendencias")
    animation_fig = create_bar_chart_animation(data_filepath, top_artists)
    st.plotly_chart(animation_fig, use_container_width=True)

    # Tabla con los artistas destacados
    st.subheader("Top 15 Artistas Más Escuchados y Consistentes (Excluyendo BTS)")
    st.table(top_artists_df)

except Exception as e:
    st.error(f"Hubo un problema al procesar los datos: {e}")
