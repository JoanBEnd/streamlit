import sqlalchemy



# Crear cadena de conexión para SQLAlchemy

def conectar_db():
    connection_string = "mssql+pyodbc://@DESKTOP-JI4V2CK\SQLEXPRESS/Retail_ventasDM?trusted_connection=yes&driver=SQL+Server"

    engine = sqlalchemy.create_engine(connection_string)
    return engine

