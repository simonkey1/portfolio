import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

def run_scraping():
    st.subheader("Proyecto de Web Scraping - Paso a Paso")

    # Paso 1: Introducir URL
    url = st.text_input("Introduce la URL para scraping", "https://jumbo.cl", key="url_input")

    if url:
        st.write(f"URL introducida: {url}")

        # Paso 2: Realizar el scraping
        st.header("Paso 2: Scraping del contenido HTML")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                st.write("Scraping exitoso. HTML obtenido:")
                st.code(response.text[:500])  # Muestra solo los primeros 500 caracteres
            else:
                st.error(f"Error al realizar el scraping. Código de estado: {response.status_code}")
        except Exception as e:
            st.error(f"Error al intentar conectar con la URL: {e}")

        # Paso 3: Parsear el HTML
        st.header("Paso 3: Parsear y extraer datos")
        try:
            soup = BeautifulSoup(response.text, "html.parser")
            titles = [h1.text for h1 in soup.find_all("h1")]
            st.write("Títulos extraídos (etiquetas H1):", titles)
        except Exception as e:
            st.error(f"Error al parsear el contenido HTML: {e}")

        # Paso 4: Convertir los datos en DataFrame
        st.header("Paso 4: Tabular los datos")
        try:
            data = {"Títulos": titles}
            df = pd.DataFrame(data)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error al tabular los datos: {e}")
