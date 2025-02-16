
import pandas as pd
import numpy as np

def devolver_dataFrame():
    dt_retail = pd.read_csv("app-2-retail/data/retail_sales_dataset.csv", parse_dates=["Date"])
    dt_retail["Year"] = dt_retail["Date"].dt.year
    dt_retail["Month"] = dt_retail["Date"].dt.month_name()
    dt_retail["Month_less"] = dt_retail["Date"].dt.month_name().str.slice(0,3)

    orden_meses = [
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ]
    
    orden_meses_less = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
    
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
    bins = np.linspace(dt_retail["Age"].min(), dt_retail["Age"].max(), num=8)

    labels = [f"{int(bins[i])} - {int(bins[i+1])}"  for i in range(len(bins) - 1)]

    dt_retail["Rango_Edad"] = pd.cut(dt_retail["Age"], bins=bins, labels=labels, include_lowest=True)

    return dt_retail