import streamlit as st
import os
st.title("Proyecto de streamlit")
st.header("Titulo principal del proyecto.")
st.subheader("Titulo secundario del proyecto.")

variablePrincipal = "Python"
st.markdown(f"""
        Este curso nos ayudará a entender cómo funciona el modelo de lenguaje de OpenAI.
        Este curso estará desarrollado en {variablePrincipal}.
""")

st.text("Este es un texto de ejemplo.")

mensaje_error = "Este es un mensaje de error."
st.text(mensaje_error)

st.caption("Este texto es más pequeño.")

codigo_ejemplo = """
        def mi_funcion(variable1, variable2):
            return  variable1 + variable2

"""

st.code(codigo_ejemplo, language="python")


codigo_js = """
        function sumatoria(mi_lista){
            let suma = 0;
            for (let i = 0; i < mi_lista.length; i++){
                suma += mi_lista[i];
            }
            return suma;
        }
"""

st.code(codigo_js, language="javascript")

st.divider() 

st.image(os.path.join(os.getcwd(), "app-5-streamlit-themes", "images", "data_analyst.jpg"), width=150)
st.image(os.path.join(os.getcwd(), "app-5-streamlit-themes", "images", "dev_programer.jpg"), width=150)