
import streamlit as st

st.title("Formulario")
 
with st.form(key="Formulario"):
    nombre = st.text_input("Ingresa tu nombre")
    apellido = st.text_input("Ingresa tu apellido")

    fecha_nacimiento = st.date_input("Ingresa tu fecha de nacimiento", min_value="1930-01-01")
    genero = st.radio("Selecciona tu género", ["Masculino", "Femenino"])

    #profesion = st.selectbox("Selecciona una profesión", ["Ingeniero", "Arquitecto", "Diseñador"])
    profesion = st.selectbox("Selecciona una profesión",["Ingeniero", "Arquitecto", "Diseñador"])

    habilidades = st.multiselect("Selecciona tus habilidades", ["Python", "Java", "JavaScript"])

    notificar = st.checkbox("¿Desea ser notificado?")
    estudios = None

    bt_registro = st.form_submit_button("Registrar")
    print(nombre, apellido, fecha_nacimiento, genero, profesion, habilidades, notificar)    
    if bt_registro:
        st.text(f"""Hola {nombre} {apellido}, tu fecha de nacimiento es {fecha_nacimiento}, tu género es {genero},  tu profesión es {profesion}, tus habilidades son {', '.join(habilidades)} """)

