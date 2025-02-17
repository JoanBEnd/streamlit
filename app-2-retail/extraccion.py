import pandas as pd
#Filtros

def obtener_filtro_años(df_retail):
    #Obtenemos la lista unica de años
    return df_retail["Year"].unique()

def obtener_filtro_producto(df_retail):
    #Obtenemos la lista unica de productos
    return df_retail["Product Category"].unique()


#Cards
def obtener_total_producto(df_retail):
    #Obtenemos la suma total de los productos vendidos
    return df_retail["Quantity"].sum()

def obtener_total_ventas(df_retail):
    #Obtenemos la suma total de las ventas.
    return df_retail["Total Amount"].sum()


#Lineas
def obtener_tabla_mes_año_venta(df_retail):
    #OBtenemos el total de la venta por mes y año
    df_filtro = df_retail[["Year", "Month_less", "Total Amount"]]        
    df_filtro = df_filtro.groupby(["Month_less","Year"], observed=False)["Total Amount"].sum()
    df_filtro = df_filtro.fillna(0)
    df_filtro = df_filtro.reset_index()
    return df_filtro

def obtener_tabla_mes_año_producto(df_retail):
    #OBtenemos el total de prodiuctos por mes y año
    df_filtro = df_retail[["Year", "Month_less", "Quantity"]]
    df_filtro = df_filtro.groupby(["Month_less", "Year"], observed=False)["Quantity"].sum()
    df_filtro = df_filtro.fillna(0)
    df_filtro = df_filtro.reset_index()

    return df_filtro
