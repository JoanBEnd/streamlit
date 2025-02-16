import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="REPORTE TRENDING - TIENDA", layout="wide")
st.title("📊 Reporte Tendencia de Venta - Temporada")


df_tiendas = pd.read_csv("data/shopping_trends.csv")
st.sidebar.header("Filtros")

categorias = df_tiendas["Season"].unique().tolist()
opciones = ["Todos"] + categorias

temporadas = st.sidebar.multiselect(
    "Seleccione la Temporada",
    options= opciones, #df_tiendas["Season"].unique()
    default= "Todos"
)

if "Todos" in temporadas:
    temporadas = categorias



mis_estados = df_tiendas["Location"].unique().tolist()
opciones_estado = ["Todos"] + mis_estados

locacion = st.sidebar.multiselect(
    "Seleccione el estado",
    options=opciones_estado,
    default="Todos"
)

if "Todos" in locacion:
    locacion = mis_estados


df_seleccion = df_tiendas.query(
    "Season==@temporadas & Location==@locacion"
)

def Home():
    
    #Obtener los totales de la base:
    card_tot_producto = float(df_seleccion["Customer ID"].count())
    card_sum_venta = float(df_seleccion["Purchase Amount (USD)"].sum())

    #Creando las columnas
    total_productos, total_venta = st.columns(2, gap='large')

    with total_productos:
        st.markdown("""
            <div style="text-align: center; padding: 20px; background-color: #191919; border-radius: 10px;">
                <h2 style="color: #fafafa;">📌 Total Productos</h2>
                <h1 style="color: #fafafa; font-size: 55px; font-weight: bold;">{:,}</h1>
            </div>
        """.format(card_tot_producto), unsafe_allow_html=True)

    with total_venta:
        st.markdown("""
            <div style="text-align: center; padding: 20px; background-color: #191919; border-radius: 10px;">
                <h2 style="color: #fafafa;">📌 Total Venta</h2>
                <h1 style="color: #fafafa; font-size: 55px; font-weight: bold;">${:,.0f}</h1>
            </div>
        """.format(card_sum_venta), unsafe_allow_html=True)

    st.markdown("---")




def graficas():


    #Crear columnas:
    column_edades, column_category = st.columns(2, gap="large")

    df_frecuencia = df_seleccion.groupby("Frequency of Purchases", as_index=False)["Purchase Amount (USD)"].sum()
    df_categoria = df_seleccion.groupby("Category", as_index=False)["Purchase Amount (USD)"].sum()




    with column_edades:
         
        st.subheader("Compras Totales por Rango de Edades.")
        fig_histograma = px.histogram(df_seleccion, y="Age", x="Purchase Amount (USD)", nbins=7, text_auto=True,
                              orientation='h', 
                              color_discrete_sequence=['#7F45EE']
                                ) 
        fig_histograma.update_layout(bargap=0.1)
        fig_histograma.update_traces(textfont_size=14)
        st.plotly_chart(fig_histograma,  use_container_width=True)


    with column_category:
        
        st.subheader("Compras Totales por Categoria.")
        fig_barra_categoria = px.bar(df_categoria, x="Category", y="Purchase Amount (USD)", text_auto=True, 
                              color_discrete_sequence=['#7a47ec'])
        fig_barra_categoria.update_traces(textfont_size=14)
        st.plotly_chart(fig_barra_categoria, use_container_width=True)


    st.markdown("---") 

    st.subheader("Compras por Frecuencia de compra.")
    fig_barra_frecuencia = px.bar(df_frecuencia, 
                                  x="Frequency of Purchases", 
                                  y="Purchase Amount (USD)",
                                  text_auto=True, 
                                  color_discrete_sequence=['#385AB9'] )
    fig_barra_frecuencia.update_traces(textfont_size=14)
    fig_barra_frecuencia.update_layout(bargap=0.3)
    st.plotly_chart(fig_barra_frecuencia, use_container_width=True)

    st.markdown("---")


Home()
graficas()