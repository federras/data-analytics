from datetime import datetime
import pandas as pd
import requests
import config
import os

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?";
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99",
             "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"];

#Función para construir el nombre del Archivo .csv
def construir_nombre_archivo_csv(data):
    fecha = datetime.utcfromtimestamp(data['dt']-10800).strftime('%Y-%m-%d')
    nombre_archivo = f'openweather/tiempodiario_{fecha}.csv'
    return nombre_archivo

# Verificar si la carpeta no existe, la creamos
nombre_carpeta = "openweather"
if not os.path.exists(nombre_carpeta):
    # Crear la carpeta
    os.mkdir(nombre_carpeta)

datos_relevantes = {
    "ciudad": [],
    "temperatura": [],
    "humedad": [],
    "descripcion": []
}
  
# Recorrer Array de coordenadas
for coord in coordList:

    #Construimos URL y le pegamos a la API
    url = f'{BASE_URL}{coord}&appid={config.OPENWEATHER_API_KEY}&units=metric'
    res = requests.get(url)

    #Si status code == 200, creamos el archivo con la info
    if res.status_code == 200:
        data = res.json()

        # Seleccionar los campos relevantes del JSON
        datos_relevantes["ciudad"].append(data['name'])
        datos_relevantes["temperatura"].append(data['main']['temp'])
        datos_relevantes["humedad"].append(data['main']['humidity'])
        datos_relevantes["descripcion"].append(data['weather'][0]['description'])
    else:
        print(coord, res.json())


#Recorrer Array de Ciudades
for city in cityList:

    #Construimos URL y le pegamos a la API
    url = f'{BASE_URL}q={city}&appid={config.OPENWEATHER_API_KEY}&units=metric'
    res = requests.get(url)
    
    #Si status code == 200, creamos el archivo con la info
    if res.status_code == 200:
        data = res.json()

        # Seleccionar los campos relevantes del JSON
        datos_relevantes["ciudad"].append(data['name'])
        datos_relevantes["temperatura"].append(data['main']['temp'])
        datos_relevantes["humedad"].append(data['main']['humidity'])
        datos_relevantes["descripcion"].append(data['weather'][0]['description'])
              
    else:
        print(city, res.json())

# Crear un DataFrame de pandas con los datos relevantes
df = pd.DataFrame(datos_relevantes)

# Guardar el DataFrame en un archivo CSV
ruta_archivo_csv = construir_nombre_archivo_csv(data)
df.to_csv(ruta_archivo_csv, index=False)