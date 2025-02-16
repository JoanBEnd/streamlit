import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Título de la aplicación
st.title("Explorando tendencias de tienda")

# Cargar datos
dt_tienda = pd.read_csv("data/shopping_trends.csv")



st.subheader("Vista previa de los datos")
st.write(dt_tienda.head())

st.subheader("Informacion del dataframe")
st.write(dt_tienda.info())


# Agregar un filtro por categoría si existe en los datos
if 'Category' in dt_tienda.columns:
    st.subheader("Filtrar por Categoria")
    #categoria = st.selectbox("Selecciona una categoria", dt_tienda["Category"].unique())    
    #filtered_df = dt_tienda[dt_tienda["Category"] == categoria]    
    #st.write(filtered_df)

    selected_categories = st.multiselect("Selecciona una o más categorias", dt_tienda["Category"].unique(), default=dt_tienda["Category"].unique())
    filtered_df = dt_tienda[dt_tienda["Category"].isin(selected_categories)]
    st.write(filtered_df.head())



# Agregar visualización de datos si existen columnas relevantes
if 'Purchase Amount (USD)' in dt_tienda.columns and 'Category' in dt_tienda.columns:
    st.subheader("Visualizacion de Compras por Categoria")
    
      # Gráfico con Matplotlib  
    fig, ax = plt.subplots()
    dt_tienda.groupby('Category')["Purchase Amount (USD)"].sum().plot(kind='bar', ax=ax)
    ax.set_ylabel("Total de Compras")    
    ax.set_title("Compras por Categoria")
    st.pyplot(fig)


  # Gráfico interactivo con Plotly
    st.subheader("Grafico interactivo de Compras por Categoria")
    data = dt_tienda.groupby("Category", as_index=False).sum()
    fig_plotly = px.bar(data, x="Category", y ="Purchase Amount (USD)",
                        title="Compras por Categoria",
                        color='Category',
                        hover_data=["Purchase Amount (USD)"]
                        )
    
    st.plotly_chart(fig_plotly)


    #Agregar un filtro de rango de compras
    st.subheader("Filtrar por Rango deCompras")
    min_val = int(dt_tienda["Purchase Amount (USD)"].min())
    max_val = int(dt_tienda["Purchase Amount (USD)"].max())
    purchase_range = st.slider("Selecciona un rango", min_val, max_val, (min_val, max_val))
    df_filtered_range = dt_tienda[(dt_tienda["Purchase Amount (USD)"] >= purchase_range[0]) & (dt_tienda["Purchase Amount (USD)"] <= purchase_range[1])  ]
    st.write(df_filtered_range)




    # Resumen de estadísticas
    #st.subheader("Resumen Estadístico de compras")
    #st.write(df_filtered_range["Purchase Amount (USD)"].describe())

    #boton de descargas
    st.subheader("Descargar Datos Filtrados")
    csv = df_filtered_range.to_csv(index=False).encode('utf-8')
    st.download_button(label="descargar CSV", data=csv, file_name="datos_filtrados.csv", mime="text/csv")


    st.subheader("Distribución de monto de compras")
    fig_dist = px.histogram(df_filtered_range, x="Purchase Amount (USD)", nbins=30, title="Distribución de Compras")
    st.plotly_chart(fig_dist)


    st.subheader("Boxplot de Monto de Compras")
    fig_box = px.box(df_filtered_range, y="Purchase Amount (USD)", title="Boxplot de compras")
    st.plotly_chart(fig_box)


    st.subheader("Mapa de Calor de correlaciones")
    numeric_df = df_filtered_range.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        fig_heatmap, ax= plt.subplots(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="RdYlGn", fmt='.2f', linewidths=0.5, ax=ax)
        st.pyplot(fig_heatmap)


    if 'Gender' in dt_tienda.columns:
        st.subheader("Proporción de Compras por Género")
        gender_purchases = df_filtered_range.groupby("Gender")["Purchase Amount (USD)"].sum().reset_index()
        fig_pie = px.pie(gender_purchases, names='Gender', values= 'Purchase Amount (USD)',
                         title="Proporción de Compras por Género", hole= 0.3)

        st.plotly_chart(fig_pie)