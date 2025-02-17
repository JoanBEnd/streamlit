
import pandas as pd
import numpy as np

def devolver_dataFrame():
    dt_retail = pd.read_csv("app-2-retail/data/retail_sales_dataset.csv", parse_dates=["Date"])
    #Creamos las columnas Año, Mes, Mes Abreviado y Rango de edad
    dt_retail["Year"] = dt_retail["Date"].dt.year
    dt_retail["Month"] = dt_retail["Date"].dt.month_name()
    dt_retail["Month_less"] = dt_retail["Date"].dt.month_name().str.slice(0,3)

#En esta parte del código lo que haremos es darle un orden a los meses, para que cuando grafiquemos los meses salgan en el orden correcto
#para ello creamos una lista tanto de la columna Month y Month_less
    orden_meses = [
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ]
    
    orden_meses_less = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]

#Usando pd.Categorical() nos permitira darle el orden correspondiente.

    dt_retail["Month"] = pd.Categorical(
        dt_retail["Month"],
        categories=orden_meses,
        ordered=True
    )
    dt_retail["Month_less"] = pd.Categorical(
        dt_retail["Month_less"],
        categories=orden_meses_less,
        ordered=True
    )


    #Creando el rango de edades:
    #Linespace me permite crear una lista de numeros igualmente espaciados partiendo entre el numero_inicio, numero_fin y que se dividan n valores.

    bins = np.linspace(dt_retail["Age"].min(), dt_retail["Age"].max(), num=8)
    
    #Acá empezamos a recorrer estos numeros para armar los rangos de edades
    labels = [f"{int(bins[i])} - {int(bins[i+1])}"  for i in range(len(bins) - 1)]

    #Luego de obtener la lista de rango de edades usando pd.cut() podemos asignara a que rango perteneria cada edad.
    dt_retail["Rango_Edad"] = pd.cut(dt_retail["Age"], bins=bins, labels=labels, include_lowest=True)
    #ejemplo:
            #    Age	Rango_Edad
            #    21	     18 - 26
            #    45	     44 - 53
            #    67	     62 - 71

    #pd.cut() toma cada valor en Age y lo ubica dentro de los bins:
            #Si una persona tiene 21 años, cae en el rango 18 - 26.
            #Si una persona tiene 45 años, cae en 44 - 53.

    return dt_retail