import pandas as pd


def obtener_venta_calculada_ciudad(df_mapa_filtrado):
    df_mapa_calculado = df_mapa_filtrado[["Ciudad", "lat", "lon", "Total"]]
    df_mapa_calculado = df_mapa_calculado.groupby(["Ciudad", "lat", "lon"], observed=False)["Total"].sum()
    df_mapa_calculado = df_mapa_calculado.reset_index()
    
    #print(df_mapa_calculado.iloc[1]["Ciudad"])
    return df_mapa_calculado

def obtener_empleados(df_mapa_filtrado):
    df_mapa_empleado = df_mapa_filtrado["Empleado"].unique()

    return df_mapa_empleado

def obtener_empleados_top(df_mapa_filtrado):
    df_producto_venta = df_mapa_filtrado[["Empleado", "Total"]]
    df_producto_venta = df_producto_venta.groupby(["Empleado"], observed=False)["Total"].sum()    
    df_producto_venta = df_producto_venta.reset_index()
    df_producto_venta = df_producto_venta.sort_values(by="Total", ascending=False)

    return df_producto_venta

def obtener_venta_empleado(df_mapa_filtrado):
    return df_mapa_filtrado["Total"].sum()


def obtener_venta_empleado_mes(df_mapa_filtrado):
    df_empleado_venta = df_mapa_filtrado[["Empleado", "mes", "Total"]]
    df_empleado_venta = df_empleado_venta.groupby(["Empleado", "mes"], observed=False)["Total"].sum()    
    df_empleado_venta = df_empleado_venta.reset_index()
    df_empleado_venta = df_empleado_venta[df_empleado_venta["Total"] > 0]
    
    return df_empleado_venta



def obtener_venta_empleado_dia(df_mapa_filtrado):

 
      
    año = df_mapa_filtrado["año"].unique().max()
    mes = (df_mapa_filtrado["mes"]
            .drop_duplicates()  # Eliminar duplicados respetando el orden del DataFrame
            .sort_values()  # Ordenar según la categoría establecida
            .tolist()[-2:]  # Tomar los dos últimos meses correctamente
            )    
    print(mes)
    mes_completo = df_mapa_filtrado["mes_completo"].unique()[-1]
    print(df_mapa_filtrado["mes"].unique())
    df_mapa_filtrado = df_mapa_filtrado[(df_mapa_filtrado["año"] == año) &  (df_mapa_filtrado["mes"].isin(mes))]
    df_empleado_venta = df_mapa_filtrado[["Empleado","mes" ,"dia", "Total"]]
    df_empleado_venta = df_empleado_venta.groupby(["mes", "dia"], observed=False)["Total"].sum()    
    df_empleado_venta = df_empleado_venta.reset_index()
    df_empleado_venta = df_empleado_venta[df_empleado_venta["Total"] > 0]
    
    return df_empleado_venta, mes_completo


def obtener_venta_empleado_ciudad(df_mapa_filtrado):
    df_empleado_venta = df_mapa_filtrado[["Empleado", "Ciudad", "Total"]]
    df_empleado_venta = df_empleado_venta.groupby(["Empleado", "Ciudad"], observed=False)["Total"].sum()    
    df_empleado_venta = df_empleado_venta.reset_index()
    df_empleado_venta = df_empleado_venta.sort_values(by="Total", ascending=False)

    return df_empleado_venta

def obtener_venta_empleado_genero(df_mapa_filtrado):
    
    df_genero_venta = df_mapa_filtrado[["Genero", "Total"]]
    df_genero_venta = df_genero_venta.groupby(["Genero"], observed=False)["Total"].sum()    
    df_genero_venta = df_genero_venta.reset_index()
    df_genero_venta = df_genero_venta.sort_values(by="Total", ascending=False)

    return df_genero_venta

def obtener_venta_producto_empleado(df_mapa_filtrado):
    df_producto_venta = df_mapa_filtrado[["Producto", "Total"]]
    df_producto_venta = df_producto_venta.groupby(["Producto"], observed=False)["Total"].sum()    
    df_producto_venta = df_producto_venta.reset_index()
    df_producto_venta = df_producto_venta.sort_values(by="Total", ascending=False)

    return df_producto_venta
