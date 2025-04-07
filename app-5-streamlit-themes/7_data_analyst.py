import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard Ventas", layout="wide")

miDataFrame = pd.read_csv("app-5-streamlit-themes/data/ventas.csv", parse_dates=["Date"])
miDataFrame["Año"] = miDataFrame["Date"].dt.year
miDataFrame["Mes"] =  miDataFrame["Date"].dt.month_name()
print(miDataFrame)

columnas_tiempo, columnas_barra = st.columns(2)

with columnas_tiempo:
    st.subheader("Gráfica ventas por mes")
    miDataFrameTiempo = miDataFrame[["Año", "Mes", "Total Amount"]]
    miDataFrameTiempo = miDataFrameTiempo.groupby(["Año", "Mes"], observed=False)["Total Amount"].sum()
    miDataFrameTiempo = miDataFrameTiempo.reset_index()

    miGraficaTiempo = px.line(miDataFrameTiempo, x="Mes", y="Total Amount", color="Año")
    st.plotly_chart(miGraficaTiempo, use_container_width=True)


with columnas_barra:
    st.subheader("Gráfica ventas por Producto.")
    miDataFrameProductos = miDataFrame[["Product Category", "Total Amount"]]
    miDataFrameProductos = miDataFrameProductos.groupby("Product Category", observed= False)["Total Amount"].sum()
    miDataFrameProductos = miDataFrameProductos.reset_index()

    miGraficaBarras = px.bar(miDataFrameProductos, x="Product Category", y="Total Amount", color="Product Category")
    st.plotly_chart(miGraficaBarras, use_container_width=True)