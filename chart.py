import pandas as pd
import plotly.express as px

def create_trend_chart():
    # Carga de datos reales (reemplaza con la ruta de tu archivo)
    df_final = pd.read_csv("df_final.csv")  # Cambia esto a tu fuente de datos

    # Convertir 'ts' en formato datetime
    df_final['date'] = pd.to_datetime(df_final['ts'])

    # Extraer el año
    df_final['year'] = df_final['date'].dt.year

    # Eliminar zona horaria de 'date'
    df_final['date'] = df_final['date'].dt.tz_localize(None)

    # Definir rango de fechas
    fecha_inicio = pd.Timestamp("2017-01-01")
    fecha_fin = pd.Timestamp("2024-12-29")

    # Filtrar el DataFrame dentro del rango de fechas
    df_filtrado = df_final[(df_final['date'] >= fecha_inicio) & (df_final['date'] <= fecha_fin)]

    # Extrae mes y año para agrupar
    df_filtrado['month'] = df_filtrado['date'].dt.month

    df_filtrado['min_played'] = df_filtrado['ms_played'] / 60000

    # Agrupar los datos por año y mes
    df_grouped = df_filtrado.groupby(['year', 'month'])['min_played'].sum().reset_index()

    # Definición de colores para los años
    colors = {
        2016: 'steelblue',
        2017: 'mediumseagreen',
        2018: 'gold',
        2019: 'purple',
        2020: 'crimson',
        2021: 'peru',
        2022: 'darkkhaki',
        2023: 'cadetblue',
        2024: 'darkorange',
    }

    # Crear el gráfico
    fig = px.line(
        df_grouped,
        x='month',
        y='min_played',
        color='year',
        title='Tendencia de minutos escuchados por mes a lo largo de los años',
        labels={'month': 'Mes', 'min_played': 'Minutos Escuchados', 'year': 'Año'},
        markers=True,
        color_discrete_map=colors
    )

    # Ajustar las etiquetas de los meses, centrar el título y la leyenda
    fig.update_layout(
        title={
            'text': 'Tendencia de minutos escuchados por mes a lo largo de los años',
            'x': 0.5,  # Centrar título horizontalmente
            'xanchor': 'center'
        },
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
            title_font=dict(size=14, color='deepskyblue'),  # Títulos del eje X más brillantes
            tickfont=dict(size=12, color='deepskyblue')  # Etiquetas del eje X más brillantes
        ),
        yaxis=dict(
            title_font=dict(size=14, color='deepskyblue'),  # Títulos del eje Y más brillantes
            tickfont=dict(size=12, color='deepskyblue')  # Etiquetas del eje Y más brillantes
        ),
        legend_title={
            'text': 'Año'
        },
        legend=dict(
            x=0.5,  # Centrar la leyenda horizontalmente
            xanchor='center',
            orientation='h'
        )
    )
    return fig
