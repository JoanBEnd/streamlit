import streamlit as st
import urllib.parse
from logica_app import crear_usuario_log, obtener_usuario
# Configuración inicial 


if "role" not in st.session_state:
    st.session_state["role"] = None
if "idUser" not in st.session_state:
    st.session_state["idUser"] = None

# 1️⃣ Función para mantener la sesión con parámetros URL
def maintain_session():
    
    if not st.session_state["role"]:  # Si no está autenticado, redirigir al login
        st.rerun()


# 2️⃣ Función de login actualizada
def show_login():
    
    st.image("images/horizontal_blue.png", width=200) 

    with st.form(key="Ingresar"):
        #Ingresamos credenciales
        st.subheader(":green[Login]")
        usuario = st.text_input("Usuario", placeholder="Ingrese el usuario")
        password = st.text_input("Contraseña", placeholder="Ingrese la contraseña", type="password")

        submit_button = st.form_submit_button("Ingresar")
        #Validamos credenciales        
        if submit_button:
            if (usuario and password):
                id_user, validacion = crear_usuario_log.validar_credenciales_login(usuario, password)
                if validacion:
                    role = obtener_usuario.obtener_rol(id_user)
                    st.session_state["role"] = role
                    st.session_state["idUser"]= id_user
                    
                    st.rerun()
                    #Después de que todo este ok con las credenciales ejecuta st.rerun() que en
                    #actualiza la pagina y volvemos a leer código y como ya se tiene
                    #sesion iniciada entonces entrará al punto 4 y redirecciona al contenido principal.
                else:
                    st.error("Credenciales incorrectas")


   
 
 
if st.session_state["role"]:
    #Despues de que validamos y recarga la pagina login, entra a esta
    # parte del código - Importar y mostrar contenido principal
    maintain_session()  
    st.set_page_config(page_title="Intranet", layout="wide")    
    from menu_sidebar import show_main_content
    show_main_content()
else:
    st.set_page_config(page_title="Intranet", layout="centered")    
    show_login()