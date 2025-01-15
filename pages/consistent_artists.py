# pages/consistent_artists.py
import streamlit as st
from consistent_artists import prepare_data, get_consistent_artists_with_playtime, create_consistency_chart, create_consistency_animation, get_total_playtime_in_days

# Título y descripción de la página
st.title("🎶 Top 3 Artistas Más Consistentes")

st.markdown("""
Explora los 3 artistas más consistentes (presentes todos los años entre 2017 y 2024) 
con la mayor cantidad de minutos reproducidos. Además, visualiza cómo han evolucionado las tendencias año a año.
""")

# Ruta al archivo real
data_filepath = "df_final.csv"

try:
    # Preparar los datos y obtener el total de días reproducidos
    df_filtrado = prepare_data(data_filepath)
    total_days = get_total_playtime_in_days(df_filtrado)
    
    # Mostrar la métrica de días totales
    st.metric(label="🎧 Total de Días de Reproducción", value=f"{total_days} días")
    
    # Obtener el top 3 de artistas consistentes
    top_artists_df = get_consistent_artists_with_playtime(df_filtrado, top_n=3)
    top_artists = top_artists_df['artist'].tolist()

    # Crear el gráfico para los artistas destacados
    fig = create_consistency_chart(data_filepath, top_artists)
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar la tabla de artistas destacados
    st.subheader("Top 3 Artistas Más Escuchados y Consistentes")
    st.table(top_artists_df)

    # Agregar la animación
    st.subheader("🎥 Animación de Tendencias")
    st.markdown("""
    Visualiza cómo han evolucionado los minutos reproducidos de los artistas más consistentes a lo largo de los años.
    """)
    animation_fig = create_consistency_animation(data_filepath, top_artists)
    st.plotly_chart(animation_fig, use_container_width=True)

    st.markdown("""
    Estos artistas han sido consistentemente populares y acumulan la mayor cantidad de minutos reproducidos. La animación muestra las tendencias de su popularidad.
    """)
except Exception as e:
    st.error(f"Hubo un problema al procesar los datos: {e}")
