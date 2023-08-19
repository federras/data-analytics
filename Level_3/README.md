# Proyecto Python: Extracción, Almacenamiento en CSV y Carga en Base de Datos PostgreSQL

Este proyecto en Python demuestra cómo extraer datos de una API, almacenarlos en archivos CSV y luego cargar los datos desde los archivos CSV a una base de datos PostgreSQL. El proyecto consta de los siguientes pasos:

1. Instalar las dependencias del proyecto.
2. Extraer datos de una API externa y guardarlos en archivos CSV.
3. Leer los archivos CSV y cargar los datos en una base de datos PostgreSQL.

1. Instalar las dependencias del proyecto.
2. Crear las tablas en la base de datos.
3. Extraer datos de una API externa.
4. Almacenar los datos extraídos en la base de datos.

## Instalación

1.1. Clona este repositorio en tu máquina local:

   git clone https://github.com/tu-usuario/tu-proyecto.git
   cd tu-proyecto

1.2.  Crea un entorno virtual (opcional pero recomendado):

    python -m venv venv
    source venv/bin/activate

1.3.  Instala las dependencias del proyecto desde el archivo requirements.txt:

    pip install -r requirements.txt

2.1.  Extracción y Almacenamiento en CSV
      Antes de ejecutar el script de extracción, asegúrate de actualizar los detalles de conexión y la configuración de la API en el archivo config.py.

      python extract_and_store_csv.py

3. Crear Tablas en la Base de Datos
Antes de ejecutar los scripts para extraer y almacenar datos, asegúrate de tener una base de datos PostgreSQL configurada y de haber actualizado los detalles de conexión en el archivo config.py.

Ejecuta el siguiente comando para crear las tablas en la base de datos:
python create_tables.py



Almacenar Datos en la Base de Datos 
Después de haber extraído los datos, ejecuta el siguiente comando para almacenarlos en la base de datos PostgreSQL::
python store_data.py




