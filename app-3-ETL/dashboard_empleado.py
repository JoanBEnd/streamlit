import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import limpieza
import extraccion



st.set_page_config(page_title="Reporte de ventas", layout="wide")

def sidebar():
    miDFrame = limpieza.devolver_dataframe()
    st.sidebar.header("Filtros:")
#Filtro años
    año = st.sidebar.selectbox(
        label="Seleccionar Año",
        options=extraccion.obtener_años(miDFrame) 
    )

#Filtro empleados
    mis_empleados = extraccion.obtener_empleado(miDFrame).tolist()
    opciones_Empleo = ["Todos"] + mis_empleados

    empleados = st.sidebar.selectbox(
        "Seleccion Empleado",
        options= opciones_Empleo
    )

    titulo_asesor= ""
    if "Todos" in empleados:
        empleados = mis_empleados
    else:
        titulo_asesor = "- " + empleados

#Filtro categorias
    mis_categorias = extraccion.obtener_categoria(miDFrame).tolist()
    opciones = ["Todos"] + mis_categorias

    categoria = st.sidebar.selectbox(
        "Seleccionar Categoria",
        options= opciones
    )

    if "Todos" in categoria:
        categoria = mis_categorias


  

    df_venta_filtrado = miDFrame.query(
        "Año==@año & Categoria==@categoria & Empleado==@empleados" 
    )

    df_venta_todos_por_año = miDFrame.query(
        "Año==@año & Categoria==@mis_categorias & Empleado==@mis_empleados" 
    )

    df_filtro_año_empleado = miDFrame.query(
        "Año==@año & Categoria==@categoria  & Empleado==@mis_empleados" 
    )
    st.sidebar.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)


    st.header(f"📊 Dashboard de Ventas { titulo_asesor }")
    #st.write(df_venta_filtrado)
    st.markdown("---")


    with st.sidebar:
        selected = option_menu(
            menu_title="Menú Principal",
            options=["Empleados", "Productos"],
            icons=["person", "archive-fill"],
            menu_icon="cast",
            default_index = 0
        )
    
    if selected == "Empleados":
         
        card_productos_venta(df_venta_filtrado, df_venta_todos_por_año)
        grafica_lineas_empleado(df_venta_filtrado)
    
    if selected == "Productos":
        
        grafica_de_barras(df_venta_filtrado)
        grafica_lineas_empleado(df_filtro_año_empleado)



def card_productos_venta(df_venta_filtrado, df_venta_todos_por_año):
    
    card_producto = extraccion.obtener_total_producto(df_venta_filtrado)

    col_producto, col_ventas, col_porcentaje = st.columns(3, gap="large")
    with col_producto:
        st.markdown("""
                <div style="text-align: center; padding: 10px; background-color: #181d27; border-radius: 10px;">
                    <h2 style="font-size: 30px; font-weight: bold;">📌 Total Productos</h2>
                    <h1   style="color: #fafafa; font-size: 55px; font-weight: bold;">{:,}</h1>
                </div>
                """.format(card_producto), unsafe_allow_html=True
        )

    card_ventas = extraccion.obtener_total_ventas(df_venta_filtrado)
    with col_ventas:
        st.markdown("""
                <div style="text-align: center; padding: 10px; background-color: #181d27; border-radius: 10px;">
                    <h2 style="font-size: 30px; font-weight: bold;">📌 Total Ventas </h2>
                    <h1   style="color: #fafafa; font-size: 55px; font-weight: bold;">${:,}</h1>
                </div>
                """.format(card_ventas), unsafe_allow_html=True )

    Total_Venta = df_venta_todos_por_año["Total"].sum()
    card_porcentaje = extraccion.obtener_porcentaje(df_venta_filtrado,Total_Venta)
    with col_porcentaje:
        st.markdown("""
                <div style="text-align: center; padding: 10px; background-color: #181d27; border-radius: 10px;">
                    <h2 style="font-size: 25px; font-weight: bold;">📌 Porcentaje de Venta </h2>
                    <h1 style="color: #fafafa; font-size: 55px; font-weight: bold;">{:,}%</h1>
                </div>
                """.format(card_porcentaje), unsafe_allow_html=True )

    
    st.markdown("---")



