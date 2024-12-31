# pages/consistent_artists.py
import streamlit as st
from consistent_artists import prepare_data, get_consistent_artists_with_playtime, create_consistency_chart, get_total_playtime_in_days

# Título y descripción de la página
st.title("🎶 Top 3 Artistas Más Consistentes")

st.markdown("""
Explora los 3 artistas más consistentes (presentes todos los años entre 2017 y 2024) 
con la mayor cantidad de minutos reproducidos.
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

    # Crear el gráfico para los artistas destacados
    top_artists = top_artists_df['artist'].tolist()
    fig = create_consistency_chart(data_filepath, top_artists)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar la tabla de artistas destacados
    st.subheader("Top 3 Artistas Más Escuchados y Consistentes")
    st.table(top_artists_df)

    st.markdown("""
    Estos artistas han sido consistentemente populares y acumulan la mayor cantidad de minutos reproducidos.
    """)
except Exception as e:
    st.error(f"Hubo un problema al procesar los datos: {e}")
