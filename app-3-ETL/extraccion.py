import pandas as pd


def obtener_total_producto(df_venta):
    return df_venta["Cantidad"].sum()

def obtener_años(df_venta):
    return df_venta["Año"].unique()


def obtener_categoria(df_venta):
    return df_venta["Categoria"].unique()

def obtener_total_ventas(df_venta):
    return df_venta["Total"].sum()

def obtener_porcentaje(df_venta, Total_Venta):
    #venta_empleado = df_venta["Total"].sum()     
    #return  round(venta_empleado / Total_Venta, 2) * 100

    porcentajes = (df_venta["Total"].sum() / Total_Venta) * 100
    return porcentajes.round(2)  # Redondeamos todo al final

def obtener_producto_cantidades(df_venta):
    df_venta_cantidad =  df_venta.groupby("Producto", as_index=False)["Cantidad"].sum()
    df_venta_cantidad = df_venta_cantidad.sort_values(by="Cantidad",   ascending=True)
    return df_venta_cantidad

def obtener_producto_ventas(df_venta):
    df_venta_total =  df_venta.groupby("Producto", as_index=False)["Total"].sum()
    df_venta_total = df_venta_total.sort_values(by="Total",   ascending=True)
    return df_venta_total



def obtener_empleado(df_venta):
    return df_venta["Empleado"].unique()

def obtener_venta_empleado_productos_por_mes(df_venta):
    df_venta_filtro = df_venta[["Empleado","Mes_Abrev","Cantidad"]]
    df_venta_filtro = df_venta_filtro.groupby(["Empleado", "Mes_Abrev"], observed=False)["Cantidad"].sum()
    df_venta_filtro = df_venta_filtro.fillna(0)
    df_venta_filtro = df_venta_filtro.reset_index()
    return df_venta_filtro

def obtener_venta_empleado_total_por_mes(df_venta):
    df_venta_filtro = df_venta[["Empleado","Mes_Abrev","Total"]]
    df_venta_filtro = df_venta_filtro.groupby(["Empleado", "Mes_Abrev"], observed=False)["Total"].sum()
    df_venta_filtro = df_venta_filtro.fillna(0)
    df_venta_filtro = df_venta_filtro.reset_index()
    return df_venta_filtro


def obtener_venta_empleado_categoria_por_mes(df_venta):
    df_venta_filtro = df_venta[["Categoria","Mes_Abrev","Cantidad"]]
    df_venta_filtro = df_venta_filtro.groupby(["Categoria", "Mes_Abrev"], observed=False)["Cantidad"].sum()
    df_venta_filtro = df_venta_filtro.fillna(0)
    df_venta_filtro = df_venta_filtro.reset_index()
    return df_venta_filtro

def obtener_venta_empleado_total_categoria_por_mes(df_venta):
    df_venta_filtro = df_venta[["Categoria","Mes_Abrev","Total"]]
    df_venta_filtro = df_venta_filtro.groupby(["Categoria", "Mes_Abrev"], observed=False)["Total"].sum()
    df_venta_filtro = df_venta_filtro.fillna(0)
    df_venta_filtro = df_venta_filtro.reset_index()
    return df_venta_filtro   