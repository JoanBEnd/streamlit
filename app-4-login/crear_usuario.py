import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

with st.form(key="Ingresar", clear_on_submit=True):
    st.subheader(":green[Log in]")
    correo = st.text_input("Correo", placeholder="Ingrese su correo registrado")
    usuario = st.text_input("Usuario", placeholder="Ingrese el usuario")
    password = st.text_input("Contraseña", placeholder="Ingrese la contraseña", type="password")

    st.form_submit_button("Ingresar")