import streamlit as st
from metric_plot import create_metric_plot

def render_page():
    """
    Renderiza la página de métricas con tema oscuro y proporción 4:5.
    """
    # Título de la página
    st.title("🎨 Métricas con Proporción 4:5 y Tema Oscuro")

    # Ejemplo de métrica 1: Total de Días de Reproducción
    label1 = "🎧 Total de Días de Reproducción"
    value1 = 326.72

    # Generar y mostrar la métrica 1
    filename1 = create_metric_plot(label1, value1, filename="metric_total_days_4_5.png")
    st.image(filename1, caption="Métrica: Total de Días de Reproducción")

    # Botón para descargar la métrica 1
    with open(filename1, "rb") as file1:
        st.download_button(
            label="📥 Descargar Métrica: Total de Días de Reproducción",
            data=file1,
            file_name="metric_total_days_4_5.png",
            mime="image/png"
        )

    # Ejemplo de métrica 2: Total de Días Reproducidos por BTS
    label2 = "🎧 Total de Días Reproducidos por BTS"
    value2 = 50.76

    # Generar y mostrar la métrica 2
    filename2 = create_metric_plot(label2, value2, filename="metric_bts_days_4_5.png")
    st.image(filename2, caption="Métrica: Total de Días Reproducidos por BTS")

    # Botón para descargar la métrica 2
    with open(filename2, "rb") as file2:
        st.download_button(
            label="📥 Descargar Métrica: Total de Días Reproducidos por BTS",
            data=file2,
            file_name="metric_bts_days_4_5.png",
            mime="image/png"
        )

# Nota: Si deseas que esta página se pueda ejecutar de manera independiente, puedes agregar:
if __name__ == "__main__":
    render_page()
