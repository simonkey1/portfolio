import streamlit as st
from consistent_artists import create_bts_playtime_chart, get_bts_playtime_in_days

def render_page():
    st.title("🎤 Evolución de Minutos Reproducidos de BTS")

    st.markdown("""
    Descubre cómo han evolucionado los minutos reproducidos de **BTS** a lo largo de los años.
    """)

    data_filepath = "df_final.csv"

    try:
        total_days = get_bts_playtime_in_days(data_filepath)
        st.metric(label="🎧 Total de Días Reproducidos por BTS", value=f"{total_days} días")

        fig = create_bts_playtime_chart(data_filepath)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        Desde su debut, **BTS** ha roto innumerables récords, 
        y estos datos reflejan su impacto global en la música. 🎶
        ¿Cuál es tu canción favorita de BTS? 💜
        """)
    except Exception as e:
        st.error(f"Hubo un problema al procesar los datos: {e}")
