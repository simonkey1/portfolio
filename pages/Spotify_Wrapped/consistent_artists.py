import streamlit as st
from consistent_artists import (
    prepare_data,
    get_consistent_artists_with_playtime,
    create_consistency_chart,
    create_consistency_animation,
    get_total_playtime_in_days
)

def render_page():
    st.title("🎶 Top 3 Artistas Más Consistentes")

    st.markdown("""
    Explora los 3 artistas más consistentes (presentes todos los años entre 2017 y 2024) 
    con la mayor cantidad de minutos reproducidos. Además, visualiza cómo han evolucionado las tendencias año a año.
    """)

    data_filepath = "df_final.csv"

    try:
        df_filtrado = prepare_data(data_filepath)
        total_days = get_total_playtime_in_days(df_filtrado)

        st.metric(label="🎧 Total de Días de Reproducción", value=f"{total_days} días")
        
        top_artists_df = get_consistent_artists_with_playtime(df_filtrado, top_n=3)
        top_artists = top_artists_df['artist'].tolist()

        fig = create_consistency_chart(data_filepath, top_artists)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Top 3 Artistas Más Escuchados y Consistentes")
        st.table(top_artists_df)

        st.subheader("🎥 Animación de Tendencias")
        animation_fig = create_consistency_animation(data_filepath, top_artists)
        st.plotly_chart(animation_fig, use_container_width=True)

        st.markdown("""
        Estos artistas han sido consistentemente populares y acumulan la mayor cantidad de minutos reproducidos. La animación muestra las tendencias de su popularidad.
        """)
    except Exception as e:
        st.error(f"Hubo un problema al procesar los datos: {e}")
