OPENWEATHER_API_KEY="1e2566e8d350e5d5a0c41ea6c5eacb8a"

class Config:
    # Configuración de la conexión a la base de datos PostgreSQL
    DB_USERNAME = "postgres"
    DB_PASSWORD = "feder123"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "informatorioAnalisisDatos"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"