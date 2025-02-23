
import streamlit as st
import pandas as pd
import plotly.express as px

# Simulación de datos
data = {
    "Mes_Abrev": ["Ene", "Ene", "Ene", "Feb", "Feb", "Feb", "Mar", "Mar", "Mar"],
    "Categoria": ["Electrónica", "Ropa", "Electrónica", "Ropa", "Electrónica", "Ropa", "Electrónica", "Ropa", "Electrónica"],
    "Empleado": ["Juan", "Ana", "Carlos", "Juan", "Ana", "Carlos", "Juan", "Ana", "Carlos"],
    "Total": [5000, 7000, 6000, 5200, 6800, 6200, 5400, 6600, 6400]
}

df = pd.DataFrame(data)

st.subheader("📈 Evolución Mensual del Total Vendido por Categoría")

# Primer nivel: Gráfico general por Categoría
graf_lineas_categoria = px.line(df, x="Mes_Abrev", y="Total", 
                                color="Categoria", 
                                markers=True, 
                                labels={"Total": "Venta Total", "Mes_Abrev": "Meses"})
st.plotly_chart(graf_lineas_categoria, use_container_width=True)

st.markdown("---")

# Segundo nivel: Drilldown por Categoría -> Ventas por Empleado
st.subheader("📊 Evolución Mensual por Empleado en Categoría Específica")

# Seleccionar una categoría
categorias = df["Categoria"].unique()
categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias)

# Filtrar los datos por categoría seleccionada
df_filtrado = df[df["Categoria"] == categoria_seleccionada]

# Gráfico de evolución mensual por empleado
graf_lineas_empleado = px.line(df_filtrado, x="Mes_Abrev", y="Total",
                               color="Empleado", 
                               markers=True, 
                               labels={"Total": "Venta Total", "Mes_Abrev": "Meses"})
st.plotly_chart(graf_lineas_empleado, use_container_width=True)