# LEVEL 1
Este pequeño proyecto demuestra cómo extraer el clima actual de distintas ciudadades y de coordenadas cargadas de dos arrays, y almacenarlos localmente en un archivo .csv. Para esto usaremos la API de openweathermap.org.

### Instalación
Clona este repositorio en tu máquina local

    git clone https://github.com/federras/data-analytics.git
    cd Level_1

### Configuración de la API de OpenWeatherMap

Una vez que tengas tu API KEY, actualiza el valor de la variable OPENWEATHER_API_KEY en el archivo config.py

### Ejecución de la extracción

Ejecuta el comando en la consola:

    python3 main.py

----------------------------------------------------------------------------------

# LEVEL 2
## Proyecto Python: Extracción, Almacenamiento en CSV y Carga en Base de Datos PostgreSQL

Para este proyecto se utiliza la API de openweathermap.org para extraer el clima de 5 días (la fecha de hoy y 4 días atrás) de distintas ciudades cargadas en 2 arrays (hardcode) en donde un array tiene nombre de ciudades, y otro tiene latitud y longitud.
El objetivo del proyecto es demostrar mediante Python, cómo extraer datos de una API, almacenarlos en archivos CSV y luego cargar los datos desde los archivos CSV a una base de datos PostgreSQL.

El proyecto consta de los siguientes pasos:

1. Instalar las dependencias del proyecto.
2. Extraer datos de una API externa y guardarlos en archivos CSV.
3. Leer los archivos CSV y cargar los datos en una base de datos PostgreSQL.

### 1. Instalación

1. Clona este repositorio en tu máquina local si no lo hiciste antes, luego accede a la carpeta Level_2

   cd Level_2

2.  Crea un entorno virtual (opcional pero recomendado):

    python3 -m venv venv
    source venv/bin/activate

3.  Instala las dependencias del proyecto desde el archivo requirements.txt:

    pip install -r requirements.txt
    
### 2. Extracción y Almacenamiento en CSV

Antes de ejecutar el script de extracción, asegúrate de actualizar los detalles de conexión a la base de datos y la api_key de Open Weather para poder acceder a a la API, en el archivo config.py. Abre el archivo config.py y completa las siguientes variables:

    OPENWEATHER_API_KEY=
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_NAME = ""

Luego ejecuta:

    python3 extract.py

### 3. Crear Tablas en la Base de Datos

1. Ejecuta el siguiente comando para crear las tablas en la base de datos:

        python3 create_tables.py

2. Almacenar Datos en la Base de Datos
Después de haber extraído los datos, ejecuta el siguiente comando para almacenarlos en la base de datos PostgreSQL:
    
        python3 store_data.py

--------------------------------------------------------------------------------
# LEVEL 3
Esta última versión del proyecto incluye todos los elementos presentes en el nivel 2. Además, incorporamos el uso de Flask para ejecutar un servidor y renderizar diversas vistas.
Repetiremos los pasos por si querés directamente correr este nivel:

### 1. Instalación

1. Clona este repositorio en tu máquina local si no lo hiciste antes, luego accede a la carpeta Level_2

   cd Level_3

2.  Crea un entorno virtual:

    python3 -m venv venv
    source venv/bin/activate

3.  Instala las dependencias del proyecto desde el archivo requirements.txt:

    pip install -r requirements.txt
    
### 2. Extracción y Almacenamiento en CSV

Antes de ejecutar el script de extracción, asegúrate de actualizar los detalles de conexión a la base de datos y la api_key de Open Weather para poder acceder a a la API, en el archivo config.py. Abre el archivo config.py y completa las siguientes variables:

    OPENWEATHER_API_KEY=
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_NAME = ""

Luego ejecuta:

    python3 extract.py

### 3. Crear Tablas en la Base de Datos

1. Ejecuta el siguiente comando para crear las tablas en la base de datos:

        python3 create_tables.py

2. Almacenar Datos en la Base de Datos
Después de haber extraído los datos, ejecuta el siguiente comando para almacenarlos en la base de datos PostgreSQL:
    
        python3 store_data.py

### 3. Puesta en marcha del proyecto
Ejecuta
    
    python3 app.py

¡El proyecto está listo para funcionar!

Puedes acceder a la interfaz web haciendo Ctrl+Click Izq. sobre la direccion del localhost:  http://127.0.0.1:5000

Con la direccion http://127.0.0.1:5000/mostrar_datos se peude visualizar el clima de todas las ciudades almacenadas en la base de datos PostgreSQL los ultimos 5 dias.

En la raiz http://127.0.0.1:5000/ se puede consultar como esta el clima de cualquier ciudad en el momento actual.

En el endpoint http://127.0.0.1:5000/api/weather podemos enviar una solicitud get con una query city=nombre_ciudad y nos devolverá un json con la información.
