import streamlit as st
import plotly.express as px
import plotly.graph_objects as go 
import pandas as pd
import numpy as np

from funciones import vendedor_data, jefatura_data

def main_pais(df_mapa):
    
    
    años_lista = vendedor_data.obtener_años(df_mapa).tolist()
    año = st.selectbox("📅 Seleccionar Año",options=años_lista, index=len(años_lista) - 1)
    df_mapa_filtrado = df_mapa.query(
        "año==@año"
    )

    df_venta_pais = jefatura_data.obtener_venta_calculada_ciudad(df_mapa_filtrado)
    df_venta_pais['text'] = df_venta_pais['Ciudad'] + '<br>Total ' + (df_venta_pais['Total']).astype(str)


    scale = df_venta_pais["Total"].mean()/ 1000
    x = np.percentile(df_venta_pais["Total"], 33)
    y = np.percentile(df_venta_pais["Total"], 66)
    df_venta_pais["color"] = df_venta_pais["Total"].apply(lambda v: "#cb4e47" if v <= x else "#fada50" if v <= y else "#00573f")

    colores = {
        "#cb4e47": "Ciudades con Baja Venta",
        "#fada50": "Ciudades con Venta Media",
        "#00573f": "Ciudades con Alta Venta"
    }

    fig = go.Figure()
    for color, leyenda in colores.items():
        df_filtro = df_venta_pais[df_venta_pais["color"] == color]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=df_filtro['lon'],
            lat=df_filtro['lat'],
            text=df_filtro['text'],
            marker=dict(
                size=df_filtro['Total']/scale,
                color=color,
                line_color='white',  # Bordes blancos para contraste
                line_width=0.5,
                sizemode='area'
            )   ,
            name=leyenda
        ))
    
    fig.update_layout(
        title_text=f'{año} US City Ventas',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='#20212b',  # Color de la tierra negro
            lakecolor='#20212b',  # Color de los lagos negro
            bgcolor='#20212b'  # Fondo del mapa negro
        ),
        paper_bgcolor="#20212b",  # Fondo negro general
        plot_bgcolor="#20212b",  # Fondo negro del gráfico
        font=dict(color="white"),  # Texto en blanco para visibilidad
        height=800,  # Aumentar el tamaño del gráfico
        width=1000
    )

    st.plotly_chart(fig, use_container_width=True)
