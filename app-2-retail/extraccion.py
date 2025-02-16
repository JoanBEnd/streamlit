import pandas as pd
#Filtros

def obtener_filtro_años(df_retail):
    return df_retail["Year"].unique()

def obtener_filtro_producto(df_retail):
    return df_retail["Product Category"].unique()


#Cards
def obtener_total_producto(df_retail):
    return df_retail["Quantity"].sum()

def obtener_total_ventas(df_retail):
    return df_retail["Total Amount"].sum()


#Lineas
def obtener_matriz_mes_año(df_retail):
    df_filtro = df_retail[["Year", "Month_less", "Total Amount"]]    
    df_filtro = df_filtro.groupby(["Month_less","Year"], observed=False)["Total Amount"].sum().unstack()
    df_filtro = df_filtro.fillna(0)
    df_filtro = df_filtro.reset_index()
    df_long = df_filtro.melt(id_vars=["Month_less"], var_name="Year", value_name="Total Amount")
    
    return df_long

def obtener_matriz_mes_año_producto(df_retail):
    df_filtro = df_retail[["Year", "Month_less", "Quantity"]]
    df_filtro = df_filtro.groupby(["Month_less", "Year"], observed=False)["Quantity"].sum().unstack()
    df_filtro = df_filtro.fillna(0)
    df_filtro = df_filtro.reset_index()

    df_long = df_filtro.melt(id_vars=["Month_less"], var_name="Year", value_name="Quantity")
    return df_long
