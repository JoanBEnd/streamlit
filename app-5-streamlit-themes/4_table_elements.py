import streamlit as st
import pandas as pd


mi_dataframe = pd.DataFrame(
    {
        "Nombre": ["Juan", "Ana", "Pedro", "María"],
        "Edad": [28, 22, 35, 30],
        "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    },
    columns=["Nombre", "Edad", "Ciudad"]
)

st.dataframe(mi_dataframe, use_container_width=True)

st.table(mi_dataframe)

st.write(mi_dataframe)

mi_tabla_editada =  st.data_editor(mi_dataframe, num_rows="dynamic", use_container_width=True)
print(mi_tabla_editada)

st.divider()


mi_json =  {
        "Nombre": ["Juan", "Ana", "Pedro", "María"],
        "Edad": [28, 22, 35, 30],
        "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    }

st.json(mi_json, expanded=True)

st.divider()

temp_actual = "20 °C"
var_temp = "-3 °C"

st.metric(label="Temperatura actual", value=temp_actual, delta=var_temp)