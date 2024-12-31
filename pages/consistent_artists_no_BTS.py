# pages/consistent_artists_no_bts.py
import streamlit as st
from consistent_artists_no_BTS import prepare_data, get_consistent_artists_with_playtime_excluding_bts, create_consistency_chart_no_bts

# Título y descripción de la página
st.title("🎶 Consistencia de Artistas (Excluyendo BTS)")

st.markdown("""
Explora los artistas más consistentes (presentes todos los años entre 2017 y 2024), 
excluyendo a BTS, quienes acumulan una cantidad desproporcionada de minutos reproducidos.
""")

# Ruta al archivo real (asegúrate de que esté en tu directorio)
data_filepath = "df_final.csv"

try:
    # Prepara los datos y filtra los artistas consistentes con mayor tiempo reproducido
    df_filtrado = prepare_data(data_filepath)
    top_artists_df = get_consistent_artists_with_playtime_excluding_bts(df_filtrado, top_n=15)

    # Crear el gráfico para los artistas destacados
    top_artists = top_artists_df['artist'].tolist()
    fig = create_consistency_chart_no_bts(data_filepath, top_artists)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar la tabla de artistas destacados
    st.subheader("Top 15 Artistas Más Escuchados y Consistentes (Excluyendo BTS)")
    st.table(top_artists_df)

    st.markdown("""
    Estos artistas no solo han sido consistentes a lo largo de los años, sino que también acumulan la mayor cantidad de minutos reproducidos (sin incluir a BTS).
    """)
except Exception as e:
    st.error(f"Hubo un problema al procesar los datos: {e}")
