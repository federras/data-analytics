from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine


config = Config()

db = SQLAlchemy()

def conect_DB():
    config = Config()
    # Establecer la conexión a la base de datos PostgreSQL utilizando SQLalchemy
    try:
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        connection = engine.connect()
        print("Conexión exitosa!")
    except SQLAlchemyError as e:
        print("Error en la conexión:", e)