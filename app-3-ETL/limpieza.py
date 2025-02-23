import coneccion as cn
import pandas as pd

conexion = cn.conectar_db()

# df_clientes = pd.read_sql("select Id_Cliente, CONCAT(apellido, ' ',nombre) Cliente 	,	Genero,	Edad from Dim_Cliente", conexion)
# df_productos = pd.read_sql("select * from Dim_Producto", conexion)
# df_empleados = pd.read_sql("Select id_Empleado, CONCAT(Apellido, ' ',Nombre) Trabajador,	Cargo  from Dim_Empleado", conexion)
# df_tiempo = pd.read_sql("Select * from Dim_Tiempo", conexion)
# df_ventas = pd.read_sql("Select * from H_Ventas", conexion)
# #Convertimos el campo fecha a datetime
# df_tiempo["fecha_registro"] =  pd.to_datetime(df_tiempo["fecha_registro"])

# df_venta_completa = df_ventas.merge(df_clientes, on="Id_Cliente", how="left")
# df_venta_completa = df_venta_completa.merge(df_empleados, left_on="Id_Empleado", right_on="id_Empleado", how="left").drop(columns=["id_Empleado"])
# df_venta_completa = df_venta_completa.merge(df_productos, on="Id_Producto", how="left" )
# df_venta_completa =  df_venta_completa.merge(df_tiempo, left_on="Transaccion_ID", right_on="transaccion_id", how="left").drop(columns=["transaccion_id"])




def devolver_dataframe():

    df_venta_general = pd.read_sql("""                               
                                    SELECT h.Transaccion_ID, h.Id_Cliente, h.Id_Empleado, h.Id_Producto, h.Cantidad, h.Precio_unitario, h.Total ,
                                            CONCAT(d.Nombre,' ', d.Apellido) Cliente, d.Genero, d.Edad,
                                            CONCAT(de.Nombre,' ', de.Apellido) Empleado, de.Cargo,
                                            dp.id_Categoria, dp.Categoria, dp.Producto,
                                            dt.transaccion_id, dt.fecha_registro
                                    FROM H_Ventas h
                                    inner JOIN Dim_Cliente d ON d.Id_Cliente = h.Id_Cliente
                                    inner JOIN Dim_Empleado  de ON h.Id_Empleado = de.id_Empleado
                                    inner JOIN Dim_Producto dp ON h.Id_Producto = dp.Id_Producto
                                    inner JOIN Dim_Tiempo dt ON h.Transaccion_ID = dt.transaccion_id
                                """, conexion) 





    df_venta_general["Año"] = df_venta_general["fecha_registro"].dt.year
    df_venta_general["Mes"] = df_venta_general["fecha_registro"].dt.month_name()
    df_venta_general["Mes_Abrev"] = df_venta_general["Mes"].str.slice(0,3)

    orden_meses = [
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ]
    
    orden_meses_less = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]

#Usando pd.Categorical() nos permitira darle el orden correspondiente.

    df_venta_general["Mes"] = pd.Categorical(
        df_venta_general["Mes"],
        categories=orden_meses,
        ordered=True
    )
    df_venta_general["Mes_Abrev"] = pd.Categorical(
        df_venta_general["Mes_Abrev"],
        categories=orden_meses_less,
        ordered=True
    )

   

    return df_venta_general