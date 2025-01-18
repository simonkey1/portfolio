import streamlit as st
from consistent_artists import (
    prepare_data,
    create_consistency_chart,
    create_bts_playtime_chart,
    get_bts_playtime_in_days,
    get_total_playtime_in_days,
    get_consistent_artists_with_playtime,
)
from tracks_top5 import create_track_chart, prepare_track_data
from consistent_artists_no_BTS import (
    get_consistent_artists_with_playtime_excluding_bts,
    create_bar_chart_animation,
)
from chart import create_trend_chart


# Configuración inicial de la app
st.set_page_config(
    page_title="Spotify Wrapped 2017-2024",
    page_icon="🎵",
    layout="wide",
)

# Función para agregar fondo degradado
def add_background_gradient():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to bottom, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
            background-attachment: fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Agregar gradiente de fondo
add_background_gradient()

# Título principal
st.title("🎵 Spotify Wrapped: Análisis Longitudinal de Datos")
st.markdown("""
Todos los años desde 2015 Spotify Wrapped nos permite ver nuestros datos de escucha. Pero hay ocasiones donde no nos sentimos tan identificados con sus resultados. El año pasado, una amiga me comentó que no estaba satisfecha son su Spotify Wrapped, que no sentía que reflejara sus gustos musicales. Así que me embarqué en la idea de hacer mi propio Spotify Wrapped, ¿la diferencia? !Con datos de más de 8 años!. Quise observar sus patrones de escucha de manera más holgada que un Spotify Wrapped anual. El siguiente análisis es el resultado de mi experimento.
""")

# Ruta al archivo de datos
data_filepath = "df_final.csv"

try:
    # Preparar los datos
    df = prepare_data(data_filepath)
    track_data = prepare_track_data(data_filepath)



    # Sección: Minutos Totales por Año

    total_days = get_total_playtime_in_days(df)
    st.metric(label="🎧 Total de Días de Reproducción", value=f"{total_days} días")
    top_artists_df = get_consistent_artists_with_playtime(df, top_n=3)
    top_artists = top_artists_df['artist'].tolist()
    

    st.header("📊 Minutos Totales por Año")
    st.markdown("""
    Primero empecé con sus minutos escuchados por años, con resultados muy interesantes. El marzo de 2020, se inició la pandemia, un proceso que afectó los hábitos de escucha de música de muchas personas, incluyendo a mi amiga. Notamos que tuvo un pico impresionante de minutos al día durante marzo. Sin embargo, luego vemos un declive en los meses siguientes, ocasionando que en septiembre del mismo año se escuche menos música que en 2019. Ante esto, le pregunté a mi amiga si había notado este cambio, a lo que respondió que sí, que en efecto, utilizó muchísimo Spotify al inicio de la pandemia, pero a medida que avanzaron los meses, optó por escuchar lofi en Youtube para dedicarse principalmente al estudio, lo cual se refleja en la gráfica.
    """)
    fig = create_trend_chart()
    st.plotly_chart(fig, use_container_width=True)

  

    # Sección: Top 3 Artistas Consistentes
    st.header("🎤 Top 3 Artistas Más Consistentes")
    st.markdown("""
    Normalmente Spotify te proporciona tu artista destacado del año, indicando sus minutos totales y tu posición respecto a otros oyentes. Para el pasado 2024, Spotify señaló que Mora fue su artista más destacado, sumando 9288 minutos. Ahondando en la idea de que no se sentía identificada con los resultados de Spotify Wrapped, le pregunté si Mora era su artista favorito, a lo que respondió que no, que le gustaba mucho, pero que no era su favorito. Por lo que decidí hacer un análisis más profundo de sus artistas más escuchados, añadiendo los minutos de todos los años desde 2017. Encontré que sus artistas más consistentes son: BTS, Bad Bunny y Justin Bieber. Así que lo siento Mora, destacaste bastante este año, pero la consistencia te delata que quizás eres sólo una temporada en la vida de mi amiga.
                
    En cuanto a mi propio ranking, podemos observar que BTS arrasa, opacando enormemente los datos de Justin Bieber y Bad Bunny. Entre todos los años, 2020 fue definitvamente de BTS, registrando casi 25 mil minutos de reproducción!, seguido de Bad Bunny con "solo" 2300 minutos y Justin Bieber con 905 minutos. Pero, ¿Por qué BTS? Mi amiga es fanática antes de llegar a estos números. consulté con mi amiga y nos cuenta que precisamente ese año se estrenó el álbum "Map of the Soul: 7", el cual fue considerado el más escuchado en la historia de Corea del Sur y su sencillo 'Dynamite' encabezando el ranking de Billboard por 3 semanas consecutivas,!Impresionante!
    """)

    fig = create_consistency_chart(data_filepath, top_artists)
    st.plotly_chart(fig, use_container_width=True)


    # Sección: Top 15 Excluyendo BTS
    st.header("🎶 Top 15 Artistas Excluyendo BTS")
    st.markdown("""
    Excluyendo a BTS, exploramos los 15 artistas más reproducidos entre 2017 y 2024. 
    Visualiza cómo evolucionaron sus reproducciones a lo largo del tiempo.
    """)
    top_artists_df = get_consistent_artists_with_playtime_excluding_bts(df, top_n=15)
    top_artists = top_artists_df['artist'].tolist()
    fig = create_bar_chart_animation(data_filepath, top_artists)
    st.plotly_chart(fig, use_container_width=True)

    # Sección: Análisis Exclusivo de BTS
    st.header("💜 Análisis de BTS")
    st.markdown("""
    Analizamos cómo evolucionaron las reproducciones de BTS durante el periodo. 
    Sus lanzamientos como 'Dynamite' impulsaron picos importantes.
    """)
    bts_days = get_bts_playtime_in_days(data_filepath)
    st.metric(label="🎧 Total de Días Reproducidos por BTS", value=f"{bts_days} días")
    bts_fig = create_bts_playtime_chart(data_filepath)
    st.plotly_chart(bts_fig, use_container_width=True)

    # Sección: Top 5 Canciones por Artista y Año
    st.header("🎵 Top 5 Canciones por Artista y Año")
    st.markdown("""
    Selecciona un artista y un año para explorar las cinco canciones más populares basadas en minutos reproducidos.
    """)
    search_query = st.text_input("Busca un Artista")
    artists = sorted(track_data['artist'].dropna().unique())
    filtered_artists = [a for a in artists if search_query.lower() in a.lower()]
    artist = st.selectbox("Selecciona el Artista", filtered_artists)
    year = st.selectbox("Selecciona el Año", sorted(track_data['year'].unique()))
    if artist and year:
        fig = create_track_chart(data_filepath, year, artist)
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Hubo un problema al procesar los datos: {e}")