def grafica_de_barras(df_venta_filtrado):

    col_barras_producto, col_barras_ventas = st.columns(2, gap="large")

    with col_barras_producto:
        productos_totales = extraccion.obtener_producto_cantidades(df_venta_filtrado)
        st.subheader("Total de productos vendidos.") 
        barras_producto =  px.bar(productos_totales, 
                                  x=productos_totales["Cantidad"], 
                                  y= productos_totales["Producto"], 
                                  orientation="h",
                                  color_discrete_sequence=['#7F45EE'], 
                                  text_auto= True)
        
        st.plotly_chart(barras_producto, use_container_width=True)


    with col_barras_ventas:
        productos_totales = extraccion.obtener_producto_ventas(df_venta_filtrado)
        st.subheader("Venta total por producto.") 
        barras_producto =  px.bar(productos_totales, 
                                  x=productos_totales["Total"], 
                                  y= productos_totales["Producto"], 
                                  orientation="h",
                                  color_discrete_sequence=['#7F45EE'], 
                                  text_auto= True )
        st.plotly_chart(barras_producto, use_container_width=True)

    st.markdown("---")

def grafica_lineas_empleado(df_venta_filtrado):     
     
    col_meses_producto_empleado, col_meses_venta_empleado = st.columns(2, gap='large')
    
    with col_meses_producto_empleado:        
        st.subheader("Evolución Mensual del Total Producto Vendido por Empleado.") 
        empleado_venta_producto = extraccion.obtener_venta_empleado_productos_por_mes(df_venta_filtrado)
        graf_lineas_producto = px.line(empleado_venta_producto, x="Mes_Abrev", y="Cantidad",
                                            color="Empleado",
                                            markers=True,  
                                            #text="Cantidad",
                                            labels={"Cantidad": "Productos Vendidos", "Mes_Abrev": "Meses"}
                                            )
        st.plotly_chart(graf_lineas_producto, use_container_width=True)

    
    with col_meses_venta_empleado:
        st.subheader("Evolución Mensual del Total Venta por Empleado.") 
        empleado_venta_total = extraccion.obtener_venta_empleado_total_por_mes(df_venta_filtrado)
        graf_lineas_producto_venta = px.line(empleado_venta_total, x="Mes_Abrev", y="Total",
                                            color="Empleado",
                                            markers=True,  
                                            #text="Total",
                                            labels={"Total": "Venta Total", "Mes_Abrev": "Meses"}
                                            )
        
 
        
        st.plotly_chart(graf_lineas_producto_venta, use_container_width=True)
    st.markdown("---")


def grafica_lineas_empleado(df_filtro_año_empleado):     
     
    col_meses_producto_empleado, col_meses_venta_empleado = st.columns(2, gap='large')
    
    with col_meses_producto_empleado:        
        st.subheader("Evolución Mensual del Total Categoria Vendido por Empleado.") 
        empleado_venta_producto = extraccion.obtener_venta_empleado_categoria_por_mes(df_filtro_año_empleado)
        graf_lineas_producto = px.line(empleado_venta_producto, x="Mes_Abrev", y="Cantidad",
                                            color="Categoria",
                                            markers=True,  
                                            #text="Cantidad",
                                            labels={"Cantidad": "Total por Categoria", "Mes_Abrev": "Meses"}
                                            )
        st.plotly_chart(graf_lineas_producto, use_container_width=True)

    
    with col_meses_venta_empleado:
        st.subheader("Evolución Mensual del Total Categoria Vendida por Empleado.") 
        empleado_venta_total = extraccion.obtener_venta_empleado_total_categoria_por_mes(df_filtro_año_empleado)
        graf_lineas_producto_venta = px.line(empleado_venta_total, x="Mes_Abrev", y="Total",
                                            color="Categoria",
                                            markers=True,  
                                            #text="Total",
                                            labels={"Total": "Venta Total", "Mes_Abrev": "Meses"}
                                            )
        
 
        
        st.plotly_chart(graf_lineas_producto_venta, use_container_width=True)
    st.markdown("---")


sidebar()