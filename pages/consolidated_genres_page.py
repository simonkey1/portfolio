import streamlit as st
import pandas as pd
from genre_consolidation import prepare_data, format_genres_column, consolidate_genres_using_index, calculate_genre_trends, create_genre_trend_chart

# Título de la página
st.title("📊 Tendencias de Géneros Musicales (2017-2024)")

# Subtítulo
st.subheader("Explora cómo han cambiado tus géneros musicales favoritos a lo largo de los años")

# Instrucción para el usuario
st.markdown("""
Carga un archivo CSV con tus datos musicales. 
El archivo debe tener al menos estas columnas:
- `song`: Nombre de la canción.
- `artist`: Nombre del artista.
- `album`: Nombre del álbum.
- `ms`: Tiempo reproducido en milisegundos.
- `genres`: Géneros asociados a la canción.

Además, puede incluir columnas adicionales como `genre_1`, `genre_2`, etc.
""")

# Carga del archivo
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file:
    try:
        # Leer el archivo subido
        df = pd.read_csv(uploaded_file)

        # Validar las columnas necesarias
        required_columns = ['song', 'artist', 'album', 'ms', 'genres']
        if not all(col in df.columns for col in required_columns):
            missing_cols = [col for col in required_columns if col not in df.columns]
            st.error(f"El archivo cargado no contiene las columnas necesarias: {', '.join(missing_cols)}")
        else:
            # Preparar los datos
            st.write("Procesando el archivo...")
            df = prepare_data(df)
            df = format_genres_column(df)
            df = consolidate_genres_using_index(df)

            # Calcular tendencias
            st.write("Calculando tendencias de géneros...")
            genre_trends = calculate_genre_trends(df)

            # Crear gráfico
            st.write("Generando el gráfico...")
            fig = create_genre_trend_chart(genre_trends)

            # Mostrar el gráfico
            st.plotly_chart(fig, use_container_width=True)

            # Guardar el gráfico como imagen (opcional)
            if st.checkbox("¿Guardar gráfico como imagen?"):
                from genre_consolidation import save_chart
                save_chart(fig, filename="genre_trend_chart.png")
                st.success("El gráfico ha sido guardado como 'genre_trend_chart.png'.")

            # Mostrar tabla de tendencias
            st.subheader("Tabla de tendencias de géneros")
            st.dataframe(genre_trends)

    except Exception as e:
        st.error(f"Hubo un error al procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
