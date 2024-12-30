# charts.py
import pandas as pd
import plotly.express as px

def create_trend_chart():
    # Simulación de datos (reemplázalo con tus datos reales)
    data = {
        'date': pd.date_range(start='2016-01-01', periods=84, freq='M'),
        'min_played': [300 + (i % 12) * 10 + (i // 12) * 50 for i in range(84)]
    }
    df_filtrado = pd.DataFrame(data)
    df_filtrado['year'] = df_filtrado['date'].dt.year
    df_filtrado['month'] = df_filtrado['date'].dt.month
    df_grouped = df_filtrado.groupby(['year', 'month'])['min_played'].sum().reset_index()

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
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        )
    )
    return fig
