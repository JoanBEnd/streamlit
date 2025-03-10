import streamlit as st
import urllib.parse
import plotly.express as px 
from logica_app import extraccion_venta
import pandas as pd 
from maquetacion.jefatura import mapaPais, empleados

def main():
    # Verificar parámetros URL y sesión
    if "role" not in st.session_state:
        st.query_params["role"] = ""
        st.rerun()
    
    if st.session_state.role != "Jefe de Venta":
        st.error("Acceso no autorizado")
        st.stop()
    
    st.title("📊 Dashboard - Venta General")
    tab1, tab2, tab3 = st.tabs(["🌎 Ventas por Ciudad en EE.UU.", "👨‍💼 Productos Vendiddos por Empleado", "📊 Reporte Comparativo"])

    df_mapa =  extraccion_venta.obtener_dataframe_vendedor(0)
    with tab1:        
        mapaPais.main_pais(df_mapa)

    with tab2:
        empleados.main_empleado(df_mapa)

    with tab3:
        
            st.warning(f"⚠️ Reporte en construcción.")
        
    # Tu contenido normal aquí
    


    