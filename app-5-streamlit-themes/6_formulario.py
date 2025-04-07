import streamlit as st
import re

st.title("Formulario de Registro")

dict_validacion = {
    "nombre" : None,
    "apellido": None,
    "fecha_nacimiento": None,
    "genero": None,
    "correo": None

}

def validar_correo(correo):
    return bool( re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo) )

def validar_texto(texto):
    return bool(re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", texto))

with st.form(key="Formulario"):

    dict_validacion["nombre"] = st.text_input("Ingrese el nombre:")
    dict_validacion["apellido"] = st.text_input("Ingrese el apellido:")
    dict_validacion["fecha_nacimiento"] = st.date_input("Ingrese su fecha de nacimiento", min_value="1910-01-01")
    dict_validacion["genero"] = st.selectbox("Seleccione el género", ["Masculino", "Femenino"])
    dict_validacion["correo"] = st.text_input("Ingrese el correo:")

    btn_registro = st.form_submit_button("Registrar")

    if btn_registro:

        if not all(dict_validacion.values()):
            st.warning("Por favor complete todos los datos.")
        elif not validar_texto(dict_validacion["nombre"]):
            st.warning("Por favor ingresar un nombre válido")
        elif not validar_texto(dict_validacion["apellido"]):
            st.warning("Por favor ingresar un apellido válido")
        elif not validar_correo(dict_validacion["correo"]):
            st.warning("Por favor ingresar un correo válido")
        else:
            nombre = dict_validacion["nombre"]
            apellido = dict_validacion["apellido"]
            fecha_nacimiento = dict_validacion["fecha_nacimiento"]
            genero = dict_validacion["genero"]
            correo = dict_validacion["correo"]
            st.success("Se realizo el registro.")
            st.text(f"Los datos ingresados son: {nombre} {apellido}, {fecha_nacimiento} , {genero}, {correo}")

    