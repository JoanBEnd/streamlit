import streamlit as st
import plotly.express as px
from logica_app import extraccion_venta
from funciones import vendedor_data
import pandas as pd

def main():
    # Verificar sesión
    if "role" not in st.session_state:
        st.query_params["role"] = ""
        st.rerun()

    if st.session_state.role != "Vendedor":
        st.error("Acceso no autorizado")
        st.stop()

    id_Usuario = st.session_state.idUser
    st.markdown("<h1 style='text-align: center; color: #00ff00;'>📊 Dashboard de Ventas</h1>", unsafe_allow_html=True)

    df_Vendedor = extraccion_venta.obtener_dataframe_vendedor(int(id_Usuario))

    col_año, col_ciudad = st.columns(2)
    df_anios = vendedor_data.obtener_años(df_Vendedor)

    with col_año:
        año = st.selectbox("📅 Seleccionar Año", options=df_anios.max())

    with col_ciudad:
        ciudad = st.selectbox("🏙️ Seleccionar Ciudad", options=vendedor_data.obtener_ciudades(df_Vendedor))

    df_vendedor_filtro = df_Vendedor.query("año == @año & Ciudad == @ciudad")
    st.markdown("---")
    mostrar_metricas(df_vendedor_filtro)
    mostrar_grafica_barra(df_vendedor_filtro, df_Vendedor)
    mostrar_grafica_lineas(df_vendedor_filtro)


def mostrar_metricas(df_vendedor_filtro):

    # Obtener métricas
    card_venta = vendedor_data.obtener_Total_venta(df_vendedor_filtro)
    card_producto = vendedor_data.obtener_Total_producto(df_vendedor_filtro)
    card_venta_mayor = vendedor_data.obtener_venta_mes_actual(df_vendedor_filtro)

    mes_max = card_venta_mayor["mes_completo"]
    venta_max = card_venta_mayor["Total"]

    # Sección de KPI

    col_total_venta, col_total_producto, col_venta_anual = st.columns(3)

    with col_total_venta:
        st.markdown(f"""
            <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                <h3 style="color: #ffffff; font-size: 20px;">📆 Venta en {mes_max} </h3>        
                <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">💲 {venta_max:,.2f}</h1>
            </div>
        """, unsafe_allow_html=True)

    with col_total_producto:
        st.markdown(f"""
            <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                <h3 style="color: #ffffff; font-size: 20px;">📦 Productos Vendidos</h3>
                <h1 style="color: #fafafa; font-size: 30px; font-weight: bold;">{card_producto}</h1>                
            </div>
        """, unsafe_allow_html=True)

    with col_venta_anual:
        st.markdown(f"""
            <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                <h3 style="color: #ffffff; font-size: 20px;">💰 Venta Anual</h3>
                <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">💲 {card_venta:,.2f}</h1>                
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

def mostrar_grafica_barra(df_vendedor_filtro, df_Vendedor):

    # Botón para mostrar/ocultar detalles (simulando un expander abierto)
    if "mostrar_detalles" not in st.session_state:
        st.session_state["mostrar_detalles"] = True

    if st.button("🔄 Ocultar/Mostrar Venta Categoria"):
        st.session_state["mostrar_detalles"] = not st.session_state["mostrar_detalles"]

    if st.session_state["mostrar_detalles"]:
        # Sección de ventas por producto (expander simulado)
        st.markdown("<h2>📊 Venta Categoria - Producto</h2>", unsafe_allow_html=True)

        mis_categorias = vendedor_data.obtener_categorias(df_Vendedor).tolist()
        opciones_categoria = ["Todos"] + mis_categorias
        Categoria = st.selectbox("🎯 Seleccionar Categoría", options=opciones_categoria)

        if "Todos" in Categoria:
            Categoria = mis_categorias

        df_venta_categoria = df_vendedor_filtro.query("Categoria == @Categoria")
        df_venta_producto = vendedor_data.obtener_venta_producto(df_venta_categoria)

        # Gráfico mejorado
        fig = px.bar(df_venta_producto, x="Producto", y="Total", 
                     color="Total", 
                     color_continuous_scale="viridis", 
                     text_auto=".2s",  # Muestra los valores encima de las barras
                     labels={"Total": "Total de Ventas"})

        fig.update_layout(
            title="🔹 Ventas por Producto",
            xaxis_title="Producto",
            yaxis_title="Ventas",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

    
def mostrar_grafica_lineas(df_vendedor_filtro):
        
        st.markdown("<h2>📈 Evolución Mensual del Total</h2>", unsafe_allow_html=True)
        #st.markdown("<h2 style='text-align: center; color: #fafafa; font-size: 21px'>📈 Evolución Mensual del Total Venta por Año</h2>", unsafe_allow_html=True)
        df_venta_mes = vendedor_data.obtener_venta_mensual(df_vendedor_filtro)
        persona = df_venta_mes["Empleado"].unique()[0]
        
        colores_personalizados = { 
            persona: "#2ca02c"
                }
        grafica_linea = px.line(df_venta_mes, 
                                x="mes", 
                                y="Total", 
                                color="Empleado",
                                markers=True, 
                                color_discrete_map=colores_personalizados  
                                )
        st.plotly_chart(grafica_linea, use_container_width=True)   