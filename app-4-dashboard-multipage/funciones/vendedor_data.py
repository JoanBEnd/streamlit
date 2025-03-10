import pandas as pd

def obtener_años(df_vendedor):
    return df_vendedor["año"].unique()

def obtener_ciudades(df_vendedor):
    return df_vendedor["Ciudad"].unique()

def obtener_Total_venta(df_vendedor):
    return df_vendedor["Total"].sum()

def obtener_Total_producto(df_vendedor):
    return df_vendedor["Prod_Vendido"].sum()

def obtener_venta_mensual(df_vendedor):
  df_venta_filtro = df_vendedor[["Empleado","mes","Total"]]
  df_venta_filtro = df_venta_filtro.groupby(["Empleado","mes"],  observed=False)["Total"].sum()
  df_venta_filtro = df_venta_filtro.reset_index()  
  df_venta_filtro = df_venta_filtro[df_venta_filtro["Total"] > 0]  
  return df_venta_filtro

def obtener_venta_producto(df_vendedor):
    df_venta_filtro = df_vendedor[["Producto", "Total"]]
    df_venta_filtro = df_venta_filtro.groupby("Producto", observed=False)["Total"].sum()
    df_venta_filtro = df_venta_filtro.reset_index()
    df_venta_filtro = df_venta_filtro.sort_values(by="Total", ascending=False)
    return df_venta_filtro

def obtener_venta_mayor(df_vendedor):
    df_venta_filtro = df_vendedor[["mes_completo","Total"]]
    df_venta_filtro =df_venta_filtro.groupby(["mes_completo"],  observed=False)["Total"].sum().reset_index()  
    df_venta_filtro = df_venta_filtro.sort_values(by="Total", ascending=False)
    df_venta_filtro = df_venta_filtro.iloc[0]

    return df_venta_filtro


def obtener_venta_mes_actual(df_vendedor):
    df_venta_filtro = df_vendedor[["mes_completo","Total"]]
    df_venta_filtro =df_venta_filtro.groupby(["mes_completo"],  observed=False)["Total"].sum().reset_index()  
    df_venta_filtro = df_venta_filtro.sort_values(by="mes_completo", ascending=False)    
    df_venta_filtro = df_venta_filtro.iloc[0]    

    return df_venta_filtro


def obtener_categorias(df_vendedor):
    return df_vendedor["Categoria"].unique()


def obtener_venta_mensual_historico(df_vendedor):
  df_venta_filtro = df_vendedor[["año","mes","Total"]]
  df_venta_filtro = df_venta_filtro.groupby(["año","mes"],  observed=False)["Total"].sum()
  df_venta_filtro = df_venta_filtro.reset_index()  
  df_venta_filtro = df_venta_filtro[df_venta_filtro["Total"] > 0]  
  return df_venta_filtro