import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import limpieza 
import extraccion

#Asignamos un titulo a la pestaña de la página y el layout = "wide" nos permite hacer uso de todo el ancho de la página
st.set_page_config(page_title="REPORTE TRENDING - TIENDA", layout='wide')

#Creamos un titulo general
st.header("📊 Dashboard de Ventas")
st.markdown("---")
#Obtenemos el dataframe desde otro archivo que se ha encargado de limpiar ese dataframe
dt_retail = limpieza.devolver_dataFrame()

#Creamos el menu lateral donde van los filtros.
st.sidebar.header("Filtros")

#Creamos el filtro de años con un multiselector
año = st.sidebar.multiselect(
    "Filtrar por años",
    options=extraccion.obtener_filtro_años(dt_retail),
    default=extraccion.obtener_filtro_años(dt_retail)
)


list_producto =  extraccion.obtener_filtro_producto(dt_retail).tolist()
opciones = ["Todos"] + list_producto

#Creamos el filtro de productos con un selector único
productos = st.sidebar.selectbox(
    "Filtrar por productos",
    options= opciones  
)

if "Todos" in productos:
    productos = list_producto

#Filtramos del dataframe original lo seleccionado en la opción de filtros:
# La función .query() en pandas permite filtrar un DataFrame usando una sintaxis más compacta y legible.
df_seleccion = dt_retail.query(
    "Year==@año & `Product Category`==@productos"
)




def card_venta_producto():
    col_card_productos, col_card_ventas = st.columns(2, gap='large')
    #Creamos el card de total de productos
    with col_card_productos:
        card_producto = extraccion.obtener_total_producto(df_seleccion)
        #Con markdown podemos hacer uso de html para poder crear en este caso nuestro card.
        st.markdown("""
                    <div style="text-align: center; padding: 20px; background-color: #181d27; border-radius: 10px;">
                        <h2>📌 Total Productos</h2>
                        <h1  style="color: #fafafa; font-size: 55px; font-weight: bold;">{:,} </h1>                    
                    </div>
                    """.format(card_producto), unsafe_allow_html=True)
    
    #Creamos el card de total de productos
    with col_card_ventas:
        card_ventas = extraccion.obtener_total_ventas(df_seleccion)
        #Con markdown podemos hacer uso de html para poder crear en este caso nuestro card.
        st.markdown("""
                    <div style="text-align: center; padding: 20px; background-color: #181d27; border-radius: 10px;">
                        <h2>📌 Total Ventas</h2>
                        <h1 style="color: #fafafa; font-size: 55px; font-weight: bold;">${:,.0f}</h1>
                    </div>
                    """.format(card_ventas), unsafe_allow_html=True)  

    st.markdown("---")





def grafica_lineas_Ventas():

    col_meses_ventas, col_meses_productos = st.columns(2, gap='large')
    colores_personalizados = { 
    2022: "#2ca02c",  # Verde
    2023: "#7f45ee",  # Morado 
    2024: "#385ab9"   # Azul
    }


    with col_meses_ventas:
        
        st.subheader("Evolución Mensual del Total Venta por Año.") 
        #obtenemos un dataframe filtrado de acuerdo a los campos que necesitamos para la gráfica     
        df_filtro = extraccion.obtener_tabla_mes_año_venta(df_seleccion) 

        fig_line = px.line(df_filtro, x="Month_less", y="Total Amount", 
                           color="Year",
                           color_discrete_map=colores_personalizados,
                           markers=True,  
                           text="Total Amount",
                           labels={"Total Amount": "Total Venta", "Month_less": "Meses"}
                           )
        #Configuramos el gráfico
        fig_line.update_traces(textposition="top center", 
                               texttemplate="%{text:.2s}", 
                               textfont_size=14
                               )

        fig_line.update_layout(legend_title_text="Años"  # Personalizar título de la leyenda
                               )
        st.plotly_chart(fig_line, use_container_width=True) #Con esto podemos visualizar el gráfico


    with col_meses_productos:
        st.subheader("Evolución Mensual de Productos vendidos por Año.")      
        df_filtro = extraccion.obtener_tabla_mes_año_producto(df_seleccion) 
        
        #Comenzamos a crear el grafico de líneas
        fig_line_producto_mensual = px.line(df_filtro, x="Month_less", y="Quantity", 
                                            color="Year",
                                            color_discrete_map=colores_personalizados,
                                            markers=True, text="Quantity",
                                            labels={"Quantity": "Cantidad", "Month_less":"Meses"}
                                            )
        #Comenzamos a darle un diseño más personalizado
        fig_line_producto_mensual.update_traces(textposition="top center", 
                                                texttemplate="%{text:.2s}", 
                                                textfont_size=14
                                                )
        
        st.plotly_chart(fig_line_producto_mensual, use_container_width=True) #Con esto podemos visualizar el gráfico


    st.markdown("---")
 
 

def grafica_barras():
    col_rango_edades,  col_rango_edades_venta = st.columns(2, gap="large")
    
    with col_rango_edades:
        #Comenzamos a crear el rango de edad y el total de personas por cada rango de edad
        count, bins = np.histogram(df_seleccion["Age"], bins=7)
        df_histograma = pd.DataFrame({
            "Rango Edad": [f"{int(bins[i])} - {int(bins[i+1])}" for i in range(len(bins)-1)],
            "Frecuencia":count
        })

        df_histograma.reset_index(drop=True)  
        st.subheader("Distribución de Clientes por Rango de Edad.")      
        #Comenzamos a crear la gráfica    
        fig_histograma = px.histogram(df_histograma, y="Rango Edad", x="Frecuencia", nbins=7, text_auto=True,
                              orientation='h', 
                              color_discrete_sequence=['#7F45EE'],
                           labels={"Frecuencia": "Cantidad de personas", "Rango Edad": "Rango Edad"}
                                ) 
        #Comenzamos a darle un diseño más personalizado
        fig_histograma.update_layout(xaxis_title="Cantidad de Personas") 
        st.plotly_chart(fig_histograma, use_container_width=True) #Con esto podemos visualizar el gráfico
    
    with col_rango_edades_venta:
        st.subheader("Venta Total por Rango de edades.")  
        #Comenzamos a crear la gráfica    
        fig_histograma_venta = px.histogram(df_seleccion, y="Rango_Edad", x="Total Amount", nbins=7, text_auto=True,
                                  orientation = 'h',
                                  color_discrete_sequence=['#7F45EE'],                                  
                                  labels={"Rango_Edad": "Rango Edad"}
                                  )
        #Comenzamos a darle un diseño más personalizado
        fig_histograma_venta.update_layout(xaxis_title="Total de Ventas") 
        
        st.plotly_chart(fig_histograma_venta, use_container_width=True) #Con esto podemos visualizar el gráfico


card_venta_producto()
grafica_lineas_Ventas()
grafica_barras()
