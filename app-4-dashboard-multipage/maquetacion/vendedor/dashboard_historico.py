import streamlit as st
import plotly.express as px
import urllib.parse
from logica_app import extraccion_venta
from funciones import vendedor_data
 

def main():
    # # Verificar parámetros URL y sesión
    # if "role" in st.query_params or "idUser" in st.query_params:
    #     del st.query_params["role"]
    #     del st.query_params["idUser"]
    #     st.rerun()  # 🔄 Recargar para limpiar la URL

    if "role" not in st.session_state:
        st.query_params["role"] = ""
        st.rerun()
    
    if st.session_state.role != "Vendedor":
        st.error("Acceso no autorizado")
        st.stop()

    
    
    # Tu contenido normal aquí
    id_Usuario = st.session_state.idUser    
    st.markdown("<h1 style='text-align: center; color: #00ff00;'>📊 Dashboard de Ventas - Histórico</h1>", unsafe_allow_html=True)

    df_Vendedor = extraccion_venta.obtener_dataframe_vendedor(int(id_Usuario))
    
    
    #st.write(df_Vendedor.head())
    col_año, col_ciudad = st.columns(2)
    with col_año:
        año = st.selectbox(
             label="📅 Seleccionar Año",
             options= vendedor_data.obtener_años(df_Vendedor)
         )

    with col_ciudad:
        ciudad = st.selectbox(
            label= "🏙️ Seleccionar Ciudad", 
            options= vendedor_data.obtener_ciudades(df_Vendedor)
        )
   


    df_vendedor_filtro = df_Vendedor.query(
        "año ==@año & Ciudad==@ciudad"
    )
    st.markdown("---")
    
    mostrar_metricas(df_vendedor_filtro)
    mostrar_grafica_barra(df_vendedor_filtro, df_Vendedor)
    mostrar_grafica_lineas(df_vendedor_filtro, df_Vendedor,año, ciudad )

    #st.write(df_vendedor_filtro)
def mostrar_metricas(df_vendedor_filtro):
    
    # Obtener métricas
    card_venta = vendedor_data.obtener_Total_venta(df_vendedor_filtro)
    card_producto = vendedor_data.obtener_Total_producto(df_vendedor_filtro)
    card_venta_mayor = vendedor_data.obtener_venta_mayor(df_vendedor_filtro)
     
    col_total_venta, col_total_producto, col_3  = st.columns(3)

    with col_total_venta:    
          mes_max = card_venta_mayor["mes_completo"]
          venta_max = card_venta_mayor["Total"]
          st.markdown(f"""
                <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                    <h3 style="color: #ffffff; font-size: 20px;">📆 {mes_max} > Venta </h3>        
                    <h1 style="color: #00ff00; font-size: 30px; font-weight: bold;">💲 {venta_max:,.2f}</h1>
                </div>
            """, unsafe_allow_html=True)  
    
    
    with col_total_producto:
        st.markdown(f"""
            <div  style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                    <h3 style="color: #ffffff; font-size: 20px;">📦 Productos Vend. Anual</h3>
                    <h1 style="color: #fafafa; font-size: 30px; font-weight: bold;"> {card_producto}</h1>                
            </div>
        """, unsafe_allow_html=True)

    with col_3:
            
        st.markdown("""
            <div  style="text-align: center; padding: 15px; background: linear-gradient(135deg, #181d27, #28334A); border-radius: 10px;">
                    <h3 style="color: #ffffff; font-size: 20px;">💰 Venta Anual</h3>
                    <h1 style="color: #fafafa; font-size: 30px; font-weight: bold;"> 💲 {:,}</h1>                
            </div>
        """.format(card_venta), unsafe_allow_html=True) 
    st.markdown("---")


def mostrar_grafica_barra(df_vendedor_filtro, df_Vendedor):

    #with col_barra_producto:        
    #st.markdown("<h2 style='text-align: center; color: #fafafa; font-size: 21px'>📊 Venta Total por Producto</h2>", unsafe_allow_html=True)

    st.markdown("<h2>📊 Venta Categoria - Producto</h2>", unsafe_allow_html=True)
    df_venta_producto = vendedor_data.obtener_venta_producto(df_vendedor_filtro)

    mis_categorias = vendedor_data.obtener_categorias(df_Vendedor).tolist()
    opciones_categoria = ["Todos"] + mis_categorias
    Categoria = st.selectbox("🎯 Seleccionar Categoría", options=opciones_categoria)

    if "Todos" in Categoria:
        Categoria = mis_categorias

    df_venta_categoria = df_vendedor_filtro.query("Categoria == @Categoria")
    df_venta_producto = vendedor_data.obtener_venta_producto(df_venta_categoria)

    grafica_barra = px.bar(df_venta_producto, x="Producto", y="Total", 
                     color="Total", 
                     color_continuous_scale="viridis", 
                     text_auto=".2s",  # Muestra los valores encima de las barras
                     labels={"Total": "Total de Ventas"})

    grafica_barra.update_layout(
            title="🔹 Ventas por Producto",
            xaxis_title="Producto",
            yaxis_title="Ventas",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
    st.plotly_chart(grafica_barra, use_container_width=True)
    st.markdown("---")    

def mostrar_grafica_lineas(df_vendedor_filtro, df_Vendedor, año, ciudad):

    #with col_linea_venta:
    data = vendedor_data.obtener_años(df_Vendedor).tolist()
    primer_año = data[0]
    
    if primer_año == año:
        df_venta_mes = vendedor_data.obtener_venta_mensual_historico(df_vendedor_filtro)
    else:
        años_comparativos = [primer_año, año]
        df_vendedor_filtro_año = df_Vendedor.query(
            "año ==@años_comparativos & Ciudad==@ciudad"
        )
        df_venta_mes = vendedor_data.obtener_venta_mensual_historico(df_vendedor_filtro_año)    

    
    st.markdown("<h2>📈 Comparativo Año Seleccionado - Año Previo</h2>", unsafe_allow_html=True)
    grafica_linea = px.line(df_venta_mes, 
                                x="mes", 
                                y="Total", 
                                color="año",
                                markers=True
                                #color_discrete_map=colores_personalizados  
                                )
    st.plotly_chart(grafica_linea, use_container_width=True)



    st.markdown("---")        

    