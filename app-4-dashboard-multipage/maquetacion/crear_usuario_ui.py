import streamlit as st
#from logica_app import crear_usuario_log
import sys
import os

# Obtener la ruta base del proyecto (proyecto/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregar la carpeta 'proyecto' al sys.path
sys.path.insert(0, BASE_DIR)

# Importar módulos desde logica_app
from logica_app import crear_usuario_log

def main():
    st.set_page_config(page_title="Crear credenciales", page_icon="🔐", layout="centered")

    with st.form(key="Crear credenciales", clear_on_submit=True):
        st.subheader(":green[Crear credenciales]")
        email = st.text_input("Correo", placeholder="Ingrese su correo registrado")
        usuario = st.text_input("Usuario", placeholder="Ingrese el usuario")
        password = st.text_input("Contraseña", placeholder="Ingrese la contraseña", type="password")

        submit_button = st.form_submit_button("Crear credenciales")

    if submit_button:
        if usuario and password:
            mensaje, tipo = crear_usuario_log.crear_usuario_clave(email, usuario, password)

            if tipo == "success":
                st.success(mensaje)
            else:
                st.error(mensaje)
        else:
            st.warning("Debe completar los datos")


if __name__ == "__main__":
    main()