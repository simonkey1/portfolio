from metric_plot import create_metric_plot

def generate_dark_metric(label, value, filename="dark_metric_plot.png"):
    """
    Genera una métrica en tema oscuro utilizando Plotly.
    
    Args:
        label (str): Texto para la etiqueta de la métrica (ej. "Total de Días").
        value (float): Valor numérico de la métrica (ej. 326.72).
        filename (str): Nombre del archivo de salida (por defecto "dark_metric_plot.png").
    
    Returns:
        str: Ruta al archivo de la métrica generada.
    """
    # Reutiliza la función de metric_plot.py para generar la métrica
    return create_metric_plot(label, value, filename)
