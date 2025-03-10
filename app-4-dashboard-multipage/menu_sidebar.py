import streamlit as st
from streamlit_option_menu import option_menu
import urllib.parse 
from logica_app import obtener_usuario

def show_main_content():
    # Sidebar con navegación
    with st.sidebar:       
       
        st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")   
        id_usuario = int(st.session_state.idUser)
        vendedor = obtener_usuario.obtener_empleado(id_usuario)    
        st.sidebar.subheader(f"Bienvenido, {vendedor}")
        
        
        # Menú según rol
        menu_items = []
        if st.session_state.role in ["Vendedor"]:
            menu_items.extend(["Dashboard Venta"])
            menu_items.extend(["Dashboard Histórico"])
        if st.session_state.role in ["Jefe de Venta"]:
            menu_items.extend(["Dashboard Jefatura"])
        
        selected = option_menu(
            menu_title="Menú Principal",
            options=menu_items + ["Logout"], #"Settings",
            icons=["box"]*len(menu_items) + ["door-open"] , #"gear", 
            default_index=0,
            styles={
                "container": {
                    
                    "background-color": "#262730"
                },
                "icon": {"color": "#3498db", "font-size": "16px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "2px 0",
                    "color": "#84b0dc",
                    "border-radius": "8px",
                    "--hover-color": "#e9f5ff"
                },
                "nav-link-selected": {
                    "background-color": "#3498db",
                    "color": "white",
                    "font-weight": "normal"
                }
            }
        )
                
    
    # 5️⃣ Manejo de logout
    if selected == "Logout":
        st.session_state.clear()
        st.query_params.clear()
        st.rerun()
    
    # Contenido dinámico
    elif selected == "Dashboard Venta":
        from maquetacion.vendedor.dashboard import main
        main()
    elif selected == "Dashboard Histórico":
        from maquetacion.vendedor.dashboard_historico import main
        
        
        main()
    elif selected == "Dashboard Jefatura":
        from maquetacion.jefatura.dashboard import main
        main()
    # ... (agregar demás páginas de forma similar)