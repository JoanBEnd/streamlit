from sqlalchemy import create_engine
import urllib.parse
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Leer variables de entorno
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME") 

def get_db_connection():
    """ Crea y retorna una conexión SQLAlchemy a la base de datos """
    try:
        connection_string = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?trusted_connection=yes&driver=SQL+Server"
        # Crear motor SQLAlchemy
        engine = create_engine(connection_string)
        return engine

    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None



DB_NAME_OR = os.getenv("DB_NAME_OR") 

def get_db_base_original():
    try:
        connection_string = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME_OR}?trusted_connection=yes&driver=SQL+Server"
        # Crear motor SQLAlchemy
        engine = create_engine(connection_string)
        return engine

    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None
