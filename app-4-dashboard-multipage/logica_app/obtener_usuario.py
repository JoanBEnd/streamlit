
import sys
import os

# Obtener la ruta absoluta del directorio raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregar la carpeta raíz del proyecto a sys.path
sys.path.insert(0, BASE_DIR)

# Importar los módulos
from conecction import cn 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import pandas as pd



def obtener_rol(id_Usuario: int) -> str:
    engine = cn.get_db_connection()  # Obtener la conexión con SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query = text("SELECT Cargo FROM Dim_Empleado WHERE id_Empleado = :id")
        resultado = session.execute(query, {"id": id_Usuario}).fetchone()

        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Error al obtener el rol: {e}")
        return None
    finally:
        session.close()  # Cerrar la sesión correctamente


def obtener_empleado(id_Usuario: int) -> str:
    engine = cn.get_db_connection()
    Session = sessionmaker(bind=engine)
    session = Session() 
    try:
        query = text("Select concat(apellido,' ', nombre) as empleado from dim_empleado where id_empleado = :id_empleado")
        resultado = session.execute(query, {"id_empleado": id_Usuario}).fetchone()

        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Error al obtener el rol: {e}")
        return None
    finally:
        session.close()

    # conn = cn.get_db_connection()
    # if conn:
    #     cursor = conn.cursor()
    #     cursor.execute("""SELECT CONCAT(apellido, ' ', nombre) AS empleado 
    #    FROM dim_empleado 
    #    WHERE id_empleado = ?""", (id_Usuario,))
    #     resultado = cursor.fetchone()
    #     conn.close()

    #     return resultado[0] if resultado else None
