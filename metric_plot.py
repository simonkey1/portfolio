import plotly.graph_objects as go

def create_metric_plot(label, value, filename="metric_plot.png"):
    """
    Genera una métrica como gráfico con tema oscuro en proporción 4:5 (1080x1350 píxeles).
    
    Args:
        label (str): Texto para la etiqueta de la métrica (ej. "Total de Días").
        value (float): Valor numérico de la métrica (ej. 326.72).
        filename (str): Nombre del archivo de salida (por defecto "metric_plot.png").
    
    Returns:
        str: Ruta al archivo de la métrica generada.
    """
    # Crear el gráfico
    fig = go.Figure()

    # Configurar la métrica
    fig.add_trace(go.Indicator(
        mode="number",
        value=value,
        title={"text": label, "font": {"size": 60}},  # Tamaño del texto del título
        number={"font": {"size": 150, "color": "deepskyblue"}},  # Tamaño del número
    ))

    # Personalizar el diseño (proporción 4:5)
    fig.update_layout(
        width=1080,  # Ancho 1080 píxeles
        height=1350,  # Altura 1350 píxeles
        paper_bgcolor="rgb(18,18,18)",  # Fondo oscuro
        font=dict(color="white"),  # Texto blanco
        margin=dict(t=100, b=100, l=100, r=100)  # Márgenes ajustados
    )

    # Exportar como imagen con mayor calidad
    fig.write_image(filename, scale=2)  # Escala para alta resolución

    return filename
