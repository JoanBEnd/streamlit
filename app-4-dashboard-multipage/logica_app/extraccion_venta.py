from conecction import cn 
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import pandas as pd


def obtener_dataframe_vendedor(id_Usuario: int) -> pd.DataFrame:
    engine = cn.get_db_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        
        query = f"exec sp_obtener_dataframe_vendedor ?"                        
        df_venta = pd.read_sql_query(query, engine, params=(id_Usuario,) )

        orden_meses = ["ene", "feb", "mar", "abr", "may", "jun","jul", "ago",
                 "sep","oct", "nov", "dic"]

        df_venta["mes"] = pd.Categorical(
        df_venta["mes"],
        categories=orden_meses,
        ordered=True
            )

        return df_venta                         
    except Exception as e:
        
        print(f"error en la funcion obtener_dataframe_vendedor: {e}")
        return pd.DataFrame()
    finally:
        session.close()