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
Todos los años desde 2015 Spotify Wrapped nos permite ver nuestros datos de escucha. Pero hay ocasiones donde no nos sentimos tan identificados con sus resultados. El año pasado, una persona me comentó que no estaba satisfecha son su Spotify Wrapped, que no sentía que reflejara sus gustos musicales. Así que me embarqué en la idea de hacer mi propio Spotify Wrapped, ¿la diferencia? !Con datos de más de 8 años!. Quise observar sus patrones de escucha de manera más holgada que un Spotify Wrapped anual. El siguiente análisis es el resultado de mi investigación. ¡Espero que lo disfruten!
""")

# Ruta al archivo de datos
data_filepath = "df_final.csv"

try:
    # Preparar los datos
    df = prepare_data(data_filepath)
    track_data = prepare_track_data(data_filepath)


    # Sección: Minutos Totales por Año

    top_artists_df = get_consistent_artists_with_playtime(df, top_n=3)
    top_artists = top_artists_df['artist'].tolist()
    

    st.header("📊 Minutos Totales por Año")
    st.markdown("""
    Primero empecé con sus minutos escuchados por años, con resultados muy interesantes. El marzo de 2020, se inició la pandemia, un proceso que afectó los hábitos de escucha de música de muchas personas, incluyendo a la persona mencionada. Notamos que tuvo un pico impresionante de minutos al día durante marzo. Sin embargo, luego vemos un declive en los meses siguientes, ocasionando que en septiembre del mismo año se escuche menos música que en 2019. Ante esto, le pregunté a la persona si había notado este cambio, a lo que respondió que sí, que en efecto, utilizó muchísimo Spotify al inicio de la pandemia, pero a medida que avanzaron los meses, optó por escuchar lofi en Youtube para dedicarse principalmente al estudio, lo cual se refleja en la gráfica.
    """)
    fig = create_trend_chart()
    st.plotly_chart(fig, use_container_width=True)

  

    # Sección: Top 3 Artistas Consistentes
    st.header("🎤 Top 3 Artistas Más Consistentes")
    st.markdown("""
    Normalmente Spotify te proporciona tu artista destacado del año, indicando sus minutos totales y tu posición respecto a otros oyentes. Para el pasado 2024, Spotify señaló que Mora fue su artista más destacado, sumando 9288 minutos. Ahondando en la idea de que no se sentía identificada con los resultados de Spotify Wrapped, le pregunté si Mora era su artista favorito, a lo que respondió que no, que le gustaba mucho, pero que no era su favorito. Por lo que decidí hacer un análisis más profundo de sus artistas más escuchados, añadiendo los minutos de todos los años desde 2017. Encontré que sus artistas más consistentes son: BTS, Bad Bunny y Justin Bieber. Así que lo siento Mora, destacaste bastante este año, pero la consistencia te delata que quizás eres sólo una temporada en la vida de la persona mencionada.
                
    En cuanto a mi propio ranking, podemos observar que BTS arrasa, opacando enormemente los datos de Justin Bieber y Bad Bunny. Entre todos los años, 2020 fue definitvamente de BTS, registrando casi 25 mil minutos de reproducción!, seguido de Bad Bunny con "solo" 2300 minutos y Justin Bieber con 905 minutos. Pero, ¿Por qué BTS? La persona mencionada es fanática antes de llegar a estos números. Consulté con ella y nos cuenta que precisamente ese año se estrenó el álbum "Map of the Soul: 7", el cual fue considerado el más escuchado en la historia de Corea del Sur y su sencillo 'Dynamite' encabezando el ranking de Billboard por 3 semanas consecutivas,!Impresionante!
    """)

    fig = create_consistency_chart(data_filepath, top_artists)
    st.plotly_chart(fig, use_container_width=True)


    # Sección: Top 15 Excluyendo BTS
    st.header("🎶 Top 15 Artistas Excluyendo BTS")
    st.markdown("""
    Ya que BTS es el artista más escuchado, también es el más problemático para el análisis de otros artistas. Su popularidad empeora la legibilidad de la visualización. Por lo que decidí excluir a BTS de la visualización para poder observar a otros artistas con mayor claridad. y... Sorpresa! no está ni en el top 15 de artistas más escuchados Mora. ¿Qué pasó con Mora? ¿Por qué no está en el top 15? Bueno, Mora es un artista relativamente nuevo, y nuestra persona empezó a escucharlo notoriamente desde 2023, por lo que sí, es popular, pero no puede denominarse un artista consistente.
    """)
    top_artists_df = get_consistent_artists_with_playtime_excluding_bts(df, top_n=15)
    top_artists = top_artists_df['artist'].tolist()
    fig = create_bar_chart_animation(data_filepath, top_artists)
    st.plotly_chart(fig, use_container_width=True)

    # Sección: Análisis Exclusivo de BTS
    st.header("Hablemos de Datos 🤓")
    st.markdown("""
    Transformar los minutos escuchados de un artista a días nos da una métrica interesante. Nos damos cuenta que en estos 7 años, ¡BTS ha sido escuchado por un total de casi 51 días! ¿Qué significa esto? Bueno, si escuchamos a BTS por 51 días seguidos, estaríamos escuchando a BTS desde el 1 de enero hasta el 20 de febrero. O si leyeras un libro de 300 páginas en 1 hora, podrías leer 122 libros en 51 días. ¡Impresionante!
                
    Otra métrica es el uso general de la aplicación. En estos 7 años, nuestra persona ha utilizado Spotify por un total de 326 días. Si escuchamos a BTS por 51 días, entonces el resto de los días ha sido utilizado para escuchar a otros artistas. ¿Qué significa esto? Que BTS es un artista muy importante en la vida de la persona mencionada, pero no el único. En la siguiente sección podremos explorar nosotros mismos el artista que queramos en el año que queramos y ver las 5 canciones más escuchadas. Si observamos menos de 5 es porque no está registrado que haya escuchado 5 canciones diferentes de ese artista en ese año.
    """)

    bts_fig = create_bts_playtime_chart(data_filepath)
    st.plotly_chart(bts_fig, use_container_width=True)

    bts_days = get_bts_playtime_in_days(data_filepath)
    st.metric(label="🎧 Total de Días Reproducidos por BTS", value=f"{bts_days} días")

    total_days = get_total_playtime_in_days(df)
    st.metric(label="🎧 Total de Días de Reproducción", value=f"{total_days} días")
    top_artists_df = get_consistent_artists_with_playtime(df, top_n=3)
    top_artists = top_artists_df['artist'].tolist()

    # Sección: Top 5 Canciones por Artista y Año
    st.header("🎵 Top 5 Canciones por Artista y Año")
    st.markdown("""
    Más allá de los artistas consistentes, podemos averiguar su top 5 de canciones más escuchadas independiente del artista. Anteriormente hablamos de Mora, a través de esto nos damos cuenta que el 2023 fue cuando empezó a subir sustancialmente sus minutos escuchados, por eso no está figurado como artista consistente. Spotify lo destaca el 2024, porque respecto al año anterior subió 291% en minutos escuchados. ¿Qué pasó en 2023? Bueno, Mora lanzó su álbum "La Reina de la Noche", el cual fue bastante exitoso y se ha logrado mantener arriba, veremos si esta tendencia a la subida se mantiene este 2025.
    """)
    default_artist = "Mora"
    default_year = 2023

    # Búsqueda y selección de artista
    search_query = st.text_input("Busca un Artista", value=default_artist)  # Valor inicial como "Mora"
    artists = sorted(track_data['artist'].dropna().unique())
    filtered_artists = [a for a in artists if search_query.lower() in a.lower()]

    # Buscar el índice del artista predeterminado (Mora) en la lista filtrada
    if default_artist in filtered_artists:
        artist_index = filtered_artists.index(default_artist)  # Obtener índice de Mora
    else:
        artist_index = 0  # Seleccionar el primer valor si Mora no está

    # Mostrar el selectbox con el artista predeterminado seleccionado
    artist = st.selectbox("Selecciona el Artista", filtered_artists, index=artist_index)

    # Selección de año
    years = sorted(track_data['year'].unique())
    if default_year in years:
        year_index = years.index(default_year)  # Seleccionar 2023 si está disponible
    else:
        year_index = 0  # Seleccionar el primer año si 2023 no está

    year = st.selectbox("Selecciona el Año", years, index=year_index)

    # Generar gráfico si hay artista y año seleccionados
    if artist and year:
        st.markdown(f"### Top 5 Canciones de {artist} en {year}")
        fig = create_track_chart(data_filepath, year, artist)
        st.plotly_chart(fig, use_container_width=True)



    # Sección 6: conclusiones

    st.header("Conclusiones")
    st.markdown(""" Este proyecto de Spotify Wrapped personalizado nos permite observar cómo las tendencias musicales y los hábitos de escucha evolucionan con el tiempo. Aunque no tiene la intención de superar el Spotify Wrapped original, sí busca añadir una nueva arista a la conversación. Al extender el análisis a más de 8 años, enriquecemos la narrativa y obtenemos un panorama más amplio y profundo de los datos de escucha.

    Puntos destacados del análisis:

    Impacto de los eventos globales: Marzo de 2020 marcó un punto de inflexión, con un aumento significativo en el consumo musical durante el confinamiento. Este fenómeno muestra cómo la música puede ser un refugio emocional en momentos de incertidumbre.
    Artistas más consistentes: BTS, Bad Bunny y Justin Bieber no solo son nombres destacados, sino que su presencia constante refleja una fidelidad de sus fans y su impacto cultural sostenido.
    Mora como fenómeno reciente: A pesar de que Spotify Wrapped lo destacó en 2024, el análisis muestra que Mora empezó a ser relevante en 2023, consolidándose gracias a su exitoso álbum "La Reina de la Noche". Esto evidencia cómo las tendencias pueden cambiar rápidamente, pero la consistencia sigue siendo clave.
    El peso de los números: Transformar minutos en días escuchados pone en perspectiva el impacto que los artistas tienen en nuestras vidas. BTS, con casi 51 días de reproducción, simboliza una conexión profunda y significativa para la persona analizada.
    Más allá del análisis original: Si bien este proyecto se enfoca en tendencias longitudinales, hay muchas posibilidades de enriquecer el análisis con otros gráficos e indicadores. Algunas ideas incluyen:

    Análisis por géneros musicales: ¿Cuáles son los géneros más dominantes en diferentes etapas de la vida de la persona?
    Relevancia de álbumes: ¿Qué álbumes dejaron una huella más profunda a lo largo de los años?
    Colaboraciones entre artistas: ¿Cómo influyen los dúos o colaboraciones en las tendencias de escucha?
    Estacionalidad en los hábitos musicales: Identificar patrones asociados a temporadas como verano o invierno. """)
    
except Exception as e:
    st.error(f"Hubo un problema al procesar los datos: {e}")
