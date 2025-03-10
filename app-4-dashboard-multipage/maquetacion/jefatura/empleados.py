import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from funciones import vendedor_data, jefatura_data



def main_empleado(df_mapa):
    
    col_año, col_empleado, col_empleado_top = st.columns(3)

    año_lista = vendedor_data.obtener_años(df_mapa).tolist()
    opciones_año = ["Todos"] + año_lista
    with col_año:
        año =  st.selectbox("📅 Seleccionar Año", options=opciones_año, index= len(opciones_año) -1 )
    

    empleado_lista = jefatura_data.obtener_empleados(df_mapa).tolist()
    opciones_empleado = ["Todos"] + empleado_lista

    with col_empleado:
        empleado = st.selectbox("Seleccionar Empleados:", options= opciones_empleado)

    if "Todos" in str(año):
        año = año_lista
    
    if "Todos" in empleado:
        empleado = empleado_lista



    df_mapa_año =  df_mapa.query("año==@año")
    df_mapa_filtrado = df_mapa.query("año==@año  & Empleado==@empleado")


    with col_empleado_top:                
        df_empleado_top = jefatura_data.obtener_empleados_top(df_mapa_año)
        print("==============================================================")
        st.markdown(f""" 
                    <div style="text-align: center; padding: 15px;  border-radius: 10px;">
                        <h3 style="color: #ffffff; font-size: 20px;"> Empleado Top: </h3>
                        <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">🏆 {df_empleado_top.iloc[0]["Empleado"]} </h1>
                    </div>
                    """, unsafe_allow_html= True)
        
        print(df_empleado_top.iloc[0]["Empleado"],df_empleado_top.iloc[0]["Total"])



    tarjetas_empleados(df_mapa_filtrado, df_mapa_año)
    st.markdown("---")

    #col_lineas, col_barras = st.columns(2)
    col_lineas, col_sep, col_barras = st.columns([1, 0.1, 1])
    with col_lineas:
        grafica_empleado_mes_linea(df_mapa_filtrado)
    
    with col_sep:
        st.markdown("<div style='border-left: 2px solid white; height: 100%;'></div>", unsafe_allow_html=True)  # Línea divisoria

    
    with col_barras:
        
        grafica_empleado_mes_dia(df_mapa_filtrado)
    st.markdown("---")


    col_genero, col_sep_1, col_barras_productos = st.columns([1, 0.1, 1])
    
    with col_genero:
        grafica_empleado_ciudades(df_mapa_filtrado)
        
    
    with col_sep_1:
        st.markdown("<div style='border-left: 2px solid white; height: 100%;'></div>", unsafe_allow_html=True)  # Línea divisoria

    
    with col_barras_productos:
        grafica_pie_genero(df_mapa_filtrado)
    

    grafica_barra_productos(df_mapa_filtrado)
               

    


def tarjetas_empleados(df_mapa_filtrado, df_mapa_año):
    #Obtenemos la venta anual
    Total_vental_anual = df_mapa_año["Total"].sum()

    card_total_empleado = jefatura_data.obtener_venta_empleado(df_mapa_filtrado)
    
    col_venta_empleado, col_venta_total, col_porcentaje_total = st.columns(3)
    
    porcentaje = (card_total_empleado / Total_vental_anual) * 100
    with col_venta_empleado:
        st.markdown(f""" 
                    <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                        <h3 style="color: #ffffff; font-size: 20px;">💰 Venta Empleado: </h3>
                        <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">💲 {card_total_empleado:,.2f} </h1>
                    </div>
                    """, unsafe_allow_html= True)
    
    with col_venta_total:
        st.markdown(f""" 
                    <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                        <h3 style="color: #ffffff; font-size: 20px;">💰 Venta Anual: </h3>
                        <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">💲 {Total_vental_anual:,.2f} </h1>
                    </div>
                    """, unsafe_allow_html= True)
        
    
    with col_porcentaje_total:
        st.markdown(f""" 
                    <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                        <h3 style="color: #ffffff; font-size: 20px;">%󠀥 de Venta: </h3>
                        <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">% {porcentaje:,.2f} </h1>
                    </div>
                    """, unsafe_allow_html= True)


def grafica_empleado_mes_linea(df_mapa_filtrado):

    st.markdown("<h2>📈 Evolución Mensual de la Venta</h2>", unsafe_allow_html=True)
    df_venta_filtado = jefatura_data.obtener_venta_empleado_mes(df_mapa_filtrado)  
    
    grafica_linea = px.line(df_venta_filtado, x="mes", y="Total", color="Empleado",
                                markers=True)
    st.plotly_chart(grafica_linea, use_container_width= True)


def grafica_empleado_mes_dia(df_mapa_filtrado):
    st.markdown("<h2>📈 Evolución Venta por Dia</h2>", unsafe_allow_html=True)
    df_venta_filtado, ult_mes = jefatura_data.obtener_venta_empleado_dia(df_mapa_filtrado)  
     
    grafica_linea = px.line(df_venta_filtado, x="dia", y="Total", color="mes",
                                 markers=True)
    
    grafica_linea.update_layout(
            title=f"🔹 Comparativo entre los 2 últimos meses",
            xaxis_title="Dias",
            yaxis_title="Ventas",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
    st.plotly_chart(grafica_linea, use_container_width= True)


 

def grafica_empleado_ciudades(df_mapa_filtrado):
    
    st.markdown("<h2>📈 Venta por Ciudad</h2>", unsafe_allow_html=True)
    df_venta_filtrado_ciudad = jefatura_data.obtener_venta_empleado_ciudad(df_mapa_filtrado)
    grafica_barra_ciudad = px.bar(df_venta_filtrado_ciudad, x="Ciudad", y="Total",
                                    color="Total", 
                                    color_discrete_sequence=["#008013"],  # Un solo color azul #3498db                                   
                                   text_auto=".2s",  # Muestra los valores encima de las barras
                                  labels={"Total": "Total de Ventas"})

    st.plotly_chart(grafica_barra_ciudad, use_container_width=True)

def grafica_pie_genero(df_mapa_filtrado):
    st.markdown("<h2>📈 Porcentaje de la Venta por Género</h2>", unsafe_allow_html=True)
    st.write("")  
    st.write("") 
    df_venta_genero = jefatura_data.obtener_venta_empleado_genero(df_mapa_filtrado)
    grafica_pie_genero = px.pie(df_venta_genero,values="Total", names="Genero")

    st.plotly_chart(grafica_pie_genero, use_container_width=True)


def grafica_barra_productos(df_mapa_filtrado):
    st.markdown("<h2>📈 Venta por Categoria - Producto</h2>", unsafe_allow_html=True)
    

    categoria_lista = vendedor_data.obtener_categorias(df_mapa_filtrado).tolist()
    opciones_categoria = ["Todos"] + categoria_lista
    categoria = st.selectbox("Seleccionar Categoria", options=opciones_categoria)

    if "Todos" in categoria:
        categoria = categoria_lista

    df_categorias_filtrado  = df_mapa_filtrado.query("Categoria==@categoria" )   
    
    df_venta_producto = jefatura_data.obtener_venta_producto_empleado(df_categorias_filtrado)
    grafica_barra_producto = px.bar(df_venta_producto, x="Producto", y="Total",
                                    color="Total", 
                                    color_discrete_sequence=["#008013"],  # Un solo color azul #3498db
                                   #color_continuous_scale="viridis", 
                                   text_auto=".2s",  # Muestra los valores encima de las barras
                                  labels={"Total": "Total de Ventas"})
    
    st.plotly_chart(grafica_barra_producto, use_container_width=True)