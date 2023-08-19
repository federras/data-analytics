import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from helpers import get_weather_data_city_list, get_weather_data_coord_list, concatenar_diccionarios, construir_nombre_archivo_csv
from config import Config
import os


config = Config()

# Establecer la conexión a la base de datos PostgreSQL utilizando SQLalchemy
try:
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print("Conexión exitosa!")
except SQLAlchemyError as e:
    print("Error en la conexión:", e)

# Función para cargar datos de CSV a la base de datos
def load_data_to_database(csv_path):
    df = pd.read_csv(csv_path)
    table_name = "weather_data"
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Datos cargados en la tabla '{table_name}'.")

def get_csv_paths():
    # Obtener una lista de nombres de archivos en la carpeta
    nombres_archivos = os.listdir("openweather")
    # Filtrar solo los archivos CSV
    csv_paths = [os.path.join("openweather", archivo) for archivo in nombres_archivos if archivo.endswith(".csv")]
    return csv_paths

# Ruta de los archivos CSV generados previamente
csv_paths = get_csv_paths()

# Cargar datos de todos los archivos CSV a la base de datos
for csv_path in csv_paths:
    load_data_to_database(csv_path)