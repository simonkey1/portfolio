import streamlit as st
from chart import create_trend_chart  # Importa el gráfico desde charts.py

# Título llamativo
st.title("🎵 Tu Historia Musical: Minutos Escuchados Mes a Mes")

# Subtítulo interesante
st.subheader("Explora cómo han evolucionado tus hábitos de escucha a lo largo de los años")

# Texto contextual
st.markdown("""
Este análisis muestra los minutos de música que escuchaste mes a mes desde 2016 hasta la fecha. 
📊 ¿Qué descubrimos? Patrones interesantes en las temporadas de mayor reproducción, 
como aumentos en verano y bajadas en invierno. ¿Se reflejan tus momentos favoritos aquí? 🤔
""")

# Generar y mostrar el gráfico
fig = create_trend_chart()
st.plotly_chart(fig, use_container_width=True)

# Botón para descargar el gráfico como imagen
if st.button("Descargar gráfico como imagen"):
    create_trend_chart(save_as_image=True, filename="trend_chart_download.png")
    st.markdown("✅ **Gráfico descargado como `trend_chart_download.png`.**")

# Pie de página inspirador
st.markdown("""
**🎯 Nota:** La música tiene el poder de marcar nuestras vidas. Reflexiona sobre tus momentos
más importantes y los sonidos que los acompañaron. 
¡Comparte tu propia tendencia y etiqueta a tus amigos! 🎶
""")
