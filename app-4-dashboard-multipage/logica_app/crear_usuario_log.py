
import sys
import os

# Obtener la ruta absoluta del directorio raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregar la carpeta raíz del proyecto a sys.path
sys.path.insert(0, BASE_DIR)

# Importar los módulos
from conecction import cn
from funciones import security_password
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import pandas as pd

def crear_usuario_clave(email: str, usuario: str, password: str) -> tuple:
    
    engine = cn.get_db_base_original()  # Obtener la conexión con SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        password_hashed, salt = security_password.crear_password(password)
        id_Usuario = obtener_usuarioId_correo(email)
        query = f"exec sp_Crear_usuario ?, ?, ?, ?,"
        df_rpta = pd.read_sql_query(query, engine, params=(id_Usuario, usuario, password_hashed, salt, ))
        return "Usuario creado con exito", "success"
        
    except Exception as e:
        return f"Error al crear usuario: {e}", "error"
    finally:
        session.close()
    

def obtener_usuarioId_correo(email: str) -> int:
    engine = cn.get_db_base_original()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        query = text("select id_Empleado from empleado where correo = :email")
        resultado= session.execute(query, {"correo": email}).fetchone()

        return resultado[0] if resultado else None
    
    except Exception as e:
        return f"Error al crear usuario: {e}", "error"
    finally:
        session.close()

    
def validar_credenciales_login(usuario: str, password: str) -> tuple:
    engine = cn.get_db_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        query = text("select id_Empleado, Password, salt from Dim_Usuario where UserName = :usuario")
        resultado = session.execute(query, {"usuario": usuario}).fetchmany(2)

        id_Usuario, pass_save, salt_save =  resultado[0]
        validacion = security_password.verificar_password(password, pass_save, salt_save)
        
        return id_Usuario, validacion
    
    except Exception as e:
        return f"Error al crear usuario: {e}", "error"
    finally:
        session.close()



