import requests
import datetime
import config
from api_controls import get_coordenadas, get_nombre_ciudad_by_coord
import pandas as pd
from collections import OrderedDict
import os


BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine?"

#Función para construir el nombre del Archivo .csv
def construir_nombre_archivo_csv():
    fecha = datetime.datetime.now().strftime('%Y-%m-%d')
    nombre_archivo = f'openweather/tiempodiario_{fecha}.csv'

    # Verificar si la carpeta no existe, la creamos
    nombre_carpeta = "openweather"
    if not os.path.exists(nombre_carpeta):
        # Crear la carpeta
        os.mkdir(nombre_carpeta)

    return nombre_archivo

def get_weather_data_coord(coord, dt):

    #Construimos URL y le pegamos a la API
    url = f'{BASE_URL}{coord}&dt={dt}&appid={config.OPENWEATHER_API_KEY}&units=metric'
    res = requests.get(url)

     #Si status code == 200, creamos el archivo con la info
    if res.status_code == 200:
        return res.json()            
    else:
        print("Error get_data_coord")
        return None

def get_weather_data_city(city, dt):
    coord = get_coordenadas(city)
    if coord is not None:
        res = get_weather_data_coord(coord, dt)
        return res
    else:
        print("Error get_data_city")
        return None

def get_weather_data_city_list(cityList):

    datos_relevantes = {
        "ciudad": [],
        "dia": [],
        "temperatura": [],
        "humedad": [],
        "descripcion": []
    }

    #Recorrer Array de Ciudades
    for city in cityList:
        
        dt = int(datetime.datetime.now().timestamp())
        print(f"Procesando {city}... por favor aguarde")

        #Recorremos los 5 dias
        for i in range (5):
            dt2 = dt - (i*86400) #Restamos i dias

            data = get_weather_data_city(city, dt2)
            if data is not None:
                # Seleccionar los campos relevantes del JSON
                datos_relevantes["ciudad"].append(city)
                datos_relevantes["dia"].append(datetime.datetime.fromtimestamp(dt2).strftime('%Y-%m-%d'))
                datos_relevantes["temperatura"].append(data['current']['temp'])
                datos_relevantes["humedad"].append(data['current']['humidity'])
                datos_relevantes["descripcion"].append(data['current']['weather'][0]['description'])           

    return datos_relevantes

def get_weather_data_coord_list(coordList):

    datos_relevantes = {
        "ciudad": [],
        "dia": [],
        "temperatura": [],
        "humedad": [],
        "descripcion": []
    }

    #Recorrer Array de Coordenadas
    for coord in coordList:
        
        dt = int(datetime.datetime.now().timestamp())
        print(f"Procesando coordenadas: {coord}... por favor aguarde")

        #Recorremos los 5 dias
        for i in range (5):
            dt2 = dt - (i*86400) #Restamos i dias

            data = get_weather_data_coord(coord, dt2)
            if data is not None:
                # Seleccionar los campos relevantes del JSON
                datos_relevantes["ciudad"].append(get_nombre_ciudad_by_coord(coord))
                datos_relevantes["dia"].append(datetime.datetime.fromtimestamp(dt2).strftime('%Y-%m-%d'))
                datos_relevantes["temperatura"].append(data['current']['temp'])
                datos_relevantes["humedad"].append(data['current']['humidity'])
                datos_relevantes["descripcion"].append(data['current']['weather'][0]['description'])           

    return datos_relevantes

def concatenar_diccionarios(dict1, dict2):
    total = OrderedDict()

    # Agregar valores del primer diccionario
    for key, value in dict1.items():
        total[key] = value

    # Agregar valores del segundo diccionario, concatenando si la clave ya existe
    for key, value in dict2.items():
        if key in total:
            total[key] += value
        else:
            total[key] = value
    
    return total

